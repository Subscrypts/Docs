---
title: Telegram Bot Subscription Synchronization
description: How the Subscrypts Telegram Bot syncs blockchain subscription states with Telegram group membership in real time.
status: new
tags:
  - subscrypts
  - telegram
  - synchronization
  - automation
  - membership management
  - smart contracts
  - renewals
---

# Subscription Synchronization

The **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)** acts as a **live access control bridge** between on-chain subscription contracts and group membership in Telegram.

A simple mental model:

> **Telegram group membership is a "view" of the blockchain.
> The blockchain (Subscrypts Smart Contract Suite) is the single source of truth.**

This page explains:

* How the bot reads subscription state from the chain,
* How it uses **caching and batching** to stay efficient,
* How the **Join Gate** and **Reconciler** keep Telegram in sync,
* How everything recovers from missed events or manual membership changes.

---

## What "Real-Time" Means in Subscrypts

Whenever a subscriber:

* Subscribes to a plan,
* Lets a subscription expire,
* Cancels or fails to renew,

the **[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)** aims to reflect that state in Telegram **as quickly as possible** by:

1. Using a **join gate** to block unauthorized access attempts in real time,
2. Reacting to **on-chain events** when they occur (fast path), and
3. Running a **periodic reconciliation loop** (safety net) that double-checks every linked member for each group.

There are **no manual lists** or off-chain subscription databases. If the chain says the subscription is active, the bot's goal is to ensure the member has access. If the chain says it is inactive, the bot's goal is to remove them.

---

## Where Subscription Truth Comes From

The bot uses multiple data sources, but only one carries **truth** about who is subscribed:

| Layer / Source | What it stores / does | Is it "truth"? |
|---|---|---|
| **Subscrypts Smart Contract Suite** | On-chain subscription records, payments, start/end timestamps, auto-renew flags | Yes |
| **Subscription Index** (in-memory cache) | Wallet-centric index of "wallet → plans → status" built from contract view functions | Read helper |
| **Bot Database** (linked accounts, plan maps) | Which wallet is linked to which Telegram user, which plans map to which groups, audit trail | Metadata |
| **Telegram** (group membership) | Actual access control — who is in the group | Projection |

Before changing any membership, the bot **always checks on-chain state** (directly or via the index).

---

## The Join Gate

The **join gate** is the first line of defense. When someone attempts to join a gated group:

1. The bot intercepts the join event.
2. It checks whether the user has a linked wallet with an active subscription for a mapped plan.
3. If **not**, the user is immediately removed — they never see group content.
4. If **yes**, the user is allowed to stay.

The join gate operates in **real time** and prevents unauthorized access even between reconciliation cycles. It is especially important during migration periods, where the gate blocks new freeloaders while existing members enjoy a grace window.

---

## The Reconciler Loop

The **Reconciler** is the core synchronization engine. It runs in the background on a configurable interval and ensures that group membership stays aligned with on-chain state.

### Responsibilities

* Verify that all linked members still hold active subscriptions.
* Remove members whose subscriptions have expired.
* Re-invite members who have renewed.
* Send expiry notifications via DM.

### High-Level Flow

For each group:

1. **Load configuration** from the bot database:
    * Plan mappings: which plan IDs are associated with this group.
    * Linked accounts: which wallets are linked to which Telegram users.
2. **Check subscription status** for each linked member using:
    * The **Subscription Index** (fast path — in-memory lookup), and/or
    * **Multicall batches** for cache misses (multiple contract calls in one RPC request).
3. **Apply expiry-aware skipping**:
    * Members whose subscriptions expire **more than 24 hours** in the future are **skipped entirely** — no Telegram API call is made.
    * This achieves a ~95% skip rate at scale, dramatically reducing API usage.
4. **Compare on-chain state with group membership**:
    * If a member should be in the group but isn't → send a **single-use invite link**.
    * If a member should not be in the group but is → **remove** them and send a resubscribe DM.
5. **Log all actions** to an idempotent membership ledger for audit and recovery.

### Self-Correcting Behavior

This loop makes the system **self-correcting**:

* If an on-chain event was missed or delayed,
* If a member was manually added by an admin,
* If the bot was offline for a while,

the next reconciliation cycle will eventually bring the group back in line with blockchain state.

---

## Group Priority Classification

When multiple groups are managed simultaneously, the reconciler intelligently prioritizes:

1. **Dirty groups** — Groups flagged by recent blockchain events (e.g., a payment or cancellation involving a linked member). These are processed first.
2. **Near-expiry groups** — Groups with members whose subscriptions are about to expire. These need timely checks.
3. **Routine groups** — Groups where all members are well within their subscription periods. These can be checked less frequently.

This priority system ensures that time-sensitive membership changes are processed quickly, even when managing thousands of groups.

---

## Events vs. Periodic Reconciliation

The bot uses a **hybrid model**:

### Event-driven updates (fast path)

When a subscription is created, renewed, or stopped, the Subscrypts smart contracts emit events:

* `_subscriptionPay` — when a subscription starts or renews
* `_subscriptionStop` — when a subscription is cancelled or reaches end-of-term

The bot listens for these events and triggers **targeted checks** for the affected wallet and group.

### Periodic reconciliation (safety net)

The reconciler loop runs on a fixed interval to:

* Cover cases where events were missed or delayed,
* Catch expired subscriptions that haven't fired a fresh event,
* Undo unauthorized manual membership additions.

Together, events + periodic reconciliation ensure that **Telegram eventually matches the blockchain**, even under network hiccups or temporary issues.

---

## Caching and Efficiency

### Subscription Index

The bot maintains an **in-memory subscription index** — a wallet-centric cache of all active subscriptions:

* Refreshed periodically from the smart contract via a single bulk RPC call
* Provides near-instant lookups for subscription status checks
* **Reduces RPC calls by approximately 95%** compared to querying the chain for every member

### Multicall Batching

For cache misses or targeted verification:

* Multiple contract view calls are **batched into a single RPC request** using Multicall
* Reduces network overhead for bulk verification

### Expiry-Aware Skipping

The reconciler skips Telegram API calls for members whose subscriptions are far from expiry:

* Members with >24 hours until expiry consume **zero API calls** during routine checks
* At scale, this achieves approximately **1,200 effective API calls per 60-second cycle** — sufficient for managing over 1 million users with a single bot token

All caches are **short-lived and non-authoritative** — membership decisions are always confirmed against on-chain state before granting or revoking access.

!!! success "Source of Truth"
    The blockchain — and specifically the Subscrypts contract view functions — remains authoritative at all times. Caches are **performance hints** and never override on-chain verification prior to any membership change.

---

## Auto-Renew and What the Bot Sees

Auto-renewal is handled **entirely on-chain** by the Subscrypts Smart Contract Suite:

* If a subscriber has auto-renew enabled **and** enough SUBS, the contract processes a new payment at end of term.
* If funds are insufficient, the renewal fails and the subscription becomes inactive.

From the bot's perspective:

* It simply sees **"active" vs "not active"** when reading from the contract.
* When the contract reports **active**, the member should be in the group.
* When the contract reports **inactive**, the member should be removed.

There is **no Telegram command** to force a renewal or override on-chain state. Everything is derived from the blockchain.

---

## Manual Sync Tools for Admins

While most synchronization is automatic, admins have tools to inspect and nudge the system when needed.

### `/admin reconcile`

Runs a **single reconciliation cycle** for the current group. Use after:

* Mapping new plans
* Fixing configuration issues
* A batch of new subscriptions

### `/admin ledger`

Shows the most recent membership actions for this group, useful for investigating "Why wasn't this member added?" or "Why was this member removed?" type questions.

---

## Fail-Safes and Error Handling

Several layers help keep synchronization robust:

* **RPC pool with failover** — If one blockchain endpoint fails, others are tried automatically with exponential backoff.
* **Idempotent operations** — The same action can be attempted multiple times without side effects (prevents duplicate invites or removals).
* **Membership ledger** — All actions are logged with intent IDs for audit and recovery.
* **No private keys, no custodial risk** — The bot only reads public on-chain state and manages Telegram membership. It never holds keys or funds.

---

## Summary

* **Source of truth:** Subscription state lives on the **Subscrypts Smart Contract Suite** on Arbitrum.
* **How the bot knows:** It uses a **subscription index** (in-memory cache), **Multicall batching**, and **event listeners** to read on-chain state efficiently.
* **How Telegram stays in sync:** The **join gate** blocks unauthorized access in real time, while the **reconciler** loop periodically verifies all members.
* **How drift is fixed:** On-chain events update quickly; periodic reconciliation and `/admin reconcile` make the system **self-healing** after outages or manual changes.

---

## Related Topics

- [Architecture & Integration](architecture.md) -- How the integration works end to end
- [Commands Reference](commands-reference.md) -- Full list of admin and user commands
- [Best Practices](best-practices.md) -- Operational tips and common issue resolution
- [Security & Trust](security-and-trust.md) -- Privacy model, caching transparency, and data minimization
- [Smart Contract Suite](../smart-contract/introduction.md) -- On-chain subscription logic
