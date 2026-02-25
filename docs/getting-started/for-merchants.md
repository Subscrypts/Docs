---
title: Getting Started for Merchants — Accept Crypto Subscriptions
description: Set up recurring crypto payments with Subscrypts — 1% fee, instant settlement, Discord integration, and MiCAR compliance.
tags:
  - merchant
  - getting-started
  - monetization
  - payments
  - discord
  - subscrypts
---

# Getting Started for Merchants

Accept recurring crypto payments, keep 99% of every payment, and reach subscribers globally — no banks, no chargebacks, no personal data collection required.

---

## Why Subscrypts?

| | Subscrypts | Stripe | Patreon | PayPal |
|---|---|---|---|---|
| **Fee per payment** | 1% | 2.9% + $0.30 | 5–12% | 2.9% + $0.30 |
| **Settlement** | Instant (on-chain) | 2–7 business days | Monthly | 1–3 business days |
| **Chargebacks** | Not possible | Common | Rare | Common |
| **Personal data collected** | None | Name, email, card | Name, email, card | Name, email, card |
| **Global availability** | Anyone with a wallet | Bank account required | Bank account required | Bank account required |
| **Compliance** | MiCAR-aligned (EU) | PCI-DSS | PCI-DSS | PCI-DSS |

---

## Two Ways to Get Started

### Path A: Monetize a Discord Community

Best for: community creators, educators, gaming servers, content creators.

1. **Add the bot** — Visit [discord.onsubscrypts.com](https://discord.onsubscrypts.com) and add the Subscrypts Discord Bot to your server
2. **Run initial setup** — In `#subscrypts-admin`, click **Apply Baseline** to create required roles and channels
3. **Create a subscription plan** — Click **Create Subscription** in the admin guide (the bot pre-fills your guild ID)
4. **Map plan to roles** — Click **Map Plan to Role** to connect your plan to a premium Discord role
5. **You're live** — Members can now link their wallets and subscribe. The bot grants/revokes roles automatically.

For the full walkthrough, see the [Discord Bot Admin Setup Guide](../discord-bot/admin-setup-guide.md).

### Path B: Use the dApp for Any Service

Best for: SaaS platforms, content sites, streaming services, API billing.

1. **Connect your wallet** at [app.subscrypts.com](https://app.subscrypts.com)
2. **Create a subscription plan** — Set the price, billing frequency, and currency (SUBS or USD-denominated)
3. **Share the plan link** — Subscribers can browse and subscribe directly on the dApp
4. **Monitor revenue** — Track subscribers and payments from your merchant dashboard

For details, see the [dApp Merchant Guide](../dapp/merchant-guide.md).

---

## How Revenue Works

When a subscriber pays, the smart contract:

1. **Burns** the payment amount (in SUBS) from the subscriber's wallet
2. **Mints** 99% to your merchant wallet (instant — same transaction)
3. **Mints** 1% to the protocol treasury

```
Example: $10/month plan (≈ 500 SUBS)
├── Subscriber pays:   500 SUBS
├── You receive:       495 SUBS (99%)
└── Protocol treasury:   5 SUBS (1%)
```

- Payments are **instant** — funds arrive in the same transaction
- Payments are **non-custodial** — the protocol never holds your funds
- All transactions are **verifiable** on [Arbiscan](https://arbiscan.io)

---

## Pricing Your Plans

You have two pricing options:

| Option | How It Works | Best For |
|---|---|---|
| **SUBS-denominated** | Fixed SUBS amount per billing cycle (e.g., 500 SUBS/month) | Crypto-native audiences |
| **USD-denominated** | Fixed dollar amount; contract calculates equivalent SUBS at payment time via Uniswap V3 mid-price oracle | Stable, predictable pricing |

!!! tip "Recommend USD-denominated plans for predictable revenue"
    With USD-denominated plans, your subscribers always pay the equivalent of (e.g.) $10, regardless of SUBS price fluctuations. The smart contract handles the conversion automatically.

---

## What You'll Need

| Requirement | Details |
|---|---|
| **Ethereum wallet** | MetaMask recommended. This wallet receives your revenue and owns your plans. |
| **ETH on Arbitrum** | Tiny amount for gas fees (~$0.01 to create a plan) |
| **Arbitrum One network** | All Subscrypts operations run on Arbitrum One (Chain ID 42161) |

---

## Merchant Quickstart Checklist

- [ ] Install MetaMask (or compatible wallet)
- [ ] Add Arbitrum One network to your wallet
- [ ] Fund wallet with a small amount of ETH for gas
- [ ] Choose your path: Discord Bot or dApp
- [ ] Create your first subscription plan
- [ ] Share the plan link with your audience
- [ ] (Discord only) Map your plan to premium roles

---

## Accepting USDC Payments

Your subscribers don't need to hold SUBS to subscribe. If they have **USDC**, the smart contract:

1. Pulls USDC from their wallet via **Permit2** (gasless approval)
2. Swaps USDC to SUBS on **Uniswap V3** in the same transaction
3. Completes the subscription payment using the SUBS received

The subscriber pays the equivalent amount in USDC; you receive SUBS. All in one atomic transaction.

---

## Off-Ramping Revenue

The SUBS you earn can be:

- **Swapped to USDC** via the dApp's built-in swap page or any Uniswap interface on Arbitrum
- **Bridged to Ethereum mainnet** and then to a centralized exchange for fiat withdrawal
- **Held as SUBS** for use within the ecosystem

---

## Compliance Considerations

Subscrypts is designed with regulatory compliance in mind:

- The platform's [whitepaper](https://subscrypts.com/whitepaper) is aligned with the **EU MiCAR regulation**
- The SUBS token is classified as a **utility token** — not a security, e-money token, or asset-referenced token
- The protocol does **not** collect or store personal data
- Merchants may still have independent obligations to comply with local regulations (KYC/AML, tax reporting) depending on their jurisdiction

For full compliance details, see [Compliance](../subscrypts/compliance.md).

---

## Related Topics

- [Discord Bot Admin Setup Guide](../discord-bot/admin-setup-guide.md) — Full Discord monetization walkthrough
- [dApp Merchant Guide](../dapp/merchant-guide.md) — Detailed dApp merchant features
- [Tokenomics](../subscrypts/tokenomics.md) — SUBS token supply and distribution
- [Smart Contract Core Logic](../smart-contract/core-logic.md) — How payments work under the hood
- [FAQ](../resources/faq.md) — Common merchant questions
- [vs Traditional Payments](../resources/vs-traditional-payments.md) — Detailed comparison with Stripe, Patreon, PayPal
