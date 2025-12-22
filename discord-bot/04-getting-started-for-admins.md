---
title: Getting Started for Discord Admins
description: Step-by-step setup guide for Discord server owners to configure and monetize their community with the Subscrypts Discord Bot.
tags:
 - discord admin
 - setup
 - server owner
 - monetization
 - role management
---

# Getting Started for Discord Admins

This guide helps Discord server owners set up and operate the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** so that premium access in their server is controlled automatically by **on-chain subscriptions** stored in the Subscrypts smart contract suite on Arbitrum.

> ✅ No coding required • ✅ Works with your existing roles & channels • ✅ Roles auto-sync to on-chain status

---

## Merchant Overview

From a merchant’s perspective, the Subscrypts Discord integration works like this:

1. **What Subscrypts is**  
   Subscrypts is a **blockchain-based subscription system** on Arbitrum. It lets you sell recurring access (subscriptions) without custodians or payment processors — funds flow **directly from your members’ wallets to your wallet**, enforced by smart contracts.

2. **What the Subscrypts Discord Bot does**  
   The **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** connects those on-chain subscriptions to Discord. It **grants** and **revokes** your premium roles automatically, based on each member’s live subscription status on-chain.

3. **What you do as a Discord admin**  
    - You are the **server owner** or have the `Manage Server` permission.  
    - You **add the bot** from the [Subscrypts Discord Bot](https://discord.onsubscrypts.com) setup page.  
    - In `#subscrypts-admin`, you walk through the **Admin Setup** (accept terms, apply baseline, self-test).  
    - You **create one or more subscription plans** using the Create Subscription link (Discord-native `createSubscription` flow).  
    - You **map each plan to one or more roles** (e.g., `Premium Lite Member`, `Premium Ultra Member`).  
    - You make sure the **bot’s role is higher** than the roles it needs to manage (e.g., your premium roles).
    - You gate your premium channels using those roles — the bot handles who actually gets them.

4. **What your members do**  
    - They **join your server**.  
    - They **link their Ethereum wallet** with `/subs link` in a private thread for your guild.  
    - They **subscribe to one of your plans** via the per-guild subscribe page exposed by the bot.  
    - The bot **automatically grants and later revokes** premium roles as their subscription stays active or expires.

5. **How payments work**  
    - Every payment is a **non-custodial on-chain transaction**.  
    - Subscribers pay from their own wallet; funds (minus protocol fees) go **directly to your merchant wallet** on Arbitrum.  
    - No cards, no bank accounts, no manually updating spreadsheets — the blockchain and the bot keep everything in sync.

Once you’ve completed these steps, you’ve effectively **monetized your Discord server** with self-custodial, on-chain subscriptions — and the bot takes care of the day-to-day access control for you.

---

## Prerequisites

Before you can integrate the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** and create Subscrypts subscription plans, make sure you meet the following prerequisites.

### Discord server ownership & permissions

To add and correctly configure the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)**, you need sufficient Discord permissions:

- If you created the server via **“Add a Server”** in the Discord sidebar, you are the **Discord Server Owner** by default.
- On larger or more moderated servers, the owner can grant other members high-level permissions such as **`Manage Server`** so they can also add and configure integrations like the Subscrypts bot.
- Without being **Server Owner** or having **`Manage Server`**, you **won’t be able to add** the Subscrypts Discord Bot to the server / or the integration will not function as intended.

### Ethereum wallet

* You need an **Ethereum‑compatible wallet** that you control.
* Subscrypts is **tested with MetaMask**, but other EVM wallets that support Arbitrum should also work.
* The wallet you use here will own your subscription plans and receive payments.

### Arbitrum network

* Your wallet must have the **Arbitrum One** network configured.
* Some wallets ship with Arbitrum pre‑added; in others you may need to add it manually.
* When you interact with the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)**, ensure that your wallet is **connected to Arbitrum One**, not Ethereum mainnet or another network.

### ETH for gas fees

To interact with the Subscrypts Smart Contract Suite on Arbitrum, you need **ETH on Arbitrum**:

* Every on‑chain action (e.g., creating a subscription plan, subscribing, renewing) consumes **gas fees** paid in ETH.
* Gas fees depend on **network congestion** (how busy Arbitrum is at that moment) and the **fixed fee logic** inside the Subscrypts contracts.
* At launch, creating a Subscrypts subscription plan costs roughly **0.0000032 ETH** (≈ **$0.01**) per plan. This is an **example value only** – actual fees could vary over time.

### Funding your wallet

You can fund your wallet with ETH on Arbitrum in several ways:

1. **Already have tokens in an EVM wallet?**
    - Swap those tokens for **ETH** on that network.
    - Then **bridge ETH to Arbitrum** using a compatible L2 bridge.

2. **Already have ETH on another network (e.g., Ethereum mainnet)?**
    - Use a bridge to move ETH from mainnet (or another L2) to **Arbitrum One**.

3. **Use a fiat on‑ramp provider:**
    - Many services let you buy **ETH** with traditional payment methods (card, bank transfer, etc.).
    - If possible, buy or move ETH **directly onto Arbitrum** to avoid extra bridging steps.

4. **Use a centralized exchange (CEX):**
    - Buy or convert your existing balance into **ETH** on the exchange.
    - Withdraw to your own **Ethereum wallet address** (e.g., `0x8Ed1...3fd27`).
    - If your exchange supports withdrawal **over the Arbitrum network**, select **Arbitrum** as the withdrawal network so the funds arrive on the correct chain immediately.

    > ⚠️ Always double‑check three things before withdrawing:
    >
    > 1. The **token** you are sending is `ETH` to pay for gas fees on arbitrum blockchain.
    > 2. The **network** you are using is `Arbitrum One` for Subscrypts.
    > 3. The **destination wallet address** is your own `0x...` address.
    >
    > Once your wallet holds ETH on **Arbitrum One**, the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** and **[Subscrypts dApp](https://app.subscrypts.com)** are designed to make the rest of the setup and daily usage as smooth as possible.

---

## Overview

There are two equivalent ways to configure the bot:

1. **Admin Guide UI (recommended)** — A pinned, admin‑only guide in `#subscrypts-admin` with buttons for common tasks (accept Terms, apply baseline, run self‑test, apply starter template, map plan↔role, list mappings, reconcile now, link‑flow help). Optimized for a smooth, user‑friendly setup experience.
2. **Slash Commands** — Full control via `/subs-admin ...` commands. Ideal for power users and automation.

Use either path or mix them at any time. Both write to the same configuration and state.

---

## Invite the Bot

Open the **[Discord Bot](https://discord.onsubscrypts.com)** page and click **Add to Server**. Ensure you:

* Are the Discord Server owner or have `Manage Server` permissions.
* Grant the Subscrypts Discord Bot requested permissions (notably **Manage Roles**, **Manage Channels**, **Create Private Threads**, **Read Message History**).

> Where the bot communicates
>
> * **Admin‑only:** Routine operational updates are posted in `#subscrypts-admin`.
> * **Public (optional):** A one-time template text is posted in curated channels (`#connect`, `#swap`, `#subscribe`, and `#no-active-subscription`).
> * **Private threads:** Per‑user flows (e.g., wallet linking) run in private threads.
> * **DM fallback:** If a channel is missing or restricted, the bot may DM the target user/admin.

---

## Quick Start via Admin Guide UI (recommended)

When you first add the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** to your server, it will automatically create an admin‑only channel named **#subscrypts-admin** and pin the **Subscrypts — Admin Setup** guide with interactive buttons.

### Admin Guide actions

The pinned message includes these controls:

* **Accept Terms** — Confirms server‑level Terms for using the bot.
* **Apply Baseline** — Creates/fixes **required** roles, categories and channels so the bot can operate (e.g., `Subscrypts Admins`, the admin channel, and core web3/account channels).
* **Run Self‑Test** — Verifies bot intents, permissions and role order; suggests fixes.
* **Apply Starter Template (optional)** — Creates a ready‑made set of categories/channels/overwrites for a polished “premium community” layout.
* **Create Subscription** — Opens the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** to create plans (pre‑filled with your guild id).
* **Map Plan ↔ Role** — Wizard to connect a plan ID to one or more Discord roles.
* **List Plan Mappings** — Shows all plan→role mappings in this guild.
* **Reconcile Now** — Immediately recomputes memberships and updates roles.
* **Link Flow Help** — Quick reference for member wallet linking (`/subs link` and `/subs unlink`).

If you don’t see the channel (for example, it was deleted or permissions blocked the initial creation), you can restore or recreate it at any time by running:

```text
/subs-admin setup
```

This command (re)creates the **#subscrypts-admin** channel if needed and re‑pins the **Subscrypts — Admin Setup** guide so you always have a central place to manage your configuration.

> You can rerun **Apply Baseline**, **Run Self‑Test** or **Apply Starter Template** safely — they are idempotent and report what changed.

---

## Subscrypts Baseline (required roles, channels & permissions)

The **Subscrypts Baseline** is the **minimum structure** the bot expects in every guild so it can work reliably. It focuses on **required roles** and a **required web3/account category** with the right permissions.

You trigger it via:

* The **Apply Baseline** button in `#subscrypts-admin`, or
* The `/subs-admin apply-baseline` slash command (advanced users).

### Required roles

Baseline ensures that the following roles exist and are correctly positioned under the bot’s own managed role:

* `Subscrypts Admins`
* `Linked Account`
* `Expired Subscriptions`
* `Unlinked Account`

What they’re used for:

* **Subscrypts Admins** — marks the people who operate the integration for your server. They get full read/write access in the relevant channels.
* **Linked Account** — applied to members who successfully link a wallet for your guild.
* **Expired Subscriptions** — applied to members whose subscriptions have lapsed (useful for routing them to renewal information).
* **Unlinked Account** — can be used in your permission model to represent members who have not yet linked a wallet.

Baseline also validates role **hierarchy**: the bot’s own managed role must sit **above** these roles so it can grant and revoke them. If Discord’s role order is out-of-sync, the bot guides the owner with a simple “drag-and-drop once” fix.

### Required web3/account category & channels

Baseline also ensures the **`web3/account`** category exists with these core channels:

* `connect`
* `swap`
* `subscribe`

Each is created (if missing) with **sane permission defaults**:

* **`connect`** – visible and writable for everyone so users can run `/subs link` and related flows (chat is limited to what’s needed for slash commands).
* **`swap`** – read-only informational channel (e.g., links or instructions for obtaining SUBS/ETH/USDC).
* **`subscribe`** – gated so only **Linked** accounts see a read-only announcement / call-to-action, tightly scoped to your subscribers.

On first baseline run, the bot also posts one-time **static notices** (template texts from the Subscrypts configuration) into these channels plus `#no-active-subscription`, giving your members a default explanation of what each channel is for. You can later edit or replace those messages according to your community’s style.

> Baseline **does not overwrite your entire server**. It only creates and fixes the minimal pieces the bot relies on, leaving the rest of your structure intact.

---

## Starter Template (optional premium layout)

The **Starter Template** is an **optional, opinionated layout** that builds on top of the baseline to give you a polished premium server structure out of the box.

You trigger it via:

* The **Apply Starter Template** button in `#subscrypts-admin`, or
* The `/subs-admin apply-template` slash command.

You can safely skip it if you already have a well-designed server layout. You can also run it once to bootstrap a layout and then customize everything afterwards.

### Starter roles

In addition to the required roles, the starter template introduces:

* `Premium Ultra`
* `Premium Lite`

These are intended as **example premium tiers**. The template:

* Ensures these roles exist.
* Positions all managed roles in a recommended order, roughly:

  `Subscrypts Admins` → `Premium Ultra` → `Premium Lite` → `Linked Account` → `Expired Subscriptions` → `Unlinked Account`

You can rename, recolor, or add additional roles later; the template is only a starting point.

### Starter categories & channels

The starter template ensures the following categories and channels exist and are wired with recommended permissions:

* **`Welcome`**
    - `welcome` – general welcome channel.
    - `rules` – for server rules.
    - `announcements` – read-only announcements for everyone.
* **`web3/channels`**
    - `premium-lite` – gated so only members with the **Premium Lite** role (and staff/bot) can see and chat.
    - `premium-ultra` – gated so only **Premium Ultra** members (and staff/bot) can see and chat.
    - `premium-ultra-voice` – voice channel for **Premium Ultra** members.
    - `no-active-subscription` – private read-only channel primarily visible to **Expired Subscriptions** members, where you can explain how to renew or upgrade.
* **`general`**
    - `public-chat` – general public discussion.
    - `support` – a place for members to ask for help.

For each of these, the template:

* Gives the bot’s own managed role full access to avoid lockouts.
* Grants `Subscrypts Admins` the same privileged access.
* Applies **view/send** rights to the correct premium roles only, with everyone else denied.

> The starter template is **idempotent**: re-running it will create missing pieces and gently enforce the recommended overwrites, but it won’t delete your custom channels or roles.

Once the baseline and (optionally) the starter template are applied, your server has a **clean, standardized foundation** that works well with Subscrypts and is easy for your team and members to understand.

---

## Create Your Subscription Plan(s)

Subscrypts subscriptions live **on-chain** on Arbitrum. The **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** and the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** are both UI layers on top of the same smart contract suite — the blockchain is the source of truth.

There are multiple ways to create a plan; for Discord admins, one path is **recommended**.

### Recommended: per‑guild link from `#subscrypts-admin`

In the **#subscrypts-admin** channel, the **Subscrypts — Admin Setup** guide includes a **Create Subscription** button. This button opens a per‑guild URL, for example:

```text
https://discord.onsubscrypts.com/createSubscription?guildId={guild.id}
```

When you use this link:

* The **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** opens with your **Discord guild id pre‑filled**.
* You create a subscription plan by:
    - Connecting your wallet (on **Arbitrum One**).
    - Entering the plan name, price, duration and other details.
    - Confirming the transaction in your wallet.
* After the transaction confirms, the **Subscrypts Discord Bot** receives the event and posts the **created plan details** (plan id, key parameters) back into **#subscrypts-admin** for later reference.

This is the **recommended flow** for Discord integrations, because the plan is immediately visible in your admin log and easier to map to roles in the next step.

### Alternative ways to create plans

You are not limited to the per‑guild link:

* You can open the **[Subscrypts dApp](https://app.subscrypts.com)** directly and use its *Create Subscription* page.
* Advanced users can use the dApp’s **interact** page or write their own code/scripts to call the Subscrypts smart contract suite directly.

If you create plans using one of these alternative methods, they are still fully valid: once you know the **plan id**, you can map it to roles in your Discord server. The only difference is that the bot will not automatically post the “new plan created” summary message in **#subscrypts-admin** unless the creation went through the per‑guild URL.

### Summary

Regardless of which method you choose:

* The **plan record** is stored on the Subscrypts smart contracts on **Arbitrum One**.
* The **[Subscrypts dApp](https://app.subscrypts.com)** and **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** simply read and act on that on-chain data.

> For a deep-dive into plan creation and quoting, see the [Subscrypts dApp docs](../dapp/01-introduction.md) and [Smart Contract Suite docs](../smart-contract/01-introduction.md) in this site.

---

## Map Plans to Roles

Once your plans exist on-chain, the **mapping step** tells the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)**:

> “When a member has an **active subscription** for plan X, they should get Discord role Y (and optionally Z, …).”

Without at least one mapping, the bot can’t grant any premium roles, even if members are subscribed.

You can configure mappings either via the **Admin Guide UI** in `#subscrypts-admin` or via **slash commands**. Both write to the same plan→role mapping table.

### A. Map via Admin Guide UI

1. Go to **#subscrypts-admin**.
2. Click **Map Plan ↔ Role**.
3. Enter the **Plan ID** (e.g., the one just created via the Create Subscription flow).
4. Select the **Discord role** (e.g., `Premium Ultra Member`, `Premium Lite Member`).
5. Confirm. You can map a single plan to **multiple roles** (for example, one text role + one voice role).

This is the easiest way for most admins, since it guides you step by step and validates your inputs.

### B. Map via Slash Command

Use the `/subs-admin map` command from any channel where you can use admin commands:

```text
/subs-admin map plan_id:<id> role:<@Role>
````

Examples:

```text
/subs-admin map plan_id:101 role:@Premium Lite Member
/subs-admin map plan_id:102 role:@Premium Ultra Member
```

You can also map **multiple plans to the same role** if you want several subscription options to unlock the same access tier (e.g., monthly vs. annual plans that both grant `Premium Ultra Member`).

**Related maintenance commands:**

* List mappings: `/subs-admin list-plans`
* Remove a plan entirely: `/subs-admin unmap-plan plan_id:<id>`
* Remove just one role from a plan: `/subs-admin unmap-role plan_id:<id> role:<@Role>`

> When a member has an **active on-chain subscription** for a mapped plan, the bot grants the mapped role(s). When the subscription expires, those role(s) are automatically removed on the next reconciliation tick.

---

## Verify the bot configuration

Once baseline and (optionally) the starter template are in place, you should verify the setup and then safely customize it for your community.

Use the **Self-Test** flow to make sure everything is wired correctly:

- Click **Run Self-Test** in `#subscrypts-admin`, or  
- Run the slash command:
```text
/subs-admin selftest
```

The self-test checks things like:

* Whether the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** can see and post in the required channels.
* Whether the **required roles** (`Subscrypts Admins`, `Linked Account`, `Expired Subscriptions`, `Unlinked Account`, and any starter premium roles) exist.
* Whether the bot’s managed role is **positioned above** the roles it needs to grant/revoke.
* Whether the core categories/channels created by Baseline are present.

If something is off, the guide in `#subscrypts-admin` will highlight what needs attention and how to fix it.

> Tip: After any major permissions/role rework in your server, re-run **Self-Test** to confirm everything still passes.

---

## Check bot role position in Discord

Discord only allows a bot to grant or remove roles that are **below** its own highest role in the role list.

To verify:

1. Go to **Server Settings → Roles**.
2. Locate the role associated with the **Subscrypts Discord Bot**.
3. Drag that role **above**:
    - `Premium Lite Member` / `Premium Ultra Member` (or your own premium roles),
    - `Linked Account`,
    - `Expired Subscriptions`,
    - `Unlinked Account`.

A recommended order looks roughly like:

1. `Subscrypts Discord Bot` (or your bot’s managed role)
2. `Subscrypts Admins`
3. Server Moderators, Support
3. Premium roles (e.g., `Premium Ultra Member`, `Premium Lite Member`)
4. Status roles (`Linked Account`, `Expired Subscriptions`, `Unlinked Account`)
5. Everything else (@everyone, etc., as fits your model)

If the bot’s role sits *below* any role it needs to manage, Self-Test will warn you, and the bot won’t be able to assign or revoke that role.

---

## Customize your roles safely

You are free to:

* Rename the starter roles (for example, rename `Premium Ultra Member` to `Diamond Tier`).
* Add new premium tiers (e.g., `Early Adopter`, `Founders Club`).
* Add more staff roles (e.g., `Community Manager`, `Support`).

Just keep these rules in mind:

* Any role the bot is expected to **grant or revoke** must stay **below** the bot’s managed role.
* When you create new premium roles that should be tied to on-chain plans, **map them** using:

  * **Map Plan ↔ Role** in `#subscrypts-admin`, or
  * `/subs-admin map plan_id:<id> role:<@Role>`.

You decide the names and visual hierarchy; the bot only cares about:

1. Role position (must be below the bot’s role), and
2. The plan↔role mappings you configure.

---

## Customize categories & channels (self-gated access)

You can fully tailor your server’s structure as long as your **permission model** respects how Subscrypts works:

* For **premium / gated categories and channels**:
    - Set **`@everyone`** to **“View Channel: ❌ Deny”**.
    - Allow **“View Channel: ✅ Allow”** only for:
        - The mapped **premium roles** (e.g., `Premium Lite Member`, `Premium Ultra Member`),
        - Staff roles (e.g., `Subscrypts Admins`, moderators),
        - The bot’s own managed role where needed to avoid lockouts.

* For **public/general channels** (like `welcome`, `rules`, `public-chat`):
    - Keep **`@everyone`** allowed to view.
    - Decide whether premium roles and linked/expired/unlinked roles inherit the same read/write rights or a stricter model.

If you introduce brand new premium areas (like `#trading-signals` or `#founders-chat`):

1. Create the channel and deny view for `@everyone`.
2. Grant view/send to the premium role(s) that should have access.
3. Make sure those roles are mapped to one or more Subscrypts plans.

The bot will then:

* **Grant** those roles when the member has an active on-chain subscription.
* **Revoke** them automatically as soon as the subscription expires or is cancelled and reaches end-of-term.

### Advanced per-channel permissions (optional)

Discord also allows very fine-grained, **advanced permissions** per channel (e.g., who can send messages, use threads, attach files, react, use voice, etc.). You can absolutely use these to fine-tune your premium experience — for example:

* Let everyone with a premium role **view** a channel but only staff post.
* Allow **voice** in one premium channel but keep another **read-only** for signals/announcements.
* Give moderators extra tools (e.g., timeout, manage messages) inside premium spaces.

From the Subscrypts point of view, there is only one critical requirement:

> Premium channels must remain **properly gated**:  
> `@everyone` (and other non-premium roles) should not have **View Channel** permission where access is meant to be subscription-based.

As long as:

* Premium channels are **private** (no view for `@everyone`), and  
* Only the **mapped premium roles**, staff roles, and the **bot’s role** are allowed to view them,  

Subscrypts doesn’t impose any extra rules on your advanced permissions. The exact read/write/voice rules inside those gated areas are entirely up to your community design.

> After bigger structural changes (new categories, moved channels, new premium roles), it’s a good idea to re-run **Self-Test** and, if needed, **Apply Baseline** again to repair any missing required pieces without touching your custom layout.

---

## Member Linking Flow (what users do)

Members link their wallet with:

```text
/subs link
```

A private thread opens for a gasless signature. On success, the bot recognizes the wallet and assigns roles for any **active** subscriptions (for plans you mapped). Members can unlink with:

```text
/subs unlink
```

> Tip: Pin clear instructions in your `connect` channel and consider enabling a link to your “Subscribe” channel in your announcements.

---

## Operational Tools (Admins)

Once your plans are mapped and members are linking wallets, most of the work is automatic. These tools are there for **operations, debugging, and rare interventions**.

### Reconciling (force a sync now)

Under normal circumstances, the **[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** keeps roles in sync with the blockchain using its background reconciliation logic. You do **not** need to run reconcile manually for everyday usage.

However, there are times when you may want to **force an immediate sync**, for example:

* After changing mappings (plan ↔ role).
* After fixing role order or channel permissions.
* After a period where the bot was offline and then comes back.

You can trigger this in two ways:

* Button: **Reconcile Now** in `#subscrypts-admin`.
* Slash command:

```text
/subs-admin reconcile-now
```

This tells the bot: “Re-check all known subscribers now and update their roles immediately based on on-chain subscription status.”

### Manual role actions (advanced / break-glass)

These commands are **advanced tools** intended for special situations (manual testing, customer support, or temporary overrides). They do **not** change on-chain subscription state; they only affect roles in Discord. On the next reconciliation pass, the blockchain truth will still win.

* Grant any assignable role:

```text
/subs-admin grant-role member:<@User> role:<@Role>
```

* Revoke any assignable role:

```text
/subs-admin revoke-role member:<@User> role:<@Role>
```

Typical use cases:

* Manually granting a role for a brief trial or support case.
* Removing a role from a user whose behaviour violates community rules (even if they are still technically subscribed).
* Testing permissions for a specific role without touching on-chain data.

These commands are idempotent and include safety checks (role order, managed roles, etc.), so you can’t accidentally grant roles the bot is not allowed to manage.

---

## Frequently Asked Questions

**Q: Can I run only with slash commands and ignore the Admin Guide UI?**
Yes. The Admin Guide is purely a UX layer. All core actions have `/subs-admin` equivalents. That said, flows like **Create Subscription**, **Apply Baseline**, and **Apply Starter Template** are usually easier to trigger from the pinned guide in `#subscrypts-admin`.

**Q: Can one plan grant multiple roles?**
Yes. You can map the same plan to multiple Discord roles (for example, one text role + one voice role, or a “bundle” of roles for a single tier).

**Q: Can multiple plans grant the same role?**
Also yes. If you have, for example, a monthly and a yearly plan for the same tier, you can map both plan ids to the same premium role. Any active subscription to either plan will keep that role active.

**Q: Do members need to re-link after renewing?**
No. Once a wallet is linked for a guild, renewals and expirations are picked up automatically by the reconciler. Members only need to re-link if they change Discord accounts or explicitly unlink with `/subs unlink`.

**Q: Do I need to use “Reconcile Now” every time someone subscribes?**
No. Reconciliation also runs in the background. “Reconcile Now” is mainly for **forcing an immediate sync** after configuration changes (new mappings, role order fixes, etc.) or for manual troubleshooting.

**Q: Where do I see sync status and admin notices?**
The bot posts operational updates (self-test results, reconciliation summaries, mapping changes, plan creation logs, errors) in **`#subscrypts-admin`**. This channel is your main audit log for the integration.

---

## Next Steps

* Continue to **[Getting Started for Members](05-getting-started-for-members.md)** to see the member journey.
* Review **[Commands Reference](06-commands-reference.md)** for all `/subs-admin` and member commands.
* Learn how background reconciliation works in **[Subscription Synchronization](07-subscription-synchronization.md)**.
* See **[Security & Trust](08-security-and-trust.md)** for a privacy and safety overview.
* Explore the **[Subscrypts Homepage](https://subscrypts.com)** and **[MiCAR Whitepaper](https://subscrypts.com/whitepaper)** for the broader context.

---

### Cross‑References

* **External:** [Subscrypts Homepage](https://subscrypts.com) · [Subscrypts MiCAR Whitepaper](https://subscrypts.com/whitepaper) · [Subscrypts dApp](https://app.subscrypts.com) · [Discord Bot](https://discord.onsubscrypts.com)
* **Internal:** [05‑Getting Started for Members](05-getting-started-for-members.md) · [06‑Commands Reference](06-commands-reference.md) · [07‑Subscription Synchronization](07-subscription-synchronization.md) · [08‑Security & Trust](08-security-and-trust.md)
