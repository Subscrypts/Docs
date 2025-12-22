---
title: Getting Started for Discord Members
description: A guide for Discord users on how to link their wallet, subscribe, and interact with the Subscrypts Discord Bot.
tags:
 -  subscribers
 - discord users
 - wallet
 - onboarding
 - premium roles
---

# Getting Started for Discord Members

If you've joined a Discord server that uses the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)**, this guide explains how to link your wallet, subscribe, and gain access to premium content.

> ✅ No username, email, or password needed  
> ✅ You retain full control over your wallet and funds  
> ✅ You only pay if you choose to subscribe  

---

## What You Need

Before you can link your wallet and subscribe, you’ll need a few basics in place. Don’t worry if you’re new to crypto — many servers explain or help with these steps.

### Access to a Subscrypts-enabled Discord server

- You need a **Discord account**.
- The server you joined must have the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** installed.
- If you’re not sure whether a server uses Subscrypts, look for channels like `#connect`, `#no-active-subscription`, `#swap`, or ask a moderator.

### An Ethereum-compatible wallet

- You need an **Ethereum-compatible wallet** that you control (non-custodial).
- Subscrypts is **tested with MetaMask**, but other EVM wallets that support Arbitrum generally work too.
- This wallet will be used to:
    - Prove it’s you (via a signed message when linking),
    - Pay for gas fees,
    - Pay for the actual subscription (which **always settles in SUBS** – see below).

> If you don’t have a wallet yet, MetaMask is a common starting point. Your server may have a guide in their help or FAQ channels.

### Arbitrum One network added to your wallet

Subscrypts runs on **Arbitrum One** (a Layer 2 network on top of Ethereum):

- Make sure your wallet has **Arbitrum One** configured.
- Many wallets can add it automatically when a dApp requests it; others let you add it manually from their network list.
- When you interact with Subscrypts, always check that your wallet is connected to **Arbitrum One**, not Ethereum mainnet or another chain.

### ETH for gas fees on Arbitrum

Every on-chain action (subscribing, renewing, sometimes updating settings) requires a small **gas fee** in ETH on Arbitrum:

- You need some **ETH on Arbitrum One** in your wallet — even though the subscription itself is settled in SUBS.
- Gas costs depend on how busy the network is, but they’re typically low on Arbitrum.
- Without ETH on Arbitrum, your subscription transaction cannot be confirmed.

Common ways to get ETH on Arbitrum:

- **Centralized exchange (CEX):**
    - Buy or convert to ETH.
    - Withdraw to your own wallet and, if possible, choose **Arbitrum** as the withdrawal network.
- **Bridge from another network:**
    - If you already have ETH on Ethereum mainnet or another L2, use a bridge to send some ETH to **Arbitrum One**.

> Always double-check:  
> 1) You’re sending **ETH**,  
> 2) The network is **Arbitrum One**,  
> 3) The address is your own `0x...` wallet.

### SUBS (and optionally USDC) to pay for the subscription

All Subscrypts subscriptions are **settled in SUBS** on-chain:

- Each plan can be priced in **SUBS** or in a **USDC-based value**, but when you actually pay, the **smart contract always charges in SUBS**.
- When you initiate a **direct payment** (initial subscribe or manual renewal), the contract:
    - First tries to take the required **SUBS** from your wallet.
    - If you don’t have enough SUBS but **do** have enough **USDC**, the Subscrypts smart contract can use a built-in **USDC fallback**:
        - It takes USDC from your wallet,
        - Performs an **atomic swap** from USDC → SUBS inside the transaction,
        - Uses the resulting SUBS to pay for the subscription.
- This **USDC fallback** is part of the protocol logic and is **not a per-guild/per-plan toggle** — it’s always available for supported flows.

However:

- **Automatic renewals currently require SUBS.**
- USDC fallback is **not** used for auto-renew yet.
- That means:
    - For **auto-renew** to succeed, your wallet must have enough **SUBS** at renewal time.
    - USDC in your wallet will **not** automatically be swapped during auto-renew; you would need to either:
        - Swap some USDC → SUBS yourself, or
        - Perform a **manual renewal** using the subscription page (where USDC fallback can be used again).

In practice, this means:

- It’s recommended to keep at least some **SUBS** in your wallet if you enable auto-renew.
- Holding **USDC** is useful as a backup for **direct/manual payments**, where the contract can swap USDC to SUBS for you in one transaction.

You can acquire SUBS and/or USDC on **Arbitrum One** via:

- A **swap channel** in the server (often `#swap`), which may link to a simple **swap page** provided by the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)**.
- A decentralized exchange (DEX) like **Uniswap** on Arbitrum, swapping ETH or another token to SUBS and/or USDC.

> If you’re unsure how much SUBS you need, open the server’s **Subscribe** link first — it will show the exact amount and pricing basis for each plan (and you can decide whether to hold extra SUBS for auto-renew).

---

## Join a Subscrypts-Enabled Server

After joining a server that uses Subscrypts, look for the **web3/account** category or a channel named something like:

```text
#connect
```

This is usually where your subscription journey begins. The server owner might also:

* Pin a message with “Connect your wallet” instructions, or
* Point you to the correct channel in `#welcome`, `#rules`, or `#no-active-subscription`.

If you’re unsure, ask a moderator which channel to use for **Subscrypts**.

---

## Link Your Wallet

Inside `#connect` (or another channel where the bot is available), run:

```text
/subs link
```

The **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** will:

1. Open a **private thread** with you inside that server.
2. Generate a **secure wallet-linking URL** specifically for your Discord account and that guild.
3. Ask you to open that link in your browser.

On the link page:

* You’ll see a **Subscrypts wallet connect** screen for that specific server.
* You connect your wallet and **sign a message** to prove you control it.
* **No funds are moved** — it’s a gasless signature for authentication.

Once linked:

* Your wallet is connected to your **Discord user** for that **one server** (each server is separate).
* The bot checks for any **active subscriptions** for your wallet in that guild.
* If you already have an active plan, you should receive the appropriate **premium role(s)** and see the gated channels appear.

> You can repeat `/subs link` on other servers that use Subscrypts. Each server can be linked to the **same wallet** or to **different wallets**, depending on how you prefer to manage your subscriptions.

---

## Subscribe to a Plan

If you’re not yet subscribed, you’ll need to pick a plan for that server. Each community decides which plans they offer and how they present them, but in practice you’ll usually follow a link provided by the server or the bot.

There are two common ways to reach the subscription page.

### Option A: Use links provided by the server (recommended)

Most communities will surface their subscription links in one or more of these places:

* A pinned message in channels like `#connect`, `#no-active-subscription`, `#subscribe`, or `#announcements`.
* A message or embed posted by the **Subscrypts Discord Bot** when you link your wallet or when the server announces new plans.
* A link shared by moderators or admins (for example in welcome messages or FAQs).

When you click a **Subscribe** / **View plans** link for that server:

> 🔒 **Security tip:**  
> Only trust subscription links that start with  
> `https://discord.onsubscrypts.com/s/...`  
> These URLs are generated by the official **Subscrypts Discord Bot** backend for that guild. Their content is protected and cannot be altered by server admins or third parties. If a link points to a different domain and claims to be a Subscrypts subscribe page, treat it with caution and verify with a moderator.

Once you open a trusted link:

1. Your browser loads a **per-guild subscription page** hosted by the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)**.
2. You connect the same wallet you linked in Discord (on **Arbitrum One**).
3. You review the available plans, their prices and durations.
4. You choose a plan and confirm the transaction in your wallet.

After the transaction is confirmed on-chain:

* The bot detects your new active subscription for that guild.
* Your premium role(s) in Discord are granted automatically.
* You gain access to any channels that are gated by those roles.

> If you don’t immediately see your premium channels, wait a moment and then check again. If needed, you can re-run `/subs link` to reopen your private thread and confirm everything looks correct.

### Option B: Subscrypts dApp (advanced / alternative)

Advanced users can also subscribe using the **[Subscrypts dApp](https://app.subscrypts.com)**:

* Open the dApp and navigate to the subscription or **My Subscriptions** area.
* Use the plan link or ID shared by the server to ensure you choose the **correct plan** for that Discord community.
* Subscribe from the dApp interface with your wallet on **Arbitrum One**.

As long as you subscribe to the **right plan** for that guild, the Discord bot will still recognize your on-chain subscription and grant your roles automatically.

> In most cases, using the **Subscribe links provided by the server** (that start with `https://discord.onsubscrypts.com/s/...`) is the easiest and most user-friendly path.

---

## Manage Your Subscription

Managing your access with Subscrypts has two sides:

1. **Inside Discord** – you manage which wallet is linked to your account for this server.
2. **On the web** – you manage the actual subscription (which plan, auto-renew, upgrades, etc.).

### Manage your link inside Discord

These `/subs` commands work per server (guild) — they only affect the server where you run them:

| Command          | What it does                                                                 |
| ---------------- | ----------------------------------------------------------------------------- |
| `/subs link`     | Opens a private thread and sends you a secure wallet-link URL for this server |
| `/subs unlink`   | Unlinks **one** of your wallets from this server and removes its private thread |
| `/subs my-links` | Shows all wallets you currently have linked in this server (with thread info) |
| `/subs ping`     | Simple health check to see if the bot is online and responding               |

**Notes:**

- `/subs link` is used both **the first time** you connect a wallet and later if you want to **re-check** or **re-link**.
- `/subs unlink` removes the connection between your Discord account and one wallet **for this guild only**.  
  It does **not** cancel or refund any on-chain subscription by itself — it just stops the bot from using that wallet for role decisions in this server.
- `/subs my-links` is useful if you’ve linked multiple wallets over time and want to see which ones are still active for this server.

If you change your mind about which wallet you want to use:

1. Run `/subs unlink` to remove the old wallet.
2. Run `/subs link` again and connect the new wallet.
3. If that new wallet already has an active subscription for this guild, your premium roles will be granted automatically.

### Manage your plan and renewals on the web

On the web side, the **per-guild subscription page** (the links that start with `https://discord.onsubscrypts.com/s/...`) and/or the **[Subscrypts dApp](https://app.subscrypts.com)** allow you to:

- Enable or disable **auto-renew** (if supported for that plan).
- Switch between tiers (for example, from Lite to Ultra).
- View your current and past subscriptions.
- See which guild or service a given subscription belongs to.

Remember:

> Each **Discord server** is separate. Cancelling or changing a subscription for one guild does **not** affect subscriptions in other guilds that also use Subscrypts.

---

## What Happens When a Subscription Ends?

When your subscription expires, is cancelled and reaches end-of-term, or a renewal payment fails:

* The relevant **premium role(s)** are automatically removed by the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)**.
* You will lose access to any channels that are gated behind those roles (for example, `#premium-lite`, `#premium-ultra`, or other custom premium channels).
* You can **resubscribe at any time** using the same flows as before.

You are **not** charged again unless:

* You explicitly enable **auto-renew** for a plan, and
* Your wallet has enough balance (SUBS and a small amount of ETH for gas on Arbitrum One) when renewal is due.

Subscrypts is **non-custodial**:

* No one else can spend from your wallet.
* All payments are on-chain, transparent, and require explicit approval from your wallet when you set up or change a subscription.

---

## Troubleshooting

| Issue                                       | Possible Cause / Solution                                                                                                                                               |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Role not applied after payment              | Wait a short while — the bot needs to see the on-chain transaction. If nothing changes, confirm you paid from the **same wallet** you linked for this server. If it still doesn’t work, contact a moderator. |
| No private thread opened after `/subs link` | Make sure you can see the channel where you ran the command and that you haven’t blocked the bot. If you still don’t see a new private thread, ask a moderator to check channel and thread permissions.       |
| Forgot which wallet is linked               | Run `/subs my-links` to see the wallets currently linked in this server (and their associated private threads).                                                         |
| Want to switch wallets                      | Run `/subs unlink` to remove the old wallet for this server, then run `/subs link` again and connect your new wallet.                                                   |
| I see “no active subscription” messages     | This usually means your subscription has ended, renewal failed, or the plan you bought isn’t mapped to roles in this guild. Double-check the plan link and try subscribing again, or ask a moderator.        |
| Unsure if the bot is online                 | Run `/subs ping`. If the bot responds, it’s online. If not, let a moderator or admin know.                                                                              |

If you continue to have issues, contact a server moderator or use the server’s support channel (for example, `#support` or a dedicated help desk channel).

---

## Stay In Control

* You are never charged without you **setting up and confirming** the subscription from your own wallet.
* You can **unlink** a wallet at any time with `/subs unlink` (per server).
* You can **stop renewing**, switch plans, or let a subscription expire naturally.
* You can see your subscription history and active plans via the Subscrypts web interfaces (per-guild pages at `https://discord.onsubscrypts.com/...` and the **[Subscrypts dApp](https://app.subscrypts.com)**).

For technical and privacy transparency, see the **[Subscrypts MiCAR Whitepaper](https://subscrypts.com/whitepaper)**.

---

Next: **[Commands Reference](06-commands-reference.md)** – see a full list of what you can do with the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** as a member and as an admin.
