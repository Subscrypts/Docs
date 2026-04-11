---
title: Telegram Bot Admin Setup Guide
description: Step-by-step setup guide for Telegram group owners to monetize their community with the Subscrypts Telegram Bot.
status: new
tags:
  - subscrypts
  - telegram
  - telegram admin
  - setup
  - group owner
  - monetization
  - membership management
---

# Getting Started for Telegram Admins

This guide helps Telegram group owners set up and operate the **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)** so that group membership is controlled automatically by **on-chain subscriptions** stored in the Subscrypts smart contract suite on Arbitrum.

!!! success "Quick Overview"
    No coding required -- Works with your existing groups -- Membership auto-syncs to on-chain status

---

## Merchant Overview

From a merchant's perspective, the Subscrypts Telegram integration works like this:

1. **What Subscrypts is**
   Subscrypts is a **blockchain-based subscription system** on Arbitrum. It lets you sell recurring access (subscriptions) without custodians or payment processors — funds flow **directly from your members' wallets to your wallet**, enforced by smart contracts.

2. **What the Subscrypts Telegram Bot does**
   The **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)** connects those on-chain subscriptions to Telegram. It **grants** and **revokes** group membership automatically, based on each member's live subscription status on-chain.

3. **What you do as a group admin**
    - You are the **group owner** or a group administrator.
    - You **add the bot** to your Telegram group.
    - You run `/admin setup` to check that the bot has the required permissions.
    - You **accept the Terms of Service** when prompted.
    - You **create one or more subscription plans** at [telegram.onsubscrypts.com](https://telegram.onsubscrypts.com).
    - You **map plans to your group** so the bot knows which subscriptions grant access.
    - You make sure the **bot has admin permissions** in the group (specifically: invite users, ban users, and delete messages).

4. **What your members do**
    - They open the **subscribe link** for your group.
    - They **subscribe to a plan** on-chain using their crypto wallet.
    - They **link their wallet** via a gasless SIWE signature.
    - They receive a **single-use invite link** via Telegram DM.
    - They join the group.

5. **How payments work**
    - Every payment is a **non-custodial on-chain transaction**.
    - Subscribers pay from their own wallet; funds (minus protocol fees) go **directly to your merchant wallet** on Arbitrum.
    - No cards, no bank accounts, no manually managing members — the blockchain and the bot keep everything in sync.

Once you've completed these steps, you've effectively **monetized your Telegram group** with self-custodial, on-chain subscriptions — and the bot takes care of the day-to-day membership enforcement for you.

---

## Prerequisites

### Telegram group ownership & permissions

To add and correctly configure the **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)**, you need sufficient Telegram permissions:

- You must be the **group owner** or an **administrator** with permission to add bots and manage members.
- The bot needs **admin permissions** in the group: at minimum, the ability to **invite users**, **ban users**, and **delete messages**.

### Ethereum wallet

* You need an **Ethereum-compatible wallet** that you control.
* Subscrypts is **tested with MetaMask**, but other EVM wallets that support Arbitrum should also work.
* The wallet you use here will own your subscription plans and receive payments.

### Arbitrum network

* Your wallet must have the **Arbitrum One** network configured.
* When you interact with [telegram.onsubscrypts.com](https://telegram.onsubscrypts.com), ensure that your wallet is **connected to Arbitrum One**, not Ethereum mainnet or another network.

### ETH for gas fees

* Every on-chain action (e.g., creating a subscription plan) consumes **gas fees** paid in ETH on Arbitrum.
* Gas fees on Arbitrum are typically very low (approximately $0.01 per plan creation).

---

## Step-by-Step Setup

### Step 1: Add the Bot to Your Group

1. Visit [telegram.onsubscrypts.com](https://telegram.onsubscrypts.com) and click the **Add to Telegram** button.
2. Select the group you want to monetize.
3. Grant the bot **admin permissions** (invite users, ban users, delete messages).

### Step 2: Run Initial Setup

In your Telegram group, run:

```text
/admin setup
```

The bot performs a **diagnostic check** and reports:

* Whether it has the required admin permissions
* Whether Terms of Service have been accepted
* Whether plans are mapped to the group
* Whether the bot has been promoted to admin status

### Step 3: Accept Terms of Service

If prompted, accept the Subscrypts Terms of Service for your group. This is required before the bot can enforce membership.

### Step 4: Create Subscription Plans

Visit the plan creation page:

1. Navigate to [telegram.onsubscrypts.com](https://telegram.onsubscrypts.com) and go to the plan creation page.
2. Connect your wallet on **Arbitrum One**.
3. Configure your plan:
    - **Currency** — SUBS or USD-denominated (settled in SUBS)
    - **Amount** — The price per billing cycle
    - **Duration** — Weekly, monthly, yearly, or custom
    - **Description** — A short description visible to subscribers
    - **Referral bonus** (optional) — Incentivize referrals with bonus subscription time
4. Confirm the on-chain transaction in your wallet.
5. The bot is automatically notified and announces the new plan in your group.

### Step 5: Map Plans to Your Group

After creating a plan, the bot automatically maps it to your group. You can verify the mapping and manage plans using:

```text
/admin plan
```

This shows all plans currently mapped to your group.

### Step 6: Share the Subscribe Link

The bot provides a per-group subscribe link that you can share with potential members. This link opens the subscription page showing only your group's plans. You can find this link:

* Pinned in your group by the bot
* Via the `/admin setup` command output

Share this link in your group description, on social media, or anywhere you want to attract subscribers.

---

## Verify Your Setup

Run a diagnostic check at any time:

```text
/admin check
```

This performs a **9-point diagnostic** covering:

* Bot admin permissions
* Terms of Service acceptance
* Plan mappings
* Group configuration
* Blockchain connectivity

If something is misconfigured, the bot provides specific guidance on how to fix it.

---

## Migration Mode (for Existing Groups)

If your group already has members who joined for free, you can transition to subscription-gated access using **Migration Mode**. This gives existing members a grace period to subscribe before enforcement begins.

### Starting Migration

```text
/admin migrate <days>
```

Where `<days>` is the grace period length (1–90 days). For example:

```text
/admin migrate 14
```

This starts a 14-day grace period during which:

* The bot pins an announcement with **Subscribe** and **Link Wallet** buttons
* New members who try to join are still blocked by the join gate (only existing members get the grace window)
* Automated reminders are posted at strategic intervals

### Member Discovery

For migration to be effective, the bot needs to know who your existing members are. Two approaches:

1. **Admin export (recommended)** — Export your member list from Telegram Desktop and upload it via the bot's member export tool. This provides 100% coverage.
2. **Self-registration** — Members click a verification button in the group to register themselves. Useful for broadcast groups where the admin export may not capture all members.

### Monitoring Migration Progress

```text
/admin migrate status
```

Shows real-time progress: how many members have subscribed, how many are pending, and how much time remains.

### Adjusting the Grace Period

```text
/admin migrate adjust <days>
```

Moves the deadline forward or backward. Useful if members need more time.

### Ending Migration

```text
/admin migrate end
```

This ends the grace period and begins enforcement. **Known members without linked wallets and active subscriptions are removed.** The bot asks for confirmation before proceeding.

!!! warning "Communicate Before Enforcing"
    Make sure your members understand the transition. Post clear instructions, pin the subscribe link, and give adequate notice before ending migration. See [Best Practices](best-practices.md) for detailed migration tips.

---

## Operational Tools

### View Group Statistics

```text
/admin stats
```

Shows subscriber counts, linked wallet counts, and other group metrics.

### View Membership Audit Trail

```text
/admin ledger
```

Shows the last 20 membership actions (invites, removals, reasons) for auditing and troubleshooting.

### Force Immediate Reconciliation

```text
/admin reconcile
```

Triggers an immediate subscription verification pass for all linked members. Useful after configuration changes or to quickly sync after a batch of new subscriptions.

### Check Blockchain Connectivity

```text
/admin rpc-health
```

Shows the health status of the blockchain RPC endpoints the bot uses.

### Remove a User's Wallet Link

```text
/admin unlink <user>
```

Force-unlinks a member's wallet from your group. Useful for support cases or security enforcement.

---

## Frequently Asked Questions

**Q: Can I run multiple plans for the same group?**
Yes. You can create and map multiple plans with different prices and billing cycles to the same group. Any active subscription to any mapped plan grants membership.

**Q: Do members need to re-link after renewing?**
No. Once a wallet is linked to a group, renewals and expirations are picked up automatically by the reconciler. Members only need to re-link if they change wallets.

**Q: What happens when a member's subscription expires?**
The reconciler detects the expired subscription and removes the member from the group. The member receives a DM with a link to resubscribe. If they resubscribe, they receive a new invite link automatically.

**Q: Can I use the same plan across Discord and Telegram?**
Yes. Subscrypts subscriptions are cross-platform. A plan created for your Discord server can also be mapped to your Telegram group, and vice versa. One active subscription can grant access to both platforms.

---

## Related Topics

- [Member Guide](member-guide.md) -- See the member journey from wallet linking to group access
- [Commands Reference](commands-reference.md) -- All admin commands with syntax and descriptions
- [Subscription Synchronization](subscription-sync.md) -- How background reconciliation works
- [Security & Trust](security-and-trust.md) -- Privacy and safety overview
- [Best Practices](best-practices.md) -- Migration tips and troubleshooting
- [Smart Contract Suite](../smart-contract/introduction.md) -- On-chain subscription logic and plan creation
- [Discord Bot Admin Setup Guide](../discord-bot/admin-setup-guide.md) -- Setting up the Discord integration
