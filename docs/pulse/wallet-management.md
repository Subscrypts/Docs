---
title: Managing Wallets in Pulse
description: How to add, remove, and monitor multiple wallets in Subscrypts Pulse for comprehensive subscription tracking.
status: new
tags:
  - subscrypts
  - pulse
  - wallets
  - multi-wallet
  - monitoring
---

# Managing Wallets in Pulse

Subscrypts Pulse monitors your on-chain subscriptions by watching the wallet addresses you provide. This page explains how to add, label, and manage your monitored wallets.

---

## Adding a Wallet

To start monitoring a wallet:

1. Open **Settings** in Pulse, or tap **Add Wallet** from the dashboard (if no wallets are configured)
2. Enter your **Ethereum wallet address** (the public `0x...` address)
3. Optionally add a **label** (e.g., "Main Wallet", "Cold Storage", "Business")
4. Tap **Add Wallet**

Pulse validates the address format before adding it. Once added, the app begins fetching subscription data and balances for that wallet.

!!! info "Public Address Only"
    Pulse only needs your **public wallet address** — the one that starts with `0x`. It never asks for private keys, seed phrases, or wallet passwords. Pulse is read-only and cannot initiate any transactions.

---

## Wallet Limits

You can monitor **up to 20 wallet addresses** per device. This is sufficient for most users who want to track personal wallets, hardware wallets, and business wallets simultaneously.

---

## Labeling Wallets

Labels help you identify wallets at a glance in settings and notification messages. Examples:

* "Main Wallet"
* "Ledger"
* "Trading Account"
* "Team Treasury"

Labels are stored on Pulse's server and are associated with your device registration.

---

## Removing a Wallet

To stop monitoring a wallet:

1. Open **Settings** in Pulse
2. Find the wallet you want to remove
3. Tap the **Remove** button

When you remove a wallet:

* Pulse stops monitoring that wallet's subscriptions and balances
* The wallet's data is removed from your dashboard
* You stop receiving notifications for that wallet
* The wallet can be re-added at any time

---

## Multi-Wallet Use Cases

### Personal + Business

Track subscriptions across your personal wallet and a separate business wallet. Pulse aggregates balances and subscriptions from both, so you see everything in one place.

### Hardware + Hot Wallet

Monitor subscriptions on your hardware wallet (Ledger, Trezor) alongside your hot wallet (MetaMask). Since Pulse only needs the public address, there's no need to connect your hardware device.

### Family or Team

Add wallet addresses for family members or team members to monitor their subscription status. Useful for ensuring everyone's access remains active.

!!! tip "Dashboard Aggregation"
    Balances and subscription counts on the dashboard are aggregated across all monitored wallets. The subscription list shows which wallet each subscription belongs to.

---

## Security Considerations

* **Read-only** — Pulse cannot initiate transactions, transfer funds, or interact with your wallet in any way
* **No private keys** — Only public wallet addresses are stored
* **Public data** — All subscription and balance data is read from the public Arbitrum blockchain
* **No wallet connection required** — Unlike the dApp or bot integrations, Pulse does not ask you to "connect" your wallet. You simply type or paste your public address.

---

## Related Topics

- [Features & Dashboard](features.md) -- How wallet data appears in the dashboard
- [Push Notifications](notifications.md) -- Notifications are scoped to your monitored wallets
- [Privacy & Data](privacy-and-data.md) -- How wallet data is stored and deleted
- [Installation](installation.md) -- Set up Pulse and add your first wallet
