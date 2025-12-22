---
title: Commands Reference
description: Complete categorized reference of all live Subscrypts Discord Bot commands, with syntax, permissions, and usage scenarios.
tags:
 - commands
 - slash commands
 - discord bot
 - admin
 - user
---

# Commands Reference

This page provides a comprehensive list of **currently live** commands available in the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)**, based on the latest version 0.5.8.

Each command includes:

* ✅ Syntax
* 🔐 Required permissions
* 📘 When and why to use it
* ⏱ Cooldown behavior

---

## How Command Replies Work

Most Subscrypts commands reply with **ephemeral responses**:

- **Ephemeral** means:  
  *Only you* can see the message, and it disappears if you refresh the Discord client.
- This keeps busy channels clean while still giving you detailed feedback.

Cooldowns:

- **Member `/subs ...` commands**: `1 use / 30 seconds per user`.
- **Admin `/subs-admin ...` commands**: `1 use / 15 seconds per user`.

If you hit a cooldown, Discord will show a **“You are on cooldown”** message and indicate when you can use the command again.

> All Subscrypts commands must be run **inside a server** (guild) where the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** is installed. They do **not** work in DMs.

---

## Member Commands – `/subs`

These are available to **all members** in a server that uses Subscrypts. They are scoped **per guild** – using a command in one server never affects another server.

### `/subs ping`

Quick health check for the bot.

```text
/subs ping
```

* **Who can use:** Any member
* **Cooldown:** 1 / 30 seconds per user
* **Use when:**
    * You want to verify the bot is online and responding.
    * You’re troubleshooting and need to confirm the bot can see your messages.
* **What it does:**
    * Replies with a short, ephemeral “pong” / health message.
    * Confirms that the bot is active in that server and can process `/subs` commands.

---

### `/subs link`

Starts the **wallet linking** flow for this server.

```text
/subs link
```

* **Who can use:** Any member
* **Cooldown:** 1 / 30 seconds per user
* **Use when:**
    * You are connecting your wallet for the first time in this server.
    * You want to re-link your previous unlinked wallet.
    * You want to link a additional wallet to this discord server 
* **What it does:**
    * Opens a **private thread** with you inside the server.
    * Sends a **secure wallet-link URL** generated specifically for:
        * your Discord user, and
        * this guild.
    * When you open the link, you:
        * Connect your wallet on **Arbitrum One**.
        * Sign a **gasless message** to prove you control that wallet.

Once completed:

* Your wallet is linked to your Discord account **for this server only**.
* The bot checks if that wallet already has active subscriptions for this guild and, if so, assigns the appropriate **premium roles**.

> This is usually the **first command** a member runs in a Subscrypts-enabled server.

---

### `/subs unlink`

Unlinks one of your wallets for this server.

```text
/subs unlink
```

* **Who can use:** Any member
* **Cooldown:** 1 / 30 seconds per user
* **Use when:**
    * You want to **stop using** a particular wallet in this server.
    * You are switching to a new wallet and want to clean up the old link.
* **What it does:**
    * Allows you to select and **remove** one of your linked wallets for this guild.
    * Closes the associated private thread for that wallet.
    * Stops the bot from using that wallet to decide your roles in this server.

Important:

* `/subs unlink` **does not cancel** or refund any on-chain subscription by itself.
  It only removes the **link** between your Discord user and that wallet in this guild.
* If you later re-link the same wallet and it still has an active subscription, your premium roles will be restored.

---

### `/subs my-links`

Shows which wallets you currently have linked in this server.

```text
/subs my-links
```

* **Who can use:** Any member
* **Cooldown:** 1 / 30 seconds per user
* **Use when:**
    * You forgot which wallet is linked.
    * You want to audit which wallets are connected for this guild.
* **What it does:**
    * Returns an **ephemeral** list of:
        * Wallet addresses linked in this server.
        * Their associated private threads and metadata.
    * Helps you decide which wallet to unlink or keep using.

> This command pairs naturally with `/subs unlink` when cleaning up or switching wallets.

---

## Admin Commands – `/subs-admin`

These commands are only available to users with appropriate server-level permissions (typically **Server Owner** or members of the **`Subscrypts Admin`** role) and are always scoped to the current guild.

They are meant to be used primarily in:

* The **`#subscrypts-admin`** channel, or
* Other admin/operations channels where you manage your server.

### Setup & Admin Guide

#### `/subs-admin setup`

Bootstrap or repair the core admin setup for Subscrypts.

```text
/subs-admin setup
```

* **Who can use:** Admins (Server Owner / Manage Server)
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * You just installed the bot and want to initialize it.
    * The `#subscrypts-admin` channel was deleted or broken.
* **What it does:**
    * Ensures an admin-only channel (**`#subscrypts-admin`**) exists.
    * Pins the **Subscrypts — Admin Setup** guide with buttons (Accept Terms, Apply Baseline, etc.).
    * Sets up baseline configuration needed for the bot to operate.

---

#### `/subs-admin admin-guide`

Re-post and re-pin the Admin Guide message.

```text
/subs-admin admin-guide
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * The admin guide message was unpinned, deleted, or lost in history.
    * You want to bring the Admin Guide back to the top for new staff.
* **What it does:**
    * Recreates and **pins** the Admin Guide message in `#subscrypts-admin`.
    * Restores the action buttons (Accept Terms, Apply Baseline, Apply Starter Template, Create Subscription, etc.).

---

#### `/subs-admin tos-accept`

Accept the server-level Terms of Service for using the bot.

```text
/subs-admin tos-accept
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * You want to accept the bot’s Terms **via command** instead of the button in the Admin Guide.
    * The guide button was not accessible or didn’t render correctly.
* **What it does:**
    * Records your guild’s acceptance of the Subscrypts Terms for bot usage.
    * Required before certain operations (like applying baseline or creating plans).

> Functionally similar to pressing **“Accept Terms”** in the Admin Guide.

---

### Plan ↔ Role Mapping

These commands connect **on-chain subscription plans** to **Discord roles**.

#### `/subs-admin map`

Map a plan id to one or more roles.

```text
/subs-admin map plan_id:<planId> role:<@Role>
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * You have created a Subscrypts plan on Arbitrum (via the Discord-native `createSubscription` page or the dApp).
    * You want members with that plan to receive a specific Discord role.
* **What it does:**
    * Stores a mapping between:
        * **Plan ID** (on-chain), and
        * One or more **Discord roles**.
    * When a member’s subscription for that plan is active, those roles are automatically granted; when it expires, they are removed.

> You can call `/subs-admin map` multiple times with the same `plan_id` and different roles to build multi-role mappings.

---

#### `/subs-admin list-plans`

See all current plan → role mappings in this guild.

```text
/subs-admin list-plans
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * Auditing which plans are connected to which roles.
    * Cleaning up old mappings.
* **What it does:**
    * Returns a structured, ephemeral summary of:
        * Plan IDs
        * Which roles are attached to each plan
    * Useful for checking that your premium roles are correctly wired up.

---

#### `/subs-admin unmap-plan`

Remove an entire plan mapping from this guild.

```text
/subs-admin unmap-plan plan_id:<planId>
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * A plan is no longer offered in your server.
    * You want to completely detach a specific on-chain plan from Discord roles.
* **What it does:**
    * Deletes **all role mappings** for that `plan_id` in this guild.
    * Future role assignments and reconciliations will ignore that plan.

---

#### `/subs-admin unmap-role`

Remove just one role from a plan mapping.

```text
/subs-admin unmap-role plan_id:<planId> role:<@Role>
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * A single role should no longer be granted by a plan, but the plan is still used.
* **What it does:**
    * Removes the mapping between one plan and one role.
    * Other roles linked to the same plan remain unchanged.

---

### Baseline, Template & Self-Test

These commands help you keep the server structure healthy and aligned with Subscrypts expectations.

#### `/subs-admin selftest`

Run a diagnostic of the bot’s configuration in this guild.

```text
/subs-admin selftest
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * Something “feels off” (roles not applying, missing channels, etc.).
    * After changing role order, permissions, or deleting channels.
* **What it does:**
    * Checks:
        * Bot permissions and intents.
        * Presence of required roles and channels.
        * Role order constraints (bot role above managed roles).
    * Returns a checklist of findings and suggestions.

---

#### `/subs-admin apply-baseline`

Create or repair the **required** roles and channels.

```text
/subs-admin apply-baseline
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * Setting up the bot for the first time.
    * After accidental deletion of core roles/channels.
* **What it does:**
    * Ensures that required roles (e.g. `Subscrypts Admins`) and channels (e.g. `#subscrypts-admin`, `#connect`) exist with sensible defaults.
    * Tries to be **idempotent** – safe to run multiple times; it will fix or add missing pieces rather than breaking your layout.

---

#### `/subs-admin apply-template`

Apply an **optional** starter layout.

```text
/subs-admin apply-template
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * You want a ready-made “premium community” server structure.
    * You’re starting from scratch and want a good default.
* **What it does:**
    * Creates a curated set of categories and channels (for example `welcome`, `web3/account`, `web3/channels`, `#no-active-subscription`).
    * May post a one-time **template notice** in key channels (connect/swap/subscribe/no-active-subscription).
    * Leaves room for you to customize further; can be reapplied later to repair missing pieces.

---

### Health, Reconciliation & Audit

#### `/subs-admin rpc-health`

Check the health of the bot’s blockchain RPC connections.

```text
/subs-admin rpc-health
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * You suspect RPC / blockchain connectivity issues (e.g., subscriptions not updating).
    * You’re working with Subscrypts support and need quick diagnostics.
* **What it does:**
    * Runs internal health checks against configured Arbitrum RPC endpoints.
    * Reports whether those endpoints are reachable and behaving as expected.

> Primarily a **diagnostic / advanced** tool for admins and support.

---

#### `/subs-admin grant-role`

Manually grant a role to a member (with safety checks).

```text
/subs-admin grant-role member:<@User> role:<@Role>
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * You need to grant a role **outside** of the subscription logic (e.g., staff roles, one-off access).
    * You want to correct a one-off edge case without changing mappings.
* **What it does:**
    * Grants the chosen role to the member, as long as:
        * The role is assignable by the bot.
        * Role order and basic safety checks pass.
    * Recorded in the **role ledger** for auditability.

---

#### `/subs-admin revoke-role`

Manually remove a role from a member (with safety checks).

```text
/subs-admin revoke-role member:<@User> role:<@Role>
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * You need to revoke a role manually, regardless of subscription state.
    * You’re cleaning up legacy roles or correcting mistakes.
* **What it does:**
    * Removes the specified role from the member, with the same safety checks as `grant-role`.
    * Also recorded in the **role ledger**.

---

#### `/subs-admin ledger`

View the role-change history (audit log) for this guild.

```text
/subs-admin ledger [member:<@User>] [limit:<n>]
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * Auditing how and when roles were granted or revoked.
    * Investigating an access issue for a specific member.
* **What it does:**
    * Shows recent ledger entries with:
        * Which user was affected
        * What role changed
        * By which mechanism (bot reconciliation, admin override, etc.)
    * Optional filters:
        * `member` – limit results to changes affecting one user.
        * `limit` – number of entries to show.

---

#### `/subs-admin reconcile-now`

Force an immediate reconciliation cycle.

```text
/subs-admin reconcile-now
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * You know that on-chain state has just changed (new subscriptions, cancellations, etc.) and want Discord roles to update quickly.
    * After you change mappings or repair configuration and want to immediately apply it.
* **What it does:**
    * Triggers a reconciliation tick for this guild:
        * Reads authoritative on-chain subscription state.
        * Compares it against current roles.
        * Grants or revokes roles as needed.
    * Compliments the background reconciler which runs on a schedule.

---

### Advanced Link Management (Admins)

These commands allow admins to help members troubleshoot or enforce security policies.

#### `/subs-admin unlink-admin`

Force-unlink a member’s wallet for this guild.

```text
/subs-admin unlink-admin member:<@User>
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * A user has lost control of a wallet and you want to break the link at the server level.
    * You need to reset a member’s link state so they can start fresh.
* **What it does:**
    * Removes the linkage between the member and their wallet(s) **for this guild**.
    * Closes associated private threads.
    * The user can still set up a new link later using `/subs link`.

---

#### `/subs-admin search-link-admin`

Search for links by wallet or user.

```text
/subs-admin search-link-admin [member:<@User>] [address:<0x...>]
```

* **Who can use:** Admins
* **Cooldown:** 1 / 15 seconds per user
* **Use when:**
    * You need to see which user is associated with a particular wallet address.
    * You want to see all links for a specific member.
* **What it does:**
    * Searches the link table for this guild using:
        * A Discord user, and/or
        * A wallet address.
    * Returns ephemeral results with matched links and context.

> Useful for **support requests**, security checks, and investigating access issues.

---

## Command Permissions & Cooldowns Overview

### Member (`/subs`) Commands

| Command          | Who can use | Purpose                             | Cooldown         |
| ---------------- | ----------- | ----------------------------------- | ---------------- |
| `/subs ping`     | Any member  | Check if the bot is responsive      | 1 / 30s per user |
| `/subs link`     | Any member  | Start wallet linking for this guild | 1 / 30s per user |
| `/subs unlink`   | Any member  | Unlink one wallet from this guild   | 1 / 30s per user |
| `/subs my-links` | Any member  | List wallets linked in this guild   | 1 / 30s per user |

### Admin (`/subs-admin`) Commands

| Command                         | Who can use | Purpose                                         | Cooldown         |
| ------------------------------- | ----------- | ----------------------------------------------- | ---------------- |
| `/subs-admin setup`             | Admins      | Initialize / repair core bot setup              | 1 / 15s per user |
| `/subs-admin admin-guide`       | Admins      | Re-post and pin the Admin Guide message         | 1 / 15s per user |
| `/subs-admin tos-accept`        | Admins      | Accept Subscrypts Terms for this guild          | 1 / 15s per user |
| `/subs-admin map`               | Admins      | Map a plan id to one or more roles              | 1 / 15s per user |
| `/subs-admin list-plans`        | Admins      | List all plan → role mappings                   | 1 / 15s per user |
| `/subs-admin unmap-plan`        | Admins      | Remove all roles for a given plan id            | 1 / 15s per user |
| `/subs-admin unmap-role`        | Admins      | Remove one role from a given plan id            | 1 / 15s per user |
| `/subs-admin selftest`          | Admins      | Run configuration and permission diagnostics    | 1 / 15s per user |
| `/subs-admin apply-baseline`    | Admins      | Create / repair required roles & channels       | 1 / 15s per user |
| `/subs-admin apply-template`    | Admins      | Apply the optional starter server template      | 1 / 15s per user |
| `/subs-admin rpc-health`        | Admins      | Check RPC / blockchain endpoint health          | 1 / 15s per user |
| `/subs-admin grant-role`        | Admins      | Manually grant a role with safety checks        | 1 / 15s per user |
| `/subs-admin revoke-role`       | Admins      | Manually revoke a role with safety checks       | 1 / 15s per user |
| `/subs-admin ledger`            | Admins      | View the role-change audit log                  | 1 / 15s per user |
| `/subs-admin reconcile-now`     | Admins      | Force an immediate reconciliation tick          | 1 / 15s per user |
| `/subs-admin unlink-admin`      | Admins      | Force-unlink wallets for a member in this guild | 1 / 15s per user |
| `/subs-admin search-link-admin` | Admins      | Search link records by member or wallet         | 1 / 15s per user |

---

For end-to-end flows and examples, see:

* **[Getting Started for Admins](04-getting-started-for-admins.md)** – full setup and configuration journey.
* **[Getting Started for Members](05-getting-started-for-members.md)** – wallet linking and subscribing from the user’s perspective.
* **[Subscription Synchronization](07-subscription-synchronization.md)** – how the background reconciler uses on-chain data to keep Discord roles in sync.
