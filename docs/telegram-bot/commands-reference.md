---
title: Telegram Bot Commands Reference
description: Complete reference of all Subscrypts Telegram Bot admin commands with syntax, permissions, and usage scenarios.
status: new
tags:
  - subscrypts
  - telegram
  - commands
  - admin
  - bot commands
---

# Commands Reference

This page provides a comprehensive list of commands available in the **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)**.

Each command includes:

* Syntax
* Required permissions
* When and why to use it

---

## How Commands Work

The Subscrypts Telegram Bot uses two types of interactions:

1. **Admin commands** — Run inside a gated Telegram group by group administrators. These manage configuration, enforcement, and diagnostics.
2. **User commands** — Run in a **private chat** with the bot by subscribers. These check status and provide help.

!!! info "Admin Commands Are Group-Only"
    All `/admin` commands must be run **inside a Telegram group** where the bot is installed and the user has admin permissions. They do not work in private chats.

---

## Admin Commands -- `/admin`

These commands are available only to **group administrators** and are scoped to the group where they are run.

### `/admin setup`

Check the bot's configuration and setup status for this group.

```text
/admin setup
```

* **Who can use:** Group admins
* **Use when:**
    * You just added the bot and want to verify it's configured correctly.
    * You want to see the current setup status (permissions, ToS, plans, admin status).
* **What it does:**
    * Reports whether the bot has the required admin permissions.
    * Shows Terms of Service acceptance status.
    * Lists mapped plans.
    * Provides guidance on next steps if anything is missing.

---

### `/admin check`

Run a comprehensive 9-point diagnostic.

```text
/admin check
```

* **Who can use:** Group admins
* **Use when:**
    * Something seems off (members not being added/removed as expected).
    * After changing bot permissions or group settings.
* **What it does:**
    * Checks bot admin permissions (invite, ban, delete messages).
    * Verifies Terms of Service acceptance.
    * Validates plan mappings.
    * Tests blockchain RPC connectivity.
    * Reports findings with specific fix suggestions.

---

### `/admin plan`

View subscription plans mapped to this group.

```text
/admin plan
```

* **Who can use:** Group admins
* **Use when:**
    * Auditing which plans are active for your group.
    * Verifying that a newly created plan was mapped correctly.
* **What it does:**
    * Lists all subscription plans mapped to this group.
    * Shows plan details (ID, price, duration, currency).

---

### `/admin stats`

View group subscriber statistics.

```text
/admin stats
```

* **Who can use:** Group admins
* **Use when:**
    * You want an overview of your group's subscription health.
    * Checking how many members are active subscribers.
* **What it does:**
    * Shows total linked members, active subscribers, and expired counts.
    * Provides a snapshot of group membership status.

---

### `/admin reconcile`

Force an immediate subscription verification pass.

```text
/admin reconcile
```

* **Who can use:** Group admins
* **Use when:**
    * You know on-chain state has just changed and want membership to update quickly.
    * After configuration changes (new plan mappings, permission fixes).
    * Troubleshooting — to force the bot to recheck all members now.
* **What it does:**
    * Triggers an immediate reconciliation cycle for this group.
    * Checks all linked members against on-chain subscription state.
    * Invites or removes members as needed.

---

### `/admin ledger`

View the membership action audit trail.

```text
/admin ledger
```

* **Who can use:** Group admins
* **Use when:**
    * Auditing recent membership changes (who was invited, who was removed, and why).
    * Investigating a specific member's access issue.
* **What it does:**
    * Shows the last 20 membership actions.
    * Each entry includes: user, action (invite/remove), reason, and timestamp.

---

### `/admin rpc-health`

Check blockchain endpoint health.

```text
/admin rpc-health
```

* **Who can use:** Group admins
* **Use when:**
    * You suspect blockchain connectivity issues.
    * Subscriptions are not being detected or verified.
* **What it does:**
    * Reports the status of configured Arbitrum RPC endpoints.
    * Shows whether endpoints are reachable and responding correctly.

---

### `/admin unlink <user>`

Force-unlink a member's wallet from this group.

```text
/admin unlink @username
```

* **Who can use:** Group admins
* **Use when:**
    * A member needs to re-link with a different wallet.
    * Resolving a support case where a wallet link is stuck.
    * Security enforcement — removing a compromised wallet link.
* **What it does:**
    * Removes the wallet-to-user linkage for the specified member in this group.
    * The member can link a new wallet by going through the wallet-link flow again.

---

### Migration Commands

These commands manage the transition from a free group to subscription-gated access.

#### `/admin migrate <days>`

Start migration mode with a grace period.

```text
/admin migrate 14
```

* **Who can use:** Group admins
* **Use when:**
    * Your group has existing free members and you want to introduce paid access.
* **What it does:**
    * Starts a grace period of the specified number of days (1–90).
    * Pins an announcement with Subscribe and Link Wallet buttons.
    * Activates the join gate for new members immediately.
    * Begins posting automated reminders.

#### `/admin migrate status`

Check migration progress.

```text
/admin migrate status
```

* **What it does:** Shows how many members have subscribed, how many are pending, and time remaining.

#### `/admin migrate adjust <days>`

Adjust the grace period deadline.

```text
/admin migrate adjust 21
```

* **What it does:** Moves the deadline to the specified number of days from the original start.

#### `/admin migrate end`

End the grace period and begin enforcement.

```text
/admin migrate end
```

* **What it does:** Ends migration mode. Known members without linked wallets and active subscriptions are removed. Requires confirmation before proceeding.

---

## User Commands (Private Chat)

These commands are available to **all users** in a private chat with the bot.

### `/start`

Begin interaction with the bot.

```text
/start
```

* **What it does:**
    * Shows a welcome message explaining the bot.
    * If opened via a deep link (e.g., from a subscribe page), starts the wallet-linking flow for a specific group.

### `/status`

Check your subscription status.

```text
/status
```

* **What it does:**
    * Shows your subscription status across all groups where you have linked a wallet.
    * Indicates which subscriptions are active, expiring soon, or expired.

### `/help`

Show available commands.

```text
/help
```

* **What it does:** Lists the commands available to you based on context (private chat vs. group).

---

## Command Summary

### Admin Commands (in-group)

| Command | Purpose |
|---------|---------|
| `/admin setup` | Check bot configuration and setup status |
| `/admin check` | Run 9-point diagnostic |
| `/admin plan` | View mapped subscription plans |
| `/admin stats` | View group subscriber statistics |
| `/admin reconcile` | Force immediate subscription check |
| `/admin ledger` | View last 20 membership actions |
| `/admin rpc-health` | Check blockchain endpoint health |
| `/admin unlink <user>` | Remove a user's wallet link |
| `/admin migrate <days>` | Start migration grace period |
| `/admin migrate status` | View migration progress |
| `/admin migrate adjust <days>` | Adjust grace period deadline |
| `/admin migrate end` | End migration and enforce |

### User Commands (private chat)

| Command | Purpose |
|---------|---------|
| `/start` | Welcome message or deep-link wallet linking |
| `/status` | Check subscription status across groups |
| `/help` | Show available commands |

!!! info "Subscriber Interactions"
    Unlike the Discord Bot where subscribers use slash commands to link wallets, the Telegram Bot handles subscriber-facing interactions (subscribing, wallet linking, plan browsing) through dedicated pages at [telegram.onsubscrypts.com](https://telegram.onsubscrypts.com). This provides a richer, more user-friendly experience with full wallet integration.

!!! ecosystem "Subscrypts Ecosystem"
    Commands interact with subscription plans stored on the [Smart Contract Suite](../smart-contract/introduction.md) on Arbitrum. Plans can also be created and managed through the [Subscrypts dApp](../dapp/introduction.md).

---

## Related Topics

- [Admin Setup Guide](admin-setup-guide.md) -- Full setup and configuration journey
- [Member Guide](member-guide.md) -- Wallet linking and subscribing from the user's perspective
- [Subscription Synchronization](subscription-sync.md) -- How the background reconciler works
- [Best Practices](best-practices.md) -- Operational tips and common issue resolution
- [Smart Contract Suite](../smart-contract/introduction.md) -- On-chain plan creation and subscription logic
