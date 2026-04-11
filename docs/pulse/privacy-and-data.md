---
title: Pulse Privacy & Data
description: How Subscrypts Pulse handles user data, GDPR compliance, and complete data erasure on unregister.
status: new
tags:
  - subscrypts
  - pulse
  - privacy
  - GDPR
  - data
  - security
---

# Privacy & Data

Subscrypts Pulse is built on a **custodian-free, privacy-first** design. It monitors your subscriptions by reading public blockchain data — without accessing your wallet, collecting personal information, or tracking your activity.

---

## Custodian-Free Design

Pulse is **read-only**:

* It **never** asks for private keys, seed phrases, or wallet passwords
* It **cannot** initiate transactions, transfer funds, or interact with your wallet
* It **only** reads public data from the Arbitrum blockchain (subscription status, balances, plan metadata)

You provide your public wallet address — Pulse reads on-chain data associated with that address. That's the full extent of the interaction.

---

## What Data Pulse Stores

Pulse stores the minimum data needed to deliver its monitoring and notification services:

| Data | Purpose | Retention |
|------|---------|-----------|
| **Device push token** | Deliver push notifications to your device | Until device is unregistered |
| **Public wallet addresses** | Monitor subscriptions and balances on-chain | Until wallet is removed or device is unregistered |
| **Wallet labels** | Display friendly names in the UI | Until wallet is removed or device is unregistered |
| **Notification preferences** | Respect your per-type toggles, quiet hours, and thresholds | Until device is unregistered |
| **Notification history** | Display past notifications in-app | Auto-deleted after 90 days |
| **Device metadata** | Platform (iOS/Android/web), app version | Until device is unregistered |

---

## What Data Pulse Does Not Collect

* **Personal information** — No names, emails, phone numbers, or addresses
* **Private keys or seed phrases** — Never requested, never transmitted, never stored
* **Transaction signing** — Pulse cannot prompt you to sign transactions
* **Analytics or tracking** — No behavioral analytics, no advertising trackers
* **Chat messages or social data** — Pulse has no access to your Telegram, Discord, or other platform data

---

## GDPR Compliance

Pulse supports **complete data erasure** in compliance with GDPR (General Data Protection Regulation) principles:

### Unregistering Your Device

In **Settings**, you can unregister your device. This triggers a **cascading delete** that removes:

* Your device registration
* All monitored wallet addresses and labels
* All notification preferences
* All notification history

After unregistering, Pulse retains **zero data** about your device or wallets. This is an irreversible action.

### How to Unregister

1. Open **Settings** in Pulse
2. Scroll to the bottom
3. Tap **Unregister Device**
4. Confirm the action

!!! warning "Irreversible"
    Unregistering deletes all your data permanently. If you want to use Pulse again, you'll need to re-add your wallets and reconfigure your preferences.

---

## Data in Transit

All communication between Pulse and its backend is encrypted:

* **HTTPS/TLS** — All API requests use encrypted connections
* **Push notifications** — Delivered via encrypted channels (FCM/APNs for mobile, VAPID for web)

---

## Comparison with Traditional Monitoring

| | Subscrypts Pulse | Traditional Subscription Managers |
|---|---|---|
| **Private keys required** | Never | Often (for connected accounts) |
| **Personal data collected** | None | Email, name, payment details |
| **Data erasure** | Complete on unregister | Varies; often incomplete |
| **Analytics tracking** | None | Common (behavioral, advertising) |
| **Permissions needed** | Notifications only | Broad device access typical |

---

## Related Topics

- [Features & Dashboard](features.md) -- What Pulse displays and how
- [Wallet Management](wallet-management.md) -- Adding and removing monitored wallets
- [Push Notifications](notifications.md) -- How notifications are delivered and stored
- [Installation](installation.md) -- Installing and uninstalling Pulse
