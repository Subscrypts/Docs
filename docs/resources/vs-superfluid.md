---
title: Subscrypts vs Superfluid — Protocol Comparison
description: Technical comparison of Subscrypts and Superfluid covering payment models, architecture, compliance, and community tools.
tags:
  - comparison
  - superfluid
  - streaming
  - protocol
  - subscrypts
---

# Subscrypts vs Superfluid

Subscrypts and Superfluid both enable on-chain recurring payments, but they take fundamentally different approaches to how money moves, how contracts are structured, and what use cases they serve best. This page provides a technical, feature-level comparison.

---

## Core Philosophy

**Subscrypts** is purpose-built for subscription management. It uses discrete billing cycles, a dedicated utility token (SUBS), and integrates community tools like a Discord bot. The protocol is designed around compliance (MiCAR), privacy, and low fees.

**Superfluid** is a general-purpose money streaming protocol. It enables continuous, per-second token flows between wallets using its Constant Flow Agreement (CFA) framework. It serves a broad range of use cases including payroll, vesting, and real-time payments.

---

## Feature Comparison

| Feature | Subscrypts | Superfluid |
|---|---|---|
| **Payment model** | Discrete billing cycles (monthly, weekly, custom) | Continuous per-second streaming |
| **Architecture** | UUPS upgradeable proxy with modular facets | CFA (Constant Flow Agreement) framework with Super Tokens |
| **Token model** | Native SUBS utility token (ERC-20, burn-and-mint) | Super Token wrappers around existing ERC-20 tokens |
| **Chain support** | Arbitrum One (focused) | Multi-chain (Ethereum, Polygon, Optimism, Avalanche, BNB, others) |
| **Regulatory compliance** | MiCAR-aligned (EU); whitepaper published | No formal regulatory alignment |
| **Community integration** | Built-in Discord bot with role gating | No native community tools |
| **Pricing model** | USD-denominated or SUBS-denominated plans | Token-denominated flow rates only |
| **Settlement mechanism** | Burn-and-mint (atomic, same transaction) | Continuous streaming (balance decreases per second) |
| **Platform fee** | 1% per payment | No protocol fee (integrators may charge fees) |
| **Custody** | Non-custodial (funds burn and mint atomically) | Non-custodial (funds stream from sender balance) |
| **Subscriber experience** | Approve once, auto-renew each cycle | Maintain sufficient Super Token balance for ongoing stream |
| **Merchant experience** | Receive lump-sum per billing cycle | Receive continuous inflow per second |

---

## Payment Model: Cycles vs Streams

### Subscrypts: Discrete Billing Cycles

Subscrypts processes payments at defined intervals. A subscriber approves a plan, and at each billing cycle boundary the smart contract executes the payment -- burning SUBS from the subscriber and minting 99% to the merchant.

This model mirrors how traditional subscriptions work:

- Clear billing dates
- Predictable payment amounts
- Easy to reconcile with accounting systems
- Natural alignment with service access periods (e.g., "access for 30 days")

### Superfluid: Continuous Streaming

Superfluid moves tokens continuously. A subscriber opens a stream, and their Super Token balance decreases every second while the merchant's balance increases at the same rate.

This model is better suited for:

- Real-time payroll or compensation
- Usage-based billing that needs per-second granularity
- Vesting schedules
- Scenarios where continuous money flow is more appropriate than periodic billing

!!! note "Buffer deposits"
    Superfluid requires senders to maintain a buffer deposit (typically 4 hours' worth of flow) to protect against insolvency. If the sender's balance runs out, the stream is liquidated. Subscrypts has no buffer requirement -- payments either execute fully or fail cleanly.

---

## Architecture

### Subscrypts: UUPS Proxy with Facets

Subscrypts uses a **UUPS (Universal Upgradeable Proxy Standard)** architecture with modular facets. Each facet handles a specific domain (payments, plan management, compliance, view functions). The proxy delegates calls to the appropriate facet, and upgrades are governed by admin roles with on-chain event logging.

Key architectural properties:

- Single proxy entry point
- Modular logic separation via facets
- Upgrade events logged on-chain for auditability
- Compliance mechanisms (freeze, halt, sanctions) built into the contract

### Superfluid: CFA Framework with Super Tokens

Superfluid uses a **host contract** that manages agreements (primarily CFAs). Users wrap existing ERC-20 tokens into **Super Tokens** to enable streaming. The framework provides callbacks, composability with other DeFi protocols, and programmable cash flows.

Key architectural properties:

- Host contract orchestrates agreements
- Super Token wrappers add streaming capability to any ERC-20
- Highly composable with other protocols
- No built-in compliance or governance mechanisms

---

## Token Model

| Aspect | Subscrypts (SUBS) | Superfluid (Super Tokens) |
|---|---|---|
| **Token type** | Native ERC-20 utility token | Wrapped ERC-20 tokens (e.g., USDCx, DAIx) |
| **Payment mechanism** | Burn from subscriber, mint to merchant | Stream from sender balance to receiver |
| **Token supply impact** | Circulating supply unchanged (burn + mint are equal) | No supply change (tokens flow between wallets) |
| **Fiat-denominated pricing** | Yes -- USD plans use Uniswap V3 oracle for conversion | No -- flow rates are denominated in tokens only |
| **Token required** | SUBS (or USDC via auto-swap) | Any token with a Super Token wrapper |

---

## Chain Support

**Subscrypts** is deployed on **Arbitrum One** and is optimized for that environment. Arbitrum provides low gas fees, high throughput, and Ethereum-level security -- all of which align with the protocol's focus on affordable subscription payments.

**Superfluid** is deployed across many chains including Ethereum mainnet, Polygon, Optimism, Avalanche, BNB Chain, Celo, and others. This multi-chain approach gives Superfluid broader reach but also fragments liquidity and user bases across networks.

---

## Compliance

| Aspect | Subscrypts | Superfluid |
|---|---|---|
| **Regulatory framework** | MiCAR-aligned (EU Markets in Crypto-Assets) | No formal regulatory alignment |
| **Whitepaper** | Published, MiCAR-compliant | Technical documentation only |
| **Sanctions enforcement** | On-chain sanctions checking (OFAC integration) | No built-in sanctions checking |
| **Freeze capability** | Admin can freeze specific accounts | No account freeze mechanism |
| **Halt controls** | Granular halt states for payments, plan creation | No protocol-level halt mechanism |
| **Audit trail** | All governance actions emit on-chain events | Standard EVM event logs |

For businesses operating in the EU or in regulated industries, Subscrypts' compliance-by-design approach provides a meaningful advantage.

---

## Community and Integration Tools

**Subscrypts** includes a purpose-built **Discord bot** that:

- Verifies on-chain subscription status
- Grants and revokes Discord roles automatically
- Provides admin and subscriber commands
- Handles wallet linking and subscription sync

**Superfluid** does not provide native community integration tools. Discord bating or access control requires custom development or third-party solutions.

---

## When to Choose Subscrypts

- **You need subscription billing with defined billing cycles.** Monthly, weekly, or custom intervals with clear billing dates.
- **Compliance matters.** MiCAR alignment, sanctions checking, and governance audit trails are built in.
- **You want Discord monetization.** The built-in bot handles everything without third-party tools.
- **You prefer fiat-denominated pricing.** USD-priced plans with automatic token conversion protect merchants and subscribers from price volatility.
- **Low fees are important.** A flat 1% is predictable and competitive.
- **You value instant lump-sum settlement.** Each payment arrives in full, in one transaction.

---

## When to Choose Superfluid

- **You need continuous per-second money streaming.** Payroll, vesting, or real-time compensation are natural fits for Superfluid's CFA model.
- **Multi-chain deployment is required.** If your users are spread across Polygon, Optimism, and other chains, Superfluid's multi-chain presence is an advantage.
- **You want to stream existing tokens.** Superfluid wraps any ERC-20 into a Super Token, so you can stream USDC, DAI, or any supported asset without a protocol-specific token.
- **Composability with DeFi protocols is a priority.** Superfluid's programmable cash flows integrate with lending, DEXs, and other DeFi building blocks.
- **You need usage-based billing at sub-second granularity.** Metered services that bill per second or per minute align well with continuous streams.

---

## Summary

| | Subscrypts | Superfluid |
|---|---|---|
| **Best for** | Subscription billing, Discord communities, compliance-sensitive merchants | Real-time streaming, payroll, DeFi composability |
| **Payment style** | Discrete cycles | Continuous flow |
| **Compliance** | MiCAR-aligned, built-in | No formal compliance framework |
| **Community tools** | Discord bot included | None |
| **Chain focus** | Arbitrum One | Multi-chain |

Both protocols are non-custodial and operate on-chain. The right choice depends on whether your use case calls for periodic subscription billing or continuous token streaming.

---

## Related

- [Subscrypts vs Stripe, Patreon, and PayPal](vs-traditional-payments.md) -- Comparison with traditional payment platforms
- [Subscrypts vs Unlock Protocol](vs-unlock-protocol.md) -- Comparison with Unlock Protocol's NFT-based access
- [Smart Contract Architecture](../smart-contract/architecture.md) -- How the Subscrypts UUPS proxy works
- [Compliance & Transparency](../smart-contract/compliance.md) -- Deep dive into Subscrypts compliance mechanisms
