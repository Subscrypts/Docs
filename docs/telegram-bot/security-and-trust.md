---
title: Telegram Bot Security & Trust
description: How the Subscrypts Telegram Bot ensures user privacy, secure wallet linking via SIWE, and non-custodial subscription access.
status: new
tags:
  - subscrypts
  - telegram
  - security
  - privacy
  - SIWE
  - wallet linking
  - trust
---

# Security & Trust

The **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)** is designed to be:

* **Non-custodial** -- you keep control of your wallet and funds
* **Privacy-respecting** -- minimal data, no passwords or emails
* **On-chain transparent** -- all payments and subscriptions are visible on Arbitrum
* **Globally accessible** -- no reliance on banks or card processors

This page explains what that means in practice for **Telegram members**, **merchants (group owners)**, and the **wider Subscrypts ecosystem**.

---

## Design Principles

Across the dApp, smart contracts, Discord Bot, and Telegram Bot, Subscrypts follows core principles:

1. **Wallets, not accounts**
   Identity is based on **wallet ownership**, proven by SIWE signatures — not usernames, email addresses, or passwords.

2. **On-chain = source of truth**
   Subscription state lives in the **Subscrypts smart contract suite on Arbitrum One**. The integration **reads** this state; it does not "override" it.

3. **Non-custodial funds**
   Users approve each subscription transaction from their own wallet. Subscrypts cannot move funds on their behalf.

4. **Minimal off-chain data**
   Only what is strictly needed for the system to function (e.g., "wallet X has a subscription for plan Y in group Z") is stored off-chain.

5. **Transparent & MiCAR-aligned**
   Token and subscription mechanics are documented in the **[Subscrypts MiCAR Whitepaper](https://subscrypts.com/whitepaper)**, making it easier for EU-based merchants to understand their responsibilities.

---

## Wallet Linking & Identity Mapping

When a subscriber links their wallet:

1. The integration generates a **signed JWT** containing the group ID, user ID, a single-use nonce (JTI), and a short expiry.
2. The subscriber opens the wallet-link URL at [telegram.onsubscrypts.com](https://telegram.onsubscrypts.com) and connects their wallet.
3. The subscriber **signs a SIWE (Sign-In with Ethereum) message** to prove they control the wallet.
4. The integration verifies the signature and JWT, then stores the wallet-to-user link, scoped to that specific group.

Key security properties:

* **JWT tokens are single-use** — Each token includes a JTI (JWT ID) that is tracked and invalidated after use. Replaying a token is blocked.
* **Time-limited** — Tokens expire after a short window, reducing the risk of stale links.
* **Group-scoped** — A token for Group A cannot be used to link a wallet in Group B.
* **SIWE standard** — Uses EIP-4361 for wallet verification, with domain and chain binding to prevent cross-site or cross-chain replay.
* **Cryptographically signed** — All internal communication is cryptographically signed, preventing tampering.
* **No private keys exposed** — Users sign a message, not a transaction. Private keys never leave the wallet.

---

## Single-Use Invite Links

After verifying a subscription, the bot sends a **single-use invite link** via Telegram DM:

* Each link is valid for **one use only** — once clicked, it cannot be shared or reused.
* Links have a **short expiry window**.
* The bot tracks link usage and cleans up expired links automatically.

This design prevents the most common attack on gated Telegram groups: **invite link sharing**. Even if a subscriber shares their link, it will only work once.

---

## Data Minimization & Privacy

The Subscrypts Telegram Bot operates with **as little personal data as possible**.

Data that **is** stored:

* Telegram identifiers (group ID, user ID)
* Public wallet addresses
* Plan IDs and group-to-plan mappings
* Membership action logs (user, action, timestamp — auto-pruned after 90 days)

Data that is **not** collected:

* Real names, addresses, or emails
* Passwords or seed phrases
* Credit card or bank details
* Chat messages or media (the bot runs in privacy mode)

This approach:

* Reduces the impact of any data breach (there is no trove of personal info to steal).
* Aligns with **data minimization** principles in MiCAR/GDPR-style frameworks.
* Keeps the focus on **public blockchain data**, which is already openly verifiable.

!!! info "Privacy Mode"
    The Subscrypts Telegram Bot runs in **privacy mode**, meaning it only receives messages that are commands directed to it. It does not read or store general group chat messages.

---

## On-Chain Transparency & Non-Custodial Funds

All payment and subscription actions are executed through the **Subscrypts smart contract suite** on **Arbitrum One**:

* Subscription billing is **always settled in SUBS**.
* If subscribers have **USDC** instead of SUBS, the integration handles an **atomic swap** via Uniswap V3 in the same transaction.
* **Automatic renewal** requires the subscriber to hold enough SUBS at renewal time.

Because everything happens on-chain:

* Users can inspect their subscription history using [Arbiscan](https://arbiscan.io) or any block explorer.
* Merchants can audit incoming payments to their **own wallet address**.
* There is no hidden off-ledger accounting.

Crucially:

* **Subscrypts never holds your funds**.
* The bot **cannot transfer** tokens — it only **observes** contract state and manages group membership.
* All subscriptions require **explicit confirmation** from the user's wallet.

---

## Internal Security

All internal communication within the integration is protected by **HMAC-SHA256 cryptographic signatures**, preventing unauthorized third parties from triggering wallet links, plan notifications, or membership changes.

Additional security measures:

* **CSRF protection** — All form submissions are protected with CSRF tokens.
* **Rate limiting** — API endpoints are rate-limited to prevent abuse.
* **CORS enforcement** — Strict origin checking prevents cross-site request forgery.
* **Session security** — Cookie-based sessions use `httpOnly`, `secure`, and `sameSite` flags.

---

## What This Means for Merchants

For Telegram group owners, the security model delivers:

* **Lower compliance surface** — you do not process card data or store user PII; you receive on-chain SUBS payments into your own wallet.
* **Clear separation of concerns** — the smart contracts handle billing, the bot handles access control, Telegram handles community features.
* **Cross-border reach** — anyone with a wallet and internet access can subscribe, regardless of local banking infrastructure.
* **Protection against invite link sharing** — single-use links prevent unauthorized access distribution.

You remain responsible for:

* Communicating your offering and terms clearly.
* Following any local regulations that apply to your business.

---

## What This Means for Subscribers

For members, this model ensures:

* **Self-custody** — you keep your keys, you approve each transaction.
* **Privacy** — your Telegram identity is linked to a wallet address, not to real-world identity data.
* **Portability** — you can move funds between wallets and chains outside of Subscrypts' control.
* **Borderless access** — as long as you can use a wallet on Arbitrum, you can subscribe, even without a bank account or credit card.

If you no longer want access:

* You can **let your subscription expire**.
* Your funds remain in your wallet; the bot cannot touch them.

!!! ecosystem "Subscrypts Ecosystem"
    The security model described here is shared across the [Smart Contract Suite](../smart-contract/introduction.md), the [Subscrypts dApp](../dapp/introduction.md), the [Discord Bot](../discord-bot/introduction.md), and the Telegram Bot. All interfaces read from the same on-chain source of truth without custodial risk.

---

## Summary

| Aspect | How it's handled |
|--------|-----------------|
| Identity | SIWE wallet signatures + Telegram IDs (no passwords/emails) |
| Funds | Non-custodial, on-chain payments in SUBS (with USDC fallback) |
| Source of truth | Subscrypts smart contracts on Arbitrum One |
| Invite links | Single-use, time-limited, per-user |
| Internal security | HMAC-SHA256 signed communication |
| Permissions | Controlled by Telegram group admin settings |
| Personal data | Minimal; no sensitive PII stored; privacy mode active |
| Global accessibility | Works cross-border, suitable for crypto-native and unbanked users |

---

## Related Topics

- [Architecture & Integration](architecture.md) -- How the integration works end to end
- [Subscription Synchronization](subscription-sync.md) -- How on-chain state becomes Telegram group membership
- [Best Practices](best-practices.md) -- Tips to keep your group safe and reliable
- [Admin Setup Guide](admin-setup-guide.md) -- Group configuration and permission setup
- [Smart Contract Suite](../smart-contract/introduction.md) -- On-chain subscription logic and security guarantees
