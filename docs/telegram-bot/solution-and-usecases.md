---
title: Telegram Bot Use Cases
description: How the Subscrypts Telegram Bot enables decentralized, automated community monetization for Telegram groups and channels.
status: new
tags:
  - subscrypts
  - telegram
  - use cases
  - subscriptions
  - automation
  - monetization
---

# Solution & Use Cases

The **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)** transforms ordinary Telegram groups into **subscription-gated, automated premium communities**. It brings subscription logic on-chain and links it to group membership in Telegram, enabling a new class of decentralized community monetization.

## What Problem Does It Solve?

Traditional Telegram monetization faces several problems:

* Manual invite management for paying users
* Shared invite links that leak access to non-paying members
* Centralized payment tools that collect personal data and charge high fees
* No native support for crypto-native or unbanked users
* Constant administrative overhead to check who has paid and remove expired members

The **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)** solves this through:

* **Smart contract-managed payments** — billing handled entirely on-chain
* **On-chain subscription state = live group membership** — the bot mirrors blockchain truth
* **1% fee structure via SUBS token** — compared to 5–30% charged by centralized alternatives
* **Global access with zero banking dependency** — anyone with a crypto wallet can join

It's frictionless for both group owners and subscribers, with no email, no password, and no billing intermediaries.

---

## Key Use Cases

### 1. **Premium Telegram Communities**

**Example:** A creator runs a Telegram group with free and premium areas. They want to charge $10/month for access.

* They add the **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)** to their group.
* They create a subscription plan at [telegram.onsubscrypts.com](https://telegram.onsubscrypts.com).
* They map the plan to their group.
* Users subscribe via the per-group subscription page, **link their wallet** for that group via SIWE, and receive a single-use invite link.
* When the subscription expires, the member is automatically removed.

> Merchants don't touch payments. Subscribers stay in control.

### 2. **Alpha & Trading Groups**

**Example:** A crypto analyst runs a paid Telegram group for trading signals at $50/month.

* The **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)** blocks non-subscribers from joining.
* Single-use invite links prevent link sharing — each invite is unique and expires after use.
* The analyst doesn't have to manually vet members or check payments.

> Secure, automated access with no invite link leaks.

### 3. **DAO & Governance Communities**

**Example:** A DAO wants only active subscribers to participate in governance discussions on Telegram.

* The subscription acts as a membership credential — verifiable on-chain.
* Members subscribe and link their wallet; the bot handles access.
* If a member lets their subscription lapse, they lose access until they renew.

> Subscription-based membership for decentralized organizations.

### 4. **Education & Course Access**

**Example:** An educator offers paid courses and live sessions via Telegram.

* Plans are priced in SUBS or USD-denominated (settled in SUBS).
* Members can pay with SUBS or USDC directly through the integration.
* No KYC, credit card, or regional lockouts.

> Borderless. Transparent. Permissionless.

### 5. **Multi-Tier Memberships**

**Example:** A community offers two access levels:

* Basic ($10/month) — General discussion group
* Premium ($30/month) — Signals and direct support group

Each tier maps to a different Telegram group. Subscrypts allows:

* Multiple plans linked to different groups
* Users to upgrade or switch tiers by subscribing to a different plan
* Automated membership enforcement across all groups

> Supports structured growth and scalable community management.

---

## Cross-Platform: One Subscription, Multiple Platforms

A key differentiator of the Subscrypts ecosystem is that **subscriptions are cross-platform**. The same on-chain subscription can gate access across:

* **Discord** — via the [Subscrypts Discord Bot](https://discord.onsubscrypts.com)
* **Telegram** — via the [Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)
* **Websites and apps** — via the [Subscrypts SDK](../sdk/index.md) or direct smart contract integration
* **Any third-party service** — by reading on-chain subscription state

A subscriber who already has an active Subscrypts subscription for your Discord server automatically qualifies for your Telegram group too — one subscription, multiple platforms. The blockchain is the shared source of truth.

!!! tip "Verify Anywhere"
    All Subscrypts transactions are recorded on the Arbitrum blockchain and can be independently verified using [Arbiscan](https://arbiscan.io) or any other block explorer. Subscription status is never hidden behind proprietary systems.

---

## How to Monetize Your Telegram Group

1. **Add the Bot** — Visit [telegram.onsubscrypts.com](https://telegram.onsubscrypts.com) and follow the setup instructions.
2. **Create Subscription Plans** — Create plans on-chain at [telegram.onsubscrypts.com](https://telegram.onsubscrypts.com) with your preferred pricing and billing cycles.
3. **Map Plans to Your Group** — The bot associates your plans with your group for membership enforcement.
4. **Share the Subscribe Link** — Members can subscribe via the per-group subscription page.
5. **Let the Bot Handle the Rest** — The bot manages join gating, subscription verification, invite links, and expired member removal automatically.

!!! tip "Migrating an Existing Group?"
    If your group already has free members, use **Migration Mode** to transition gracefully. Set a grace period, discover existing members, and give them time to subscribe before enforcement begins. See the [Admin Setup Guide](admin-setup-guide.md) for details.

---

## Why It Matters

Subscrypts is building an **entirely new monetization layer** for Telegram:

* Built on **Arbitrum One** for low gas fees
* Powered by the **SUBS token** — non-custodial and designed with MiCAR alignment in mind
* Designed for **privacy, self-custody, and automation**
* Protected by **single-use invite links** that prevent sharing and freeloading

> Whether you're a creator, educator, trader, or community leader — if you use Telegram, you can monetize **without friction**.

!!! ecosystem "Subscrypts Ecosystem"
    The Telegram Bot leverages the same smart contract suite used by the [Subscrypts dApp](../dapp/introduction.md), the [Discord Bot](../discord-bot/introduction.md), and the [Subscrypts SDK](../sdk/index.md). Subscription plans created through any interface are interoperable across the ecosystem.

---

## Related Topics

- [Architecture & Integration](architecture.md) -- How the bot connects to Telegram and the blockchain
- [Admin Setup Guide](admin-setup-guide.md) -- Step-by-step configuration for group owners
- [Member Guide](member-guide.md) -- The subscriber experience from wallet linking to access
- [Smart Contract Suite](../smart-contract/introduction.md) -- On-chain subscription logic and plan creation
- [Subscrypts dApp](../dapp/introduction.md) -- The general-purpose web interface for managing subscriptions
- [Discord Bot Solution & Use Cases](../discord-bot/solution-and-usecases.md) -- Looking to gate Discord servers instead?
