---
title: Pulse Features & Dashboard
description: Explore the Subscrypts Pulse dashboard, subscription list, balance aggregation, and filtering capabilities.
status: new
tags:
  - subscrypts
  - pulse
  - dashboard
  - features
  - subscriptions
  - monitoring
---

# Features & Dashboard

Subscrypts Pulse provides a comprehensive view of your on-chain subscriptions and balances. This page covers the main features and how to use them.

---

## Dashboard

The dashboard is your home screen — a high-level overview of your subscription health across all monitored wallets.

### Balance Overview

At the top of the dashboard, Pulse displays your **aggregated token balances**:

* **SUBS balance** — Total SUBS tokens across all monitored wallets
* **USDC balance** — Total USDC across all monitored wallets

These balances update automatically and help you assess whether you have enough tokens for upcoming subscription payments.

### Quick Stats

Four key metrics give you an instant health check:

| Stat | What It Shows |
|------|--------------|
| **Active** | Number of subscriptions currently active across all wallets |
| **Expiring Soon** | Subscriptions approaching their next payment date |
| **Expired** | Subscriptions that have lapsed |
| **Wallets** | Number of wallet addresses you're monitoring |

### Upcoming Payments

The dashboard displays the next upcoming subscription payments, showing:

* Plan name and description
* Payment amount and currency
* Next payment date
* Days remaining until payment

This helps you plan ahead — if a payment is approaching and your balance is low, you have time to top up.

### System Health

A status indicator shows whether Pulse's backend services are operating normally:

* **Green** — All systems healthy (backend, database, blockchain connection)
* **Yellow** — Partial issues (degraded performance)
* **Red** — Service disruption

### Pull-to-Refresh

On mobile, pull down on the dashboard to refresh all data immediately. On desktop, data refreshes automatically at regular intervals.

---

## Subscription List

The subscription screen shows all subscriptions across your monitored wallets, with filtering and detail views.

### Filtering

Three filter tabs let you focus on what matters:

* **All** — Every subscription, regardless of status
* **Active** — Only subscriptions with active on-chain status
* **Expired** — Subscriptions that have lapsed or been stopped

Each tab shows a count badge so you can see the distribution at a glance.

### Subscription Cards

Each subscription is displayed as a card showing:

* **Plan ID** — The on-chain identifier
* **Payment amount** — How much is charged per cycle, in SUBS or USDC equivalent
* **Payment frequency** — How often payments occur (weekly, monthly, yearly, etc.)
* **Next payment date** — When the next charge is due
* **Status badge** — Color-coded indicator:
    * Green = active and healthy
    * Yellow = expiring soon
    * Red = expired or stopped

### Subscription Detail

Tap any subscription card to see the full detail view:

* **Plan information** — Description, amount, frequency, auto-renew status
* **Payment status** — Next payment date, days remaining, cycles paid vs. missed
* **Blockchain addresses** — Merchant and subscriber wallet addresses, each linking to [Arbiscan](https://arbiscan.io) for independent verification
* **Manage link** — A link to the [Subscrypts dApp](https://app.subscrypts.com) where you can manage the subscription (renew, stop, toggle auto-renew)

!!! tip "Verify On-Chain"
    Every subscription displayed in Pulse can be independently verified on the blockchain. Tap the merchant or subscriber address to view the transaction history on Arbiscan.

---

## Multi-Wallet Support

Pulse supports monitoring **up to 20 wallet addresses** simultaneously. All data — balances, subscriptions, and notifications — is aggregated across your wallets.

Use cases for multi-wallet monitoring:

* **Personal + business wallets** — Track subscriptions across different wallets without switching
* **Hardware + hot wallet** — Monitor your hardware wallet subscriptions alongside your hot wallet
* **Family or team monitoring** — Keep an eye on subscriptions across multiple wallets

Each wallet can be given an optional **label** (e.g., "Main Wallet", "Cold Storage") for easy identification in the dashboard.

See [Wallet Management](wallet-management.md) for details on adding and removing wallets.

---

## Notifications Overview

Pulse sends push notifications for six event types, keeping you informed about important subscription changes without needing to check the app manually.

For full details on notification types, preferences, and delivery, see [Push Notifications](notifications.md).

---

## Related Topics

- [Push Notifications](notifications.md) -- Configure alerts for payments, expirations, and low balances
- [Wallet Management](wallet-management.md) -- Add, remove, and label monitored wallets
- [Installation](installation.md) -- Install Pulse as a PWA on your device
- [Privacy & Data](privacy-and-data.md) -- What data Pulse stores and how it's handled
