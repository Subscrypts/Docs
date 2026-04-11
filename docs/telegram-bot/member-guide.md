---
title: Telegram Bot Member Guide
description: A guide for Telegram users on how to link their wallet, subscribe, and gain access to gated groups via the Subscrypts Telegram Bot.
status: new
tags:
  - subscrypts
  - telegram
  - subscribers
  - telegram users
  - wallet
  - onboarding
---

# Getting Started for Telegram Members

If you want to join a Telegram group that uses the **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)**, this guide explains how to subscribe, link your wallet, and gain access.

!!! success "Quick Overview"
    No username, email, or password needed -- You retain full control over your wallet and funds -- You only pay if you choose to subscribe

---

## What You Need

Before you can subscribe and join a gated group, you'll need a few basics in place. Don't worry if you're new to crypto — the process is straightforward.

### A Telegram account

- You need a **Telegram account** (the app is available on iOS, Android, and desktop).
- The group you want to join must have the **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)** installed by its owner.

### An Ethereum-compatible wallet

- You need an **Ethereum-compatible wallet** that you control (non-custodial).
- Subscrypts is **tested with MetaMask**, but other EVM wallets that support Arbitrum generally work too.
- This wallet will be used to:
    - Prove it's you (via a signed message when linking — gasless, no fees),
    - Pay for gas fees (a tiny amount of ETH on Arbitrum),
    - Pay for the actual subscription (settled in SUBS tokens).

!!! tip "New to Wallets?"
    If you don't have a wallet yet, MetaMask is a common starting point. Many communities provide guides in their help channels.

### Arbitrum One network added to your wallet

Subscrypts runs on **Arbitrum One** (a Layer 2 network on top of Ethereum):

- Make sure your wallet has **Arbitrum One** configured.
- When you interact with Subscrypts, always check that your wallet is connected to **Arbitrum One**, not Ethereum mainnet or another chain.

### ETH for gas fees on Arbitrum

Every on-chain action (subscribing, renewing) requires a small **gas fee** in ETH on Arbitrum:

- You need some **ETH on Arbitrum One** in your wallet.
- Gas costs are typically very low on Arbitrum (fractions of a cent).

### SUBS (and optionally USDC) to pay for the subscription

All Subscrypts subscriptions are **settled in SUBS** on-chain:

- Each plan can be priced in **SUBS** or in a **USD-based value**, but the smart contract always settles in SUBS.
- If you don't have enough SUBS but **do** have enough **USDC**, the integration offers a **USDC fallback**:
    - It takes USDC from your wallet,
    - Performs an **atomic swap** from USDC to SUBS via Uniswap V3 in the same transaction,
    - Uses the resulting SUBS to pay for the subscription.
- **Automatic renewals require SUBS.** USDC fallback is available for initial and manual payments, but auto-renew needs sufficient SUBS balance at renewal time.

---

## How to Join a Gated Group

### Step 1: Open the Subscribe Link

Each gated Telegram group has a **subscribe link** — a URL that opens the subscription page for that specific group. You'll typically find this link:

* In the group's description or pinned messages
* Shared by the group owner or moderators
* Posted on the community's website or social media

The link opens a page at `telegram.onsubscrypts.com` showing the available plans for that group.

### Step 2: Connect Your Wallet and Subscribe

On the subscription page:

1. Connect your wallet on **Arbitrum One**.
2. Review the available plans (pricing, billing cycles, descriptions).
3. Select a plan and choose your preferred billing cycle.
4. Confirm the on-chain transaction in your wallet.

After the transaction is confirmed on the blockchain, your subscription is active.

!!! tip "USDC Fallback"
    If you don't have enough SUBS tokens, the page will offer to swap your USDC to SUBS automatically as part of the same transaction. You don't need to swap tokens manually first.

### Step 3: Link Your Wallet

After subscribing, you need to **link your wallet** to your Telegram account for this group. This step proves that you own the wallet that holds the subscription.

1. The subscription page provides a **Link Wallet** button, or the bot sends you a wallet-link URL via Telegram DM.
2. Open the link in your browser.
3. Connect the **same wallet** you used to subscribe.
4. **Sign a message** to prove you control the wallet.
    - This is a **SIWE (Sign-In with Ethereum)** signature.
    - It is **gasless** — no transaction fees, no funds moved.
    - Your private keys **never leave your wallet**.

### Step 4: Receive Your Invite Link

Once your wallet is linked and your subscription is verified:

1. The bot sends you a **single-use invite link** via Telegram DM.
2. Click the link to join the group.
3. The invite link is valid for a limited time and **cannot be shared** — it works only once.

You now have access to the gated group for the duration of your subscription.

---

## Managing Your Subscription

### Check Your Status

In a private chat with the bot, run:

```text
/status
```

This shows your subscription status across all groups you're linked to.

### What Happens When Your Subscription Expires

When your subscription expires or a renewal payment fails:

* The bot **automatically removes** you from the group during the next reconciliation cycle.
* You receive a **DM from the bot** with a link to resubscribe.
* Your wallet remains linked — you do not need to re-link if you resubscribe.
* Once you renew, you receive a **new invite link** and can rejoin immediately.

### Switching Wallets

If you want to use a different wallet:

1. Contact a group admin to unlink your current wallet (or let the old link expire).
2. Subscribe from your new wallet.
3. Link the new wallet using the wallet-link flow.

### Cancelling

To stop your subscription:

* Simply **let it expire** — do not enable auto-renew, or disable it via the [Subscrypts dApp](https://app.subscrypts.com).
* Once expired, you will lose group access.
* You are **never charged** without your explicit approval via your wallet.

---

## Stay In Control

* You are never charged without you **setting up and confirming** the subscription from your own wallet.
* You can **let a subscription expire** at any time — no lock-in, no cancellation fees.
* You can see your subscription history and status via the [Subscrypts dApp](https://app.subscrypts.com) or [Subscrypts Pulse](https://pulse.subscrypts.com).
* All transactions are on-chain and verifiable via [Arbiscan](https://arbiscan.io) or other block explorers.

Subscrypts is **non-custodial**:

* No one else can spend from your wallet.
* All payments are on-chain, transparent, and require explicit approval from your wallet.
* The bot never handles your private keys.

!!! ecosystem "Subscrypts Ecosystem"
    Subscriptions are managed by the [Smart Contract Suite](../smart-contract/introduction.md) on Arbitrum. The Telegram Bot, the [Discord Bot](../discord-bot/introduction.md), and the [Subscrypts dApp](../dapp/introduction.md) are all interfaces to the same on-chain logic — your subscription works across all of them.

---

## Troubleshooting

| Issue | Possible Cause / Solution |
|-------|--------------------------|
| No invite link received after linking | Wait a moment — the bot needs to verify your on-chain subscription. Ensure you subscribed from the **same wallet** you linked. |
| Invite link expired or doesn't work | Request a new link by re-completing the wallet-link flow. Single-use links expire after a short time. |
| Removed from group unexpectedly | Your subscription may have expired. Check your status with `/status` in a DM to the bot. Resubscribe to rejoin. |
| Can't connect wallet on the link page | Ensure your wallet is set to **Arbitrum One**. Try a different browser or clear your browser cache. |
| USDC swap failed | Ensure you have enough USDC to cover the subscription amount plus a small buffer for slippage. |

If you continue to have issues, contact the group's administrator or moderator.

---

## Related Topics

- [Commands Reference](commands-reference.md) -- Bot commands for members and admins
- [Admin Setup Guide](admin-setup-guide.md) -- How group owners configure access
- [Security & Trust](security-and-trust.md) -- Privacy model and wallet linking security
- [Best Practices](best-practices.md) -- Tips for both admins and members
- [Smart Contract Suite](../smart-contract/introduction.md) -- How subscriptions work on-chain
- [Subscrypts Pulse](../pulse/introduction.md) -- Monitor your subscriptions and receive expiry notifications
