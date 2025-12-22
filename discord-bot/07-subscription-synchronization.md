---
title: Subscription Synchronization
description: How the Subscrypts Discord Bot syncs blockchain-based subscription states with Discord role access in real time.
tags:
 - synchronization
 - automation
 - role management
 - smart contracts
 - renewals
---

# Subscription Synchronization

The **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** acts as a **live access control bridge** between on-chain subscription contracts and role-based permissions inside Discord.

A simple mental model:

> **Discord roles are a “view” of the blockchain.  
> The blockchain (Subscrypts Smart Contract Suite) is the single source of truth.**

This page explains:

* How the bot reads subscription state from chain,
* How it uses **RPCs and caching** to stay efficient,
* How the **Reconciler** loop and **RoleEngine** keep Discord in sync,
* How everything recovers from missed events or manual role changes.

---

## What “Real-Time” Means in Subscrypts

Whenever a member:

* Subscribes to a plan,
* Lets a subscription expire,
* Cancels or fails to renew,
* Switches between tiers,

the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** aims to reflect that state in Discord **as quickly as possible** by:

1. Reacting to **on-chain events** (fast path), and  
2. Running a **periodic reconciliation loop** (safety net) that double-checks every linked wallet and mapped plan for each guild.   

There are **no manual spreadsheets** or off-chain subscription lists. If the chain says the subscription is active, the bot’s goal is to grant the mapped role(s). If the chain says it is inactive, the bot’s goal is to remove them.

---

## Where Subscription Truth Comes From

Subscrypts uses multiple data sources, but only one of them carries **truth** about who is subscribed:

| Layer / Source                               | What it stores / does                                                                                   | Is it “truth”? |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------- |
| **Subscrypts Smart Contract Suite (FacetView)** | On-chain subscription records, payments, start/end timestamps, auto-renew flags, USDC fallback, etc.    | ✅ Yes          |
| **Bot SubscriptionIndex** (off-chain indexer)    | Cached wallet-centric index of “wallet → plans → status” built from FacetView **view functions**.       | 🔍 Read helper |
| **Bot DB** (`planMap`, `linkedAccount`, …)   | Discord-side config: which wallet is linked to which user, which plan maps to which role, audit logs.   | ⚙️ Metadata    |
| **Discord** (roles & channels)               | Actual access control in the guild (who can see which channels).                                        | 📺 Projection  |

Before changing any role, the bot **always checks the on-chain view** (directly or via the index).   

---

## JSON-RPCs: How the Bot Talks to Arbitrum

To read from the chain, the bot uses **JSON-RPC** calls: standard HTTP requests to an Arbitrum node that ask things like:

* “What is the current subscription state for wallet `0x…` on plan `123`?”
* “What are the details of plan `456`?”
* “Give me logs for `_subscriptionPay` between block X and Y.”

Under the hood, this goes through the `RpcPool` helper:   

* It takes one primary RPC URL plus any number of **fallback URLs**.
* It runs requests in **round-robin** order and tracks failures per endpoint.
* If an endpoint fails or times out, it marks it “backing off” for a short period using **exponential backoff plus jitter**.
* Next calls are directed to **healthy** endpoints first; unhealthy ones are retried only after their backoff window passes.

This design:

* Prevents a single bad RPC endpoint from breaking the bot,
* Distributes load across multiple providers,
* Reduces the risk of **rate limiting** and **throttling** from any single RPC provider.

---

## Caching and the SubscriptionIndex

Calling JSON-RPC for every wallet and plan on every tick would be expensive and slow. To avoid this, the bot uses:

### SubscriptionIndex (wallet-centric indexer)

At startup, the bot creates and starts a **SubscriptionIndex**:   

* It connects to the Subscrypts contract on Arbitrum using the combined ABI.
* It periodically scans subscription data and writes a wallet-centric index like:

```text
wallet 0xABC... → {
  plan 101: ACTIVE until 2025-05-01T12:00Z,
  plan 202: EXPIRED at 2025-03-15T09:00Z,
  ...
}
```

This index is essentially a **read cache** of the FacetView read-only functions: the source of truth is still the blockchain, but the index lets the bot query **many wallet/plan combos quickly**.

### Multicall batching (fallback / complement)

The Reconciler can also use a **Multicall3** contract to batch multiple `FacetView` calls in a single RPC roundtrip:

* When possible, it groups “check subscription state for (wallet, plan)” calls into chunks.
* This reduces the overhead of N separate RPC calls.
* It’s used either as a fallback to the index or to verify specific pairs.

### Lightweight in-memory caches

On top of that, the bot keeps **ephemeral in-memory caches** (guild mappings, recent lookups) to avoid re-computing the same work every few seconds.

All of these caches are **short-lived and rebuildable**:

* They improve speed and reduce RPC load.
* They never replace the **on-chain state** as the arbiter of truth.

---

## The Reconciler Loop

The **Reconciler** is the heart of subscription synchronization. It runs in the background in a interval and is also callable on demand via `/subs-admin reconcile-now`.

### Responsibilities

* Computes **desired plan-role memberships** from cache / multicall.
* Grants or revokes mapped **premium roles**.
* Toggles **Linked / Unlinked / Expired** roles per member.

### High-Level Flow

For each guild:

1. **Load mappings & links** from the bot DB:
    * `planMap`: which plan IDs map to which Discord roles.
    * `linkedAccount`: which wallets are linked to which Discord users for this guild.
2. Compute the set of all **(wallet, plan)** combinations that matter for this guild.
3. For each pair, fetch status using:
    * The **SubscriptionIndex** (fast path), and/or
    * Direct **FacetView** read calls via Multicall batches.
4. Compare on-chain truth with current Discord roles:
    * If a wallet has an active subscription for plan X → **grant** the mapped role(s).
    * If no longer active → **revoke** the mapped role(s).
5. Apply or remove **meta-roles**:
    * `Linked Account` if the user has at least one linked wallet.
    * `Unlinked Account` if they have none.
    * `Expired Subscriptions` if they have no active premium plans but did have one previously.
6. Append each action (or no-op) to an **idempotent ledger** for audit and recovery.

This loop makes the system **self-correcting**:

* If an event was missed,
* If an admin manually changed roles,
* If the bot was offline for a while,

the next reconciliation tick will eventually bring reality back in line with the blockchain.

---

## RoleEngine and the Intent Ledger

All actual role changes go through the **RoleEngine**.

Key properties:

* Every grant/revoke is wrapped in an **intent** with a unique `intentId`.
* Role changes are logged into `roleChange` with:
    * guildId, userDiscordId, roleId,
    * action (`grant` / `revoke`),
    * status (`success`, `error`, `noop`),
    * optional error message.
* If the same `intentId` shows up again, it becomes a **no-op**.
* If a member already has the role, the engine logs a **noop** rather than re-adding it.

Defensive checks before changing roles:

* The bot must have **Manage Roles** privilege.
* It will not touch `@everyone` or managed/integration roles.
* It refuses to grant a role that sits **at or above** the bot’s top role in the role hierarchy.

Admins can inspect the ledger via `/subs-admin ledger` (see Commands Reference) to debug why a user did or did not get a role.

---

## Events vs. Periodic Reconciliation

Subscrypts uses a **hybrid model**:

### Event-driven updates (fast path)

When a subscription is:

* Created or renewed, or
* Stopped/cancelled,

the Subscrypts smart contracts emit events like `_subscriptionPay` and `_subscriptionStop`.

The Subscrypts Discord Bot:

* Listens for those events (via RPC logs or webhooks),
* Resolves which wallet and plan they relate to,
* Notifies the bot so it can trigger a **targeted reconciliation** for the affected wallet/guild.

This gives near-real-time updates after successful payments.

### Periodic reconciliation (safety net)

The Reconciler loop runs on a fixed interval to:

* Cover cases where events were missed or delayed,
* Catch expired subscriptions that haven’t fired a fresh event,
* Undo manual role edits that conflict with on-chain reality.

Together, events + periodic reconciliation ensure that **Discord eventually matches chain**, even under network hiccups or temporary RPC issues.

---

## Auto-Renew, Manual Payments, and What the Bot Sees

Auto-renewal is handled **entirely on-chain** by the Subscrypts Smart Contract Suite:

* If a subscriber has auto-renew enabled **and** enough SUBS (or SUBS via USDC fallback), the contract will process a new payment at the end of term.
* If funds are insufficient or allowances missing, the renewal fails and the subscription eventually reaches “inactive” state.

From the bot’s perspective there is no “off-chain toggle”:

* It simply sees **“active” vs “not active”** when reading from FacetView.
* When the chain reports **active**, the mapped premium role(s) must be present.
* When the chain reports **inactive**, the mapped premium role(s) must be absent.

There is **no Discord command** to force a renewal or to override on-chain state. Everything is derived from the contract’s view functions.

For a deeper look at the subscription lifecycle and auto-renew logic, see the **Smart Contract Suite** documentation.

---

## Manual Sync Tools for Admins

While most synchronization is automatic, admins have tools to inspect and nudge the system when needed.

### `/subs-admin reconcile-now`

```text
/subs-admin reconcile-now
```

* **Who can use:** Admins / users with `Manage Server` or the `Subscrypts Admins` role.
* **What it does:** Runs a **single reconciliation tick** for the current guild.
* **When to use:**
    * After you’ve just mapped new plans to roles,
    * After a large batch of subscriptions or migrations,
    * When you suspect some roles are out of sync and want an immediate refresh.

The response is **ephemeral** (only visible to the caller) and will either confirm success or show an error if something went wrong.

### `/subs-admin ledger`

```text
/subs-admin ledger
```

* Lists the most recent entries in the role-change ledger for this guild.
* Can be filtered by member.
* Useful for investigating “Why didn’t this user get the role?” type questions.

---

## User-side Commands and Ephemeral Responses

On the member side, the `/subs` commands support synchronization indirectly by keeping the **link between Discord and wallet** healthy.

### Core user commands

* `/subs ping` – quick health check that the bot is online.
* `/subs link` – opens a private thread and sends a secure, short-lived wallet link URL for that guild.
* `/subs unlink` – unlinks one of your wallets from this server (with autocomplete).
* `/subs my-links` – shows all wallets you currently have linked in this guild.

All these commands:

* Return **ephemeral responses** (only you can see them; they disappear if you reload the page),
* Have **cooldowns** (for example, `/subs ping` and `/subs link` are limited to one call per 30 seconds per user) to prevent spam and accidental rate-limiting of the RPC layer.

If a user hammers a command, they see an ephemeral message like:

> “⏳ You have hit our cooldown period — try again in X.Xs.”

This helps protect both the Discord API and the chain-side infrastructure.

---

## Fail-Safes and Error Handling

Several layers help keep synchronization robust:

* **RPC pool with backoff**
  If one RPC endpoint fails or slows down, others are tried automatically.

* **Retry on role assignments**
  Failed Discord role changes are logged and can be retried; guild permission issues are surfaced via the Admin Guide and `/subs-admin selftest`.

* **No private keys, no custodial risk**
  The bot only reads public on-chain state and writes roles in Discord. It never holds keys or funds.

* **Configurable intervals**
  Both the indexer and the reconciler are tuned via configuration, so the operator can adapt to higher load, more guilds, or stricter RPC limits over time.

---

## Summary

* **Source of truth:**
  Subscription state lives on the **Subscrypts Smart Contract Suite** (FacetView).

* **How the bot knows:**
  It uses **JSON-RPC** calls through a resilient `RpcPool`, a **SubscriptionIndex** cache, and optional **Multicall** batching to read on-chain state efficiently.

* **How Discord stays in sync:**
  The **Reconciler** loop and **RoleEngine** compute desired roles from on-chain truth plus local mappings, then grant/revoke roles in a safe, idempotent way.

* **How drift is fixed:**
  On-chain events update quickly; periodic reconciliation and `/subs-admin reconcile-now` make the system **self-healing** after outages or manual changes.

For a broader view of how all components fit together, see **[Architecture & Integration](03-architecture-and-integration.md)**. For configuration tips and operational patterns, continue with **[Best Practices & Troubleshooting](09-best-practices-and-troubleshooting.md)**.
