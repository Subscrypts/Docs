---
title: Getting Started for Subscribers — Subscrypts Guide
description: Step-by-step guide to subscribing with Subscrypts — wallet setup, funding, subscribing, managing renewals, and troubleshooting.
tags:
  - subscriber
  - getting-started
  - wallet
  - subscriptions
  - tutorial
---

# Getting Started for Subscribers

Subscribing with Subscrypts takes about 30 seconds. No account creation, no email, no credit card — just a crypto wallet and a few clicks.

This guide walks you through everything from setting up your wallet to managing your subscriptions.

---

## What You Need

Before subscribing, you'll need three things:

| Requirement | Why | Cost |
|---|---|---|
| **A crypto wallet** (e.g., MetaMask) | Your wallet is your identity — no username/password needed | Free |
| **ETH on Arbitrum One** | Small amount needed for transaction fees (gas) | ~$0.01–$0.05 per transaction |
| **SUBS or USDC tokens** | To pay for subscriptions | Depends on the plan price |

!!! tip "New to crypto?"
    If you don't have a wallet yet, [MetaMask](https://metamask.io) is the most common starting point. Install the browser extension, create a wallet, and you're ready to go.

---

## Step 1: Set Up Your Wallet

1. Install **MetaMask** (or another Ethereum-compatible wallet like Coinbase Wallet, Brave Wallet, or Trust Wallet)
2. Create a new wallet or import an existing one
3. Make sure **Arbitrum One** is added as a network — most wallets include it by default

If Arbitrum One isn't listed, the Subscrypts dApp will prompt you to add it automatically when you connect.

!!! info "Arbitrum One Network Details"
    - **Chain ID:** 42161
    - **RPC URL:** `https://arb1.arbitrum.io/rpc`
    - **Block Explorer:** [arbiscan.io](https://arbiscan.io)

---

## Step 2: Fund Your Wallet

You need a small amount of **ETH on Arbitrum** for gas fees, plus **SUBS** or **USDC** for the actual subscription payment.

**How to get ETH on Arbitrum:**

- **From a centralized exchange (Coinbase, Binance, etc.):** Buy ETH and withdraw to your wallet address, selecting **Arbitrum** as the withdrawal network
- **Bridge from Ethereum mainnet:** Use the [Arbitrum Bridge](https://bridge.arbitrum.io) to move ETH from mainnet to Arbitrum One
- **Fiat on-ramp:** Services like MoonPay or Transak let you buy ETH directly with a card

!!! warning "Always double-check"
    1. You're sending **ETH** (not another token)
    2. The network is **Arbitrum One** (not Ethereum mainnet)
    3. The destination address is **your own wallet**

**How to get SUBS:**

- Use the **Swap** page on the [Subscrypts dApp](https://app.subscrypts.com) to convert USDC or ETH to SUBS
- Buy on a decentralized exchange (Uniswap on Arbitrum)

!!! tip "Don't have SUBS?"
    You can also pay with **USDC** directly. The smart contract will automatically swap your USDC to SUBS in a single transaction — no extra steps needed.

---

## Step 3: Subscribe

### Via the Subscrypts dApp

1. Open [app.subscrypts.com](https://app.subscrypts.com)
2. Click **Connect Wallet** and approve the connection in your wallet
3. Browse available subscription plans
4. Click **Subscribe** on the plan you want
5. Review the details and confirm the transaction in your wallet
6. Your subscription is active immediately

<!-- SCREENSHOT: dApp subscription flow — plan selection, confirm dialog, success state -->

### Via a Discord Server

If you're joining a Discord community that uses Subscrypts:

1. Look for the `#connect` channel in the server
2. Run `/subs link` to connect your wallet
3. Open the subscription link provided by the server
4. Choose a plan and confirm the transaction
5. The bot automatically grants your premium roles

For the full Discord guide, see [Getting Started for Discord Members](../discord-bot/member-guide.md).

---

## Step 4: Manage Your Subscriptions

Once subscribed, you can:

- **View active subscriptions** on the dApp dashboard
- **Toggle auto-renewal** on or off at any time
- **Cancel** by disabling renewal — your access continues until the current billing period ends
- **Switch plans** by subscribing to a different plan

Every action requires a wallet confirmation — nobody can change your subscription without your approval.

---

## How Renewals Work

- If **auto-renewal is on**, the smart contract automatically processes your next payment when it's due
- Your wallet needs enough **SUBS** (and a tiny amount of **ETH** for gas) at renewal time
- If your wallet doesn't have enough funds, the renewal fails and your subscription expires
- You can always **re-subscribe** at any time

!!! info "USDC and renewals"
    Automatic renewals currently require **SUBS** in your wallet. The USDC fallback is available for manual/initial payments, but not for auto-renewals yet. Keep some SUBS in your wallet if you enable auto-renew.

---

## How Much Does It Cost?

Subscription prices are set by each merchant. What you'll pay:

- **Subscription price:** As listed on the plan (in SUBS or the USD equivalent)
- **Gas fee:** ~$0.01–$0.05 per transaction on Arbitrum One
- **No hidden fees:** The 1% platform fee is taken from the merchant's side, not yours

---

## Stay in Control

Subscrypts is **non-custodial** — this means:

- Nobody can charge your wallet without your explicit approval
- You can cancel or stop renewals at any time
- No personal data is collected or stored
- You can verify every payment on [Arbiscan](https://arbiscan.io)

---

## Troubleshooting

| Issue | Solution |
|---|---|
| "Wallet not detected" | Make sure your wallet extension is installed, unlocked, and connected to Arbitrum One |
| "Wrong network" | Switch to **Arbitrum One** in your wallet — the dApp will prompt you |
| "Insufficient funds" | You need both ETH (for gas) and SUBS or USDC (for the subscription) on Arbitrum |
| "Transaction failed" | Check that you have enough balance and try again. Gas prices can fluctuate. |
| "Subscription not showing" | Wait a moment for the transaction to confirm, then refresh the page |
| "Discord role not applied" | The bot syncs roles periodically. Wait a moment, or run `/subs link` again in the server |

!!! tip "Use a Web3-enabled browser on mobile"
    Standard mobile browsers (Safari, Chrome) don't support wallet connections. Use **MetaMask Mobile**, **Brave Browser**, or **Trust Wallet** on mobile devices.

---

## Related Topics

- [What is Subscrypts?](what-is-subscrypts.md) — How the protocol works
- [dApp Subscriber Guide](../dapp/subscriber-guide.md) — Detailed dApp walkthrough
- [Discord Member Guide](../discord-bot/member-guide.md) — Subscribing via Discord
- [FAQ](../resources/faq.md) — Common questions answered
- [Glossary](../resources/glossary.md) — Crypto terms explained
