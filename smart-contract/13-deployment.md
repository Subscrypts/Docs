---
title: Deployment & Network Information
description: Technical details on the Subscrypts Smart Contract Suite deployment, including network configuration, contract addresses, and developer verification instructions.
tags:
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
| **FacetPaymentUSDC** | Handles atomic conversion and USDC→SUBS settlements. | Modular facet (selector-mapped). |
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

> **Note:** Addresses below correspond to the Subscrypts Arbitrum One release. Future versions will maintain proxy continuity.

| Contract | Address | Type |
| -------- | -------- | ---- |
| **SubscryptsProxy** | `0x0000...PROXY` | Entry point for all transactions. |
| **SubscryptsLogic)** | `0x0000...LOGIC` | Core implementation under UUPS proxy. |
| **FacetSubscription** | `0x0000...FSUB` | Subscription lifecycle logic. |
| **FacetPaymentUSDC** | `0x0000...FPAY` | Payment and USDC↔SUBS conversion. |
| **FacetAdmin** | `0x0000...FADM` | Governance and upgrades. |
| **FacetView** | `0x0000...FVIEW` | Query and data access. |
| **SubscryptsStorage** | (Proxy state reference) | Shared storage (internal only). |
| **Uniswap V3 Router** | `0xE592...1564` | Standard Uniswap V3 router. |
| **Uniswap Quoter** | `0xb273...dFFe` | Standard Uniswap V3 quoter. |

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
  proxyAddress: '0x0000...PROXY',
  uniswapRouter: '0xE592...1564',
  uniswapQuoter: '0xb273...dFFe',
  abiPath: '/docs/contracts/abi/subscryptsAbi-v1.json'
};
```

---

## Developer Verification Checklist

Before interacting with the production contracts, developers should verify:

- ✅ Network ID matches **42161 (Arbitrum One)**.
- ✅ ABI matches `subscryptsAbi-V#.json` (always use latest ABI version).
- ✅ The proxy contract emits `Upgraded` events for new versions.
- ✅ The `proxiableUUID()` matches the current logic version.
- ✅ DEX router and quoter addresses match official Uniswap V3 contracts.

---

## Summary

The Subscrypts deployment on **Arbitrum One** ensures a secure, scalable, and transparent environment for decentralized subscription management. Through its modular proxy design, verified deployment process, and consistent versioning, developers and auditors can confidently integrate, monitor, and extend the protocol without disrupting live data.

