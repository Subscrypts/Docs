---
title: Subscrypts vs Unlock Protocol — Protocol Comparison
description: Comparison of Subscrypts subscription tokens with Unlock Protocol's NFT-based access keys for recurring payments.
tags:
  - comparison
  - unlock-protocol
  - nft
  - access-control
  - subscrypts
---

# Subscrypts vs Unlock Protocol

Subscrypts and Unlock Protocol both enable on-chain access control tied to payments, but they use different models to achieve it. Subscrypts manages subscriptions through a dedicated utility token and discrete billing cycles, while Unlock Protocol uses NFT-based keys that represent time-limited access. This page compares the two protocols across the dimensions that matter most to merchants and developers.

---

## Core Philosophy

**Subscrypts** is a subscription management protocol. Merchants create plans with defined billing cycles, and subscribers pay with SUBS (or USDC, auto-swapped). The protocol handles recurring payments, access verification, and community gating through built-in tools like the Discord bot.

**Unlock Protocol** is a membership and access protocol. Merchants deploy "Locks" (smart contracts), and users purchase "Keys" (NFTs) that grant access for a defined duration. When a key expires, the user must purchase or renew it. The model is closer to ticketing or membership passes than traditional subscription billing.

---

## Feature Comparison

| Feature | Subscrypts | Unlock Protocol |
|---|---|---|
| **Access model** | Subscription token -- active status tracked on-chain per billing cycle | NFT key -- ERC-721 token with expiration timestamp |
| **Payment token** | SUBS (native utility token) or USDC via auto-swap | Any ERC-20 token or native ETH (configurable per Lock) |
| **Pricing model** | USD-denominated (oracle-based) or SUBS-denominated | Token-denominated (set per Lock) |
| **Fiat-denominated pricing** | Yes -- Uniswap V3 mid-price oracle converts USD to SUBS at payment time | No native fiat denomination -- requires off-chain price management |
| **Billing cycle** | Automated recurring payments (monthly, weekly, custom) | Manual renewal or auto-renewal via Unlock's renewal bot |
| **Platform fee** | 1% per payment | No protocol fee on self-deployed Locks; Unlock Labs charges fees on hosted checkout |
| **Settlement** | Instant burn-and-mint (same transaction) | Direct transfer to Lock contract; merchant withdraws |
| **Chain support** | Arbitrum One | Multi-chain (Ethereum, Polygon, Optimism, Arbitrum, BNB, Gnosis, others) |
| **Compliance** | MiCAR-aligned (EU), sanctions checking, freeze/halt controls | No formal regulatory framework |
| **Discord integration** | Built-in bot with automatic role gating | Third-party integration via Swordy Bot or Guild.xyz |
| **Transferability** | Subscription status is non-transferable (tied to subscriber wallet) | Keys are NFTs and transferable by default (can be disabled) |
| **Refunds** | No chargebacks; cancellation stops future payments | No refunds by default; Lock manager can issue refunds manually |

---

## Access Model: Subscriptions vs NFT Keys

### Subscrypts: On-Chain Subscription Status

In Subscrypts, a subscription is an on-chain record that tracks:

- The subscriber's wallet address
- The plan they are subscribed to
- The current billing cycle
- Payment status (active, expired, cancelled)

Access is determined by querying the smart contract for the subscriber's current status. The Discord bot, dApp, and SDK all use this mechanism. There is no token that represents "access" -- the subscription state itself is the source of truth.

### Unlock Protocol: NFT Keys

In Unlock Protocol, access is represented by an **ERC-721 NFT** (a "Key"). Each Key has:

- An owner (wallet address)
- An expiration timestamp
- A Lock it belongs to (the specific membership/subscription contract)

Access is determined by checking whether the user holds a valid (non-expired) Key NFT for the relevant Lock. This model has the advantage of composability with NFT tooling (marketplaces, wallets, galleries) but also means that keys can be transferred or sold unless the Lock explicitly disables transfers.

---

## Pricing and Payment Flexibility

| Aspect | Subscrypts | Unlock Protocol |
|---|---|---|
| **Set price in USD** | Yes -- oracle-based conversion at payment time | Not natively -- must manage pricing off-chain |
| **Accept multiple tokens** | SUBS and USDC (auto-swapped in same transaction) | Any ERC-20 or native ETH (configured per Lock) |
| **Price stability for subscribers** | USD-denominated plans ensure consistent pricing | Token-denominated; price fluctuates with token value |
| **Price stability for merchants** | USD-denominated plans ensure predictable revenue | Depends on token chosen; volatile tokens mean variable revenue |

Subscrypts' USD-denominated pricing is a significant differentiator for merchants who want predictable revenue regardless of token price movements. Unlock Protocol's flexibility in accepting any token is useful in multi-token ecosystems but puts the burden of price management on the merchant.

---

## Compliance and Governance

| Aspect | Subscrypts | Unlock Protocol |
|---|---|---|
| **Regulatory framework** | MiCAR-aligned (EU) | No formal regulatory alignment |
| **Whitepaper** | Published, MiCAR-compliant | Technical documentation only |
| **Sanctions enforcement** | On-chain OFAC sanctions checking | No built-in sanctions checking |
| **Account freeze** | Admin can freeze specific wallets | No native account freeze mechanism |
| **Halt controls** | Granular halt states (payments, plan creation, conversions) | Lock manager can disable purchases |
| **Governance audit trail** | All admin actions emit on-chain events | Standard EVM event logs |

For merchants in regulated markets -- particularly in the EU -- Subscrypts provides compliance infrastructure that Unlock Protocol does not offer natively.

---

## Community Tools

### Subscrypts Discord Bot

Subscrypts includes a **built-in Discord bot** that:

- Links Discord accounts to wallet addresses
- Checks on-chain subscription status in real time
- Grants and revokes premium Discord roles automatically
- Provides admin commands for server setup and plan management
- Requires no third-party tools or custom development

### Unlock Protocol Community Gating

Unlock Protocol does not include a native Discord bot. Community gating requires third-party tools:

- **Guild.xyz** -- token-gating platform that supports Unlock Keys
- **Swordy Bot** -- Discord bot for NFT-based role assignment
- **Custom integrations** -- developers can build their own verification using Unlock's API

These tools work but add complexity, dependencies, and potential points of failure that Subscrypts' integrated solution avoids.

---

## Developer Experience

| Aspect | Subscrypts | Unlock Protocol |
|---|---|---|
| **SDK** | React SDK with hooks and components | JavaScript SDK, Paywall.js, Checkout UI |
| **Smart contract interaction** | Single proxy contract, published ABI | Deploy individual Lock contracts per membership |
| **Integration complexity** | Connect to one contract; query subscription status | Deploy Locks, manage keys, handle renewals |
| **Checkout experience** | dApp-integrated or embeddable via SDK | Hosted checkout page or Paywall.js overlay |
| **Event system** | Rich event logs for payments, renewals, cancellations | Standard ERC-721 Transfer events + Lock-specific events |
| **Documentation** | Comprehensive (this site) | Comprehensive (docs.unlock-protocol.com) |

Subscrypts offers a simpler integration path for subscription-specific use cases: one contract, one ABI, and a React SDK. Unlock Protocol provides more flexibility for diverse membership models but requires more setup -- deploying individual Lock contracts and managing NFT keys.

---

## When to Choose Subscrypts

- **You need recurring subscription billing.** Defined billing cycles with automated renewals are Subscrypts' core strength.
- **Compliance is a requirement.** MiCAR alignment, sanctions checking, and governance controls are built in.
- **You want built-in Discord monetization.** No third-party bots or services needed.
- **USD-denominated pricing is important.** Stable pricing for merchants and subscribers without manual price management.
- **Non-transferable access is preferred.** Subscription status is tied to the subscriber's wallet and cannot be resold.
- **Low, predictable fees.** A flat 1% per payment with no hidden costs.

---

## When to Choose Unlock Protocol

- **You want NFT-based memberships.** If representing access as a transferable or collectible NFT is valuable for your use case (event tickets, collectible memberships, resellable passes), Unlock's model is a natural fit.
- **Multi-chain deployment is needed.** Unlock is deployed across many chains, giving you access to users on Polygon, Optimism, and others beyond Arbitrum.
- **You want to accept any ERC-20 token.** Unlock allows each Lock to accept different payment tokens, which is useful in multi-token ecosystems.
- **You need one-time purchases alongside memberships.** Unlock supports both time-limited keys and permanent keys, making it suitable for one-time access sales.
- **NFT ecosystem composability matters.** Unlock Keys work with NFT marketplaces, wallets, and tooling out of the box.

---

## Summary

| | Subscrypts | Unlock Protocol |
|---|---|---|
| **Best for** | Recurring subscriptions, Discord communities, compliance-sensitive merchants | NFT memberships, multi-chain access, collectible passes |
| **Access model** | On-chain subscription status | NFT key with expiration |
| **Pricing** | USD or SUBS-denominated | Token-denominated per Lock |
| **Compliance** | MiCAR-aligned, built-in | No formal compliance |
| **Discord** | Native bot | Third-party tools required |
| **Transferability** | Non-transferable | Transferable (configurable) |

Both protocols serve legitimate on-chain access control needs. Subscrypts is optimized for subscription-style billing with compliance and community tools, while Unlock Protocol excels in NFT-native membership scenarios with multi-chain flexibility.

---

## Related

- [Subscrypts vs Stripe, Patreon, and PayPal](vs-traditional-payments.md) -- Comparison with traditional payment platforms
- [Subscrypts vs Superfluid](vs-superfluid.md) -- Comparison with Superfluid's streaming model
- [Discord Bot Introduction](../discord-bot/introduction.md) -- How the Subscrypts Discord bot works
- [Smart Contract Architecture](../smart-contract/architecture.md) -- UUPS proxy and facet design
- [Getting Started for Merchants](../getting-started/for-merchants.md) -- Set up your first plan
