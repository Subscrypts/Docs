---
title: Subscrypts Deployment & Network Information
description: Technical details on the Subscrypts Smart Contract Suite deployment, network configuration, and contract addresses.
tags:
  - subscrypts
  - smart-contracts
  - deployment
  - network
  - arbitrum
  - uups
  - contracts
---

# Deployment & Network Information

The **Subscrypts Smart Contract Suite** is deployed on the **Arbitrum One** network and structured hybrid between the UUPS (Universal Upgradeable Proxy Standard) and a facet-based modular pattern. This section provides detailed information on network configuration, contract verification, and developer integration with deployed addresses.

---

## Deployment Overview

The [Subscrypts](https://subscrypts.com) deployment follows a **modular upgradeable proxy model**, ensuring every component can evolve independently while maintaining state persistence and backward compatibility.

| Component | Description | Deployment Type |
| ---------- | ------------ | ---------------- |
| **SubscryptsProxy** | Main UUPS proxy contract holding global state and delegating all calls. | Immutable address (upgradeable logic). |
| **SubscryptsLogic** | Core business logic for subscription lifecycle management. | Upgradeable logic contract. |
| **FacetSubscription** | Manages plan creation, renewals, and cancellations. | Modular facet (selector-mapped). |
| **FacetPaymentUSDC** | Handles atomic conversion and USDC->SUBS settlements. | Modular facet (selector-mapped). |
| **FacetAdmin** | Controls governance, upgrades, and halt mechanisms. | Modular facet (selector-mapped). |
| **FacetView** | Read-only query interface for public and SDK integrations. | Modular facet (selector-mapped). |
| **Uniswap Router / Quoter / Position Manager** | External DEX components for price discovery and conversion. | Verified Uniswap V3 addresses. |

---

## Network Configuration

**Primary Network:**

- **Network:** Arbitrum One
- **Chain ID:** 42161
- **RPC Endpoint:** `https://arb1.arbitrum.io/rpc`
- **Block Explorer:** [https://arbiscan.io](https://arbiscan.io)
- **Currency:** ETH (for gas)

---

## Contract Addresses

!!! info
    Addresses below correspond to the Subscrypts Arbitrum One release. Future versions will maintain proxy continuity.

| Contract | Address | Type |
| -------- | -------- | ---- |
| **SubscryptsProxy** | [`0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac`](https://arbiscan.io/address/0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac) | Entry point for all transactions. |
| **SubscryptsLogic** | [`0x46D53cE3090c5dB6e4acED58580f216dE7Be982F`](https://arbiscan.io/address/0x46D53cE3090c5dB6e4acED58580f216dE7Be982F) | Core UUPS implementation. |
| **FacetAdmin** | [`0xD97bdD4d5f4a950a713576175Ab9B8577d9D0f98`](https://arbiscan.io/address/0xD97bdD4d5f4a950a713576175Ab9B8577d9D0f98) | Admin & upgrade logic. |
| **FacetSubscription** | [`0xC2768593EF20aFba099Bc0Fbe726B1dAe8936c12`](https://arbiscan.io/address/0xC2768593EF20aFba099Bc0Fbe726B1dAe8936c12) | Subscription lifecycle logic. |
| **FacetPaymentUSDC** | [`0x424C7885190e55F6E3221E9919Ca4AE76D9fD889`](https://arbiscan.io/address/0x424C7885190e55F6E3221E9919Ca4AE76D9fD889) | USDC reference & pricing. |
| **FacetView** | [`0x32Ba23749c73181fB6133b21787d5a10C70ec835`](https://arbiscan.io/address/0x32Ba23749c73181fB6133b21787d5a10C70ec835) | Read-only helpers. |
| **SUBS Token** | [`0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac`](https://arbiscan.io/address/0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac) | ERC-20 utility token (same as proxy). |
| **SubscryptsTokenVesting** | [`0x409e092BD90ADDD9AB7FB94414D49A6562469491`](https://arbiscan.io/address/0x409e092BD90ADDD9AB7FB94414D49A6562469491) | TGE + linear vesting. |
| **SUBS/USDC Pair** | [`0xa8C221C5110FA82b0B90A6bA78227C2EE8061f48`](https://arbiscan.io/address/0xa8C221C5110FA82b0B90A6bA78227C2EE8061f48) | Uniswap V3 liquidity pair. |
| **Uniswap V3 Router** | [`0xE592427A0AEce92De3Edee1F18E0157C05861564`](https://arbiscan.io/address/0xE592427A0AEce92De3Edee1F18E0157C05861564) | Standard Uniswap V3 router. |
| **Uniswap V3 Quoter** | [`0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6`](https://arbiscan.io/address/0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6) | Standard Uniswap V3 quoter. |
| **USDC** | [`0xaf88d065e77c8cC2239327C5EDb3A432268e5831`](https://arbiscan.io/address/0xaf88d065e77c8cC2239327C5EDb3A432268e5831) | Circle USDC on Arbitrum. |

---

## Deployment Process

Deployment is performed via under a controlled CI/CD pipeline. The key steps include:

1. **Compile Contracts** using Solidity >=0.8.30 with optimization enabled.
2. **Deploy Logic Contracts** (`SubscryptsLogic`, `FacetSubscription`, etc.).
3. **Deploy Proxy Contract** with `initialize()` called post-deployment.
4. **Register Function Selectors** for each facet using `registerFacetSelector()`.
5. **Emit Deployment Events** to record addresses and version tags on-chain.

---

### Upgrade Process:

1. Governance deploys the new facet or logic contract.
2. Calls `upgradeToAndCall()` or `registerFacetSelector()` through `FacetAdmin`.
3. Emits `Upgraded` and `FacetSelectorUpdated` events for verification.
4. Existing data remains untouched within `SubscryptsStorage`.

---

## Environment Integration for Developers

Developers building integrations (dApps, SDKs, analytics dashboards) can use the following configuration template:

```js
export const subscryptsConfig = {
  network: 'Arbitrum One',
  rpcUrl: 'https://arb1.arbitrum.io/rpc',
  proxyAddress: '0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac',
  subsTokenAddress: '0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac', // same as proxy
  usdcAddress: '0xaf88d065e77c8cC2239327C5EDb3A432268e5831',
  uniswapRouter: '0xE592427A0AEce92De3Edee1F18E0157C05861564',
  uniswapQuoter: '0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6',
  vestingAddress: '0x409e092BD90ADDD9AB7FB94414D49A6562469491',
  abiUrl: 'https://files.subscrypts.com/abi/subscryptsABI-v1.json'
};
```

---

## Developer Verification Checklist

Before interacting with the production contracts, developers should verify:

- Network ID matches **42161 (Arbitrum One)**.
- ABI matches `subscryptsAbi-V#.json` (always use latest ABI version).
- The proxy contract emits `Upgraded` events for new versions.
- The `proxiableUUID()` matches the current logic version.
- DEX router and quoter addresses match official Uniswap V3 contracts.

---

## Summary

The Subscrypts deployment on **Arbitrum One** ensures a secure, scalable, and transparent environment for decentralized subscription management. Through its modular proxy design, verified deployment process, and consistent versioning, developers and auditors can confidently integrate, monitor, and extend the protocol without disrupting live data.

---

## Related Topics

- [Architecture Overview](architecture.md) — the modular UUPS proxy design that underpins deployment
- [Subscrypts ABI Reference](abi-reference.md) — the ABI used to interact with deployed contracts
- [Gas Optimization & Scalability](gas-optimization.md) — why Arbitrum One was chosen for deployment
- [Security & Auditing](security-auditing.md) — verification and audit procedures for deployed contracts
- [Getting Started for Developers](../getting-started/for-developers.md) — developer onboarding and setup

!!! ecosystem "Related Components"
    - [dApp Introduction](../dapp/introduction.md)
    - [SDK Provider Setup](../sdk/provider-setup.md)
    - [SDK Quick Start](../sdk/quick-start.md)
