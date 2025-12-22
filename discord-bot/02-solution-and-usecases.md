---
title: Solution & Use Cases
description: Explore how the Subscrypts Discord Bot enables decentralized, automated community monetization through blockchain-based subscriptions.
tags:
 -  use cases
 - subscriptions
 - discord
 - automation
 - monetization
---

# Solution & Use Cases

The **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** transforms ordinary Discord servers into **token-gated, automated premium communities**. It brings subscription logic on-chain and links it to role-based access in Discord, enabling a new class of decentralized SaaS and creator monetization.

## What Problem Does It Solve?

Traditional community monetization faces several problems:

* ❌ Manual role assignment for paying users
* ❌ Centralized platforms (Patreon, Ko-fi) take large fees
* ❌ Limited access to unbanked or crypto-native users
* ❌ Risk of fraud, chargebacks, and privacy exposure

The **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** solves this through:

* ✅ **Smart contract-managed payments**
* ✅ **On-chain subscription state = live Discord role**
* ✅ **1% fee structure via SUBS token**
* ✅ **Global access with zero banking dependency**

It’s frictionless for both server owners and subscribers, with no email, no password, and no billing intermediaries.

---

## Key Use Cases

### 1. **Premium Discord Communities**

**Example:** A creator runs a Discord with free and premium channels. They want to charge $10/month for VIP access.

* They create a subscription plan using the **Create Subscription** link in the `#subscrypts-admin` channel.
* They link the plan to a role like `VIP Member` using the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** admin flows (Admin Guide or `/subs-admin map`).
* Users join the server, **link their wallet (EOA)** for that guild via `/subs link`, subscribe via the bot’s per-guild subscription page (or, alternatively, the **[Subscrypts dApp](https://app.subscrypts.com)**), and are instantly assigned that role.
* When the subscription expires, the role is automatically removed.

> Merchants don’t touch payments. Subscribers stay in control.

### 2. **SaaS & Tools Communities**

**Example:** A startup offers early access to its product for $25/month via Discord.

* The **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** assigns a `Beta Access` role only to subscribed users.
* Access is instantly revoked when payments lapse.
* The team doesn’t have to monitor or manually vet anyone.

> Serves as a **decentralized license manager** for Discord-first SaaS.

### 3. **Crypto Education Servers**

**Example:** A DeFi educator offers paid tutorials and live calls inside Discord.

* Plans are priced based in SUBS.
* Members can pay with SUBS or USDC via their personal subscribe link for that guild and get immediate access.
* No KYC, credit card, or regional lockouts.

> Borderless. Transparent. Permissionless.

### 4. **Gifting & Community Rewards**

**Example:** A server wants to run giveaways that award 30-day access to premium content.

* Admins use the `subscriptionGift()` function in the **[Subscrypts dApp](https://app.subscrypts.com)** (or other on-chain tools) to instantly grant access.
* These gifted subscriptions cannot be configured with auto-renewal.
* If the user wants to continue the subscription after the 30 days, they can subscribe and configure auto-renewal using the per-guild subscribe link exposed by the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** in the #subscribe and #no-active-subscription channels of that server by default.

> Great for **airdrops**, **community contests**, or **promotions**.

### 5. **Multi-Tiered Memberships**

**Example:** A community has three tiers:

* Bronze ($5)
* Silver ($15)
* Gold ($30)

Each tier unlocks specific roles and channels. Subscrypts allows:

* Multiple plans linked to multiple roles
* Multiple plans linked in one role (for example, Silver includes everything Bronze has and more)
* Users to **upgrade or downgrade** by switching plans
* Fully automated transitions between access levels

> Supports structured growth and scalable community management.

---

## How to Monetize Your Server

1. **Invite the Bot** from the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** setup page.
2. **Create a Plan (recommended path)** using the **Create Subscription** link in your `#subscrypts-admin` channel. This opens `https://discord.onsubscrypts.com/createSubscription?guildId={guild.id}`, creates a plan on Arbitrum for your guild, and logs the new plan details back into `#subscrypts-admin`.
    - **Alternative:** Advanced users can create plans via the **[Subscrypts dApp](https://app.subscrypts.com)** or direct smart contract interactions, then copy the plan id for mapping.
3. **Link Plan to Role** using the Admin Guide in `#subscrypts-admin` or `/subs-admin map` (and related commands) in the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)**.
4. **Promote the Plan** inside your server by pinning the connect/subscribe links and explaining the benefits of each tier.
5. Let the bot take care of **role assignment, renewals and expirations** automatically.

> For Discord-only monetization, you can stay entirely inside the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** flows. The **[Subscrypts dApp](https://app.subscrypts.com)** is available as a powerful alternative interface for cross-channel and advanced management.

---

## Why It Matters

Subscrypts is building an **entirely new monetization layer** for Discord:

* Built on **Arbitrum One** for low gas fees
* Powered by the **SUBS token** — non-custodial and designed with MiCAR alignment in mind
* Designed for **privacy, self-custody, and automation**

> Whether you’re a creator, educator, developer, or brand — if you use Discord, you can monetize **without friction**.

Next, see [Architecture & Integration](03-architecture-and-integration.md) to understand how the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** interacts with Discord and the blockchain.
