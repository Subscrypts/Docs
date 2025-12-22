---
title: Best Practices & Troubleshooting
description: Recommendations and solutions for managing a Subscrypts-enabled Discord server effectively, minimizing sync issues, and resolving common problems.
tags:
 - best practices
 - discord admin
 - support
 - troubleshooting
 - role management
---

# Best Practices & Troubleshooting

Whether you’re managing a growing paid community or navigating your first blockchain-based subscription, these tips help ensure a smooth experience for both admins and members.

All **slash commands** used by the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** return **ephemeral responses** in Discord:

- Only the user who runs the command sees the output.
- Responses disappear when the page is reloaded or the session scrolls away.
- This keeps configuration details and wallet information private and reduces clutter in channels.

---

## Admin Best Practices

### Use Dedicated Premium Roles

Avoid reusing default roles like `@everyone` or general moderation roles.

Instead:

- Create **one or more dedicated roles per tier** (e.g., `Premium Lite Member`, `Premium Ultra Member`, `Beta Tester`).
- Map those roles to specific plans using the Admin Guide or `/subs-admin map`.

This keeps your permission model clean and makes it easier to reason about who should see what.

---

### Keep Channel Permissions Clean & Self-Gated

For **premium / gated** categories and channels:

1. Set **`@everyone` → View Channel: ❌ Deny**.
2. Allow **View Channel: ✅ Allow** only for:
    - The **premium roles** that should see the content,
    - Staff roles (e.g., `Subscrypts Admins`, moderators),
    - The bot’s own managed role where needed to avoid lockouts.

You can use **advanced permissions** (per-channel overrides) if you want finer control, but from Subscrypts’ perspective:

- It’s enough that **premium channels are private** and only accessible to the mapped premium roles (plus staff/bot).
- The bot simply ensures the **right users have the right roles**; you decide what those roles can see.

---

### Ensure Bot Role Ordering & Permissions

For the bot to manage roles correctly:

- The **Subscrypts bot’s role** must be **higher** than the premium roles it needs to grant or revoke (Discord server settings → *Roles*).
- The bot needs at least:
    - **Manage Roles**
    - **Manage Threads**
    - **Read Message History**
    - **Send Messages** in the channels it uses (e.g., `#subscrypts-admin`, `#connect`).

After major role or permission changes:

- Run **`/subs-admin selftest`** or use the **Run Self-Test** button in `#subscrypts-admin`.
- If needed, use **Apply Baseline** to repair required roles/channels **without** overwriting your custom premium layout.

---

### Pin Clear Wallet-Linking & Subscribe Instructions

In your `#connect` (or equivalent) channel:

- Pin a short message explaining:
    - How users should run `/subs link`,
    - That a **private thread** will open,
    - That they’ll receive a **secure wallet-link URL**,
    - And that they should only trust subscribe links starting with `https://discord.onsubscrypts.com/...`.

Consider also pinning:

- The server’s **main Subscribe link** (per-guild subscription page).
- A brief FAQ on **what tokens are used** (SUBS / USDC) and that **ETH on Arbitrum** is required for gas.

---

### Use `/subs-admin list-plans` Regularly

As you add or adjust plans, it’s useful to keep an overview:

```text
/subs-admin list-plans
```

Use this to:

* See which **plan IDs** exist for your guild.
* Verify which **roles** are mapped to which plans.
* Spot old or unused mappings you may want to remove via:
    * `/subs-admin unmap-plan`
    * `/subs-admin unmap-role`

This is especially helpful when you have multiple tiers or experimental plans.

---

### Re-run Baseline & Self-Test After Major Changes

If you:

* Move or rename key channels,
* Create new premium categories,
* Restructure roles extensively,
* Re-invite the bot or change its permissions,

then:

1. Open `#subscrypts-admin`.
2. Use:
    * **Run Self-Test** to check intents, permissions, and role order.
    * **Apply Baseline** if required roles/channels are missing or broken.

These actions are **idempotent** — they repair what's required while respecting your custom layout as much as possible.

---

### Communicate How Billing Works

For transparency and user trust:

* Clearly explain that:
    * Subscriptions are **non-custodial on-chain transactions**.
    * All payments ultimately settle in **SUBS** on Arbitrum.
    * There is a **USDC fallback mechanism** for **direct subscription payments** when users don’t hold enough SUBS.
    * **Automatic renewal** still requires a **sufficient SUBS balance**.
* Encourage users to read your server’s own rules and link them to the **[Subscrypts MiCAR Whitepaper](https://subscrypts.com/whitepaper)** for broader context if needed.

---

## Member Best Practices

As a member in a Subscrypts-enabled server:

* **Enable Direct Messages (DMs)** from that server so the bot can open a private thread when you run `/subs link`.
* Only trust:
    * Wallet-link URLs you receive from the bot’s private thread,
    * Subscribe links that start with `https://discord.onsubscrypts.com/...`.
* Always check that your wallet is on **Arbitrum One** before subscribing.
* Keep some **ETH on Arbitrum** for gas and enough **SUBS** (or SUBS + USDC for fallback) to cover your subscriptions.
* Use `/subs my-links` to see which wallets are connected in a specific server.
* Use `/subs unlink` before switching wallets for that guild, then `/subs link` again with your new wallet.

---

## Common Troubleshooting Scenarios

### Role Not Applied After Payment

**For members:**

* Wait a short while — the bot needs to see the on-chain transaction.
* Confirm you paid from the **same wallet** you linked via `/subs link` for this server.
* Make sure your subscription was for the **correct guild/plan**, especially if you participate in multiple Subscrypts communities.

If you still don’t see your premium channels:

* Ask a moderator or admin to check mappings and run a manual sync.

**For admins:**

* Confirm the **plan is correctly mapped** to the expected role via:
    * `/subs-admin list-plans`
* Check that the **bot role is above** the premium role in the server’s role list.
* Ensure the premium channels are correctly gated (no accidental `@everyone` access).
* Run:

```text
/subs-admin reconcile-now
```

  to force a sync pass for the affected guild.

---

### Cannot Link Wallet (No Private Thread Appears)

**For members:**

* Make sure you can see the channel where you ran `/subs link`.
* Check that:
    * You haven’t blocked the bot.
    * DMs/threads for that server are not disabled in your Discord privacy settings.

If it still doesn’t work, contact a moderator and provide:

* A screenshot of where you ran `/subs link`,
* Whether you see any error message.

**For admins:**

* Confirm the bot can **create private threads** in that channel (permissions).
* Check that the **`#connect` (or chosen) channel** still exists and the bot can read/send messages there.

---

### Subscription Paid but Access Not Granted

**For members:**

* Verify the transaction on the **per-guild subscription page** or in the **[Subscrypts dApp](https://app.subscrypts.com)**.
* Confirm:
    * You subscribed **from the same wallet** that’s linked to this server.
    * The plan corresponds to this guild (not another server).
* If needed, re-run `/subs link` to re-open your private thread and verify the linked wallet.

**For admins:**

* Use `/subs-admin list-plans` to ensure that plan id is mapped.
* Run `/subs-admin reconcile-now` to trigger syncing.
* Check that the member’s **linked wallet** actually holds an **active subscription** for that plan.

---

### Member Upgraded or Downgraded Plan

When a member changes plan for the same guild:

* On-chain subscription state is updated (e.g., active subscription for Lite and or Ultra only).
* On the next sync tick / event:
    * The **new premium role(s)** are granted,
    * The **old premium role(s)** are removed, based on your configured mappings.

If changes seem delayed:

* Admins can run `/subs-admin reconcile-now`.
* Members can re-open their private thread with `/subs link` to double-check the linked wallet.

---

### Admin Removed a Role Manually

If an admin manually removes a premium role from a user but the subscription is still active:

* The bot will eventually **re-grant** the role during reconciliation, because **on-chain subscription state is the source of truth**.

To intentionally break the automatic link for a given plan/role combination:

* Use:

```text
/subs-admin unmap-role
```

or

```text
/subs-admin unmap-plan
```

so the role is no longer managed by the subscription engine.

If you just need a temporary override, consider:

* Using `/subs-admin revoke-role` for a one-off action,
* Then remapping / remediating later if needed.

---

### Unsure if the Bot Is Online or Responsive

Members and admins can both use:

```text
/subs ping
```

If the bot responds with a health check message, it’s online and able to receive commands.
If it doesn’t respond:

* Check Discord’s bot status,
* Ask a moderator / owner to verify whether the bot is still present and has permissions,
* Or check the official **[Subscrypts Discord](https://discord.onsubscrypts.com)** for status updates.

---

## When to Contact Support

Consider contacting support (or raising an issue in the official Subscrypts Discord) if:

* Role sync issues persist across **many users**, not just one.
* Subscriptions appear valid on-chain but are **consistently ignored** by the bot in multiple cases.
* You see repeated errors in your `#subscrypts-admin` logs that don’t resolve after:
    * Running **Self-Test**,
    * Applying **Baseline**,
    * Or using **Reconcile Now**.

Primary help channels:

* Your own server’s **admin-only bot log channel** (`#subscrypts-admin`).
* The official **[Subscrypts Discord](https://discord.onsubscrypts.com)** -> `support` for broader ecosystem support.

---

## Summary Checklist

| For Admins                                                                 | For Members                                                                 |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Use **dedicated premium roles** and map them clearly to plans              | Enable DMs/threads so `/subs link` can open a private thread                |
| Gate premium channels properly (`@everyone` denied, premium roles allowed) | Only trust subscribe links starting with `https://discord.onsubscrypts.com` |
| Keep the bot’s role **above** the roles it manages                         | Keep some ETH on Arbitrum for gas and enough SUBS (and optionally USDC)     |
| Run **Self-Test** and **Apply Baseline** after big structural changes      | Use `/subs my-links` and `/subs unlink` to manage which wallet is linked    |
| Use `/subs-admin list-plans` to audit mappings regularly                   | Ask moderators if something looks wrong rather than re-subscribing blindly  |
| Use `/subs-admin reconcile-now` when in doubt about sync                   |                                                                             |

For full setup guidance, see **[Getting Started for Admins](04-getting-started-for-admins.md)** and **[Architecture & Integration](03-architecture-and-integration.md)**.

To understand what happens behind the scenes, see **[Subscription Synchronization](07-subscription-synchronization.md)**, and for security design, review **[Security & Trust](08-security-and-trust.md)**.
