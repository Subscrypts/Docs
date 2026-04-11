---
title: Telegram Bot Best Practices
description: Recommendations for managing a Subscrypts-enabled Telegram group, migration strategies, and resolving common issues.
status: new
tags:
  - subscrypts
  - telegram
  - best practices
  - telegram admin
  - support
  - troubleshooting
  - migration
---

# Best Practices & Troubleshooting

Whether you're launching a new paid Telegram community or migrating an existing group to subscription-gated access, these tips help ensure a smooth experience for both admins and members.

---

## Admin Best Practices

### Ensure Bot Permissions Are Correct

The bot needs these admin permissions in your group:

* **Invite users** — to send single-use invite links
* **Ban users** — to remove expired members (the bot bans and immediately unbans to revoke access cleanly)
* **Delete messages** — to manage join gate notifications

Run `/admin check` after setup and after any permission changes to verify everything is correct.

---

### Pin Clear Subscribe Instructions

Make it easy for potential subscribers to find your group:

* **Pin the subscribe link** in your group description or as a pinned message.
* Explain briefly what subscribers get access to and how the process works.
* Mention that subscribers will need:
    * An Ethereum wallet (MetaMask recommended)
    * Some ETH on Arbitrum for gas fees
    * SUBS tokens or USDC for the subscription payment

---

### Use Migration Mode for Existing Groups

If your group already has free members, **don't enforce immediately**. Use migration mode to transition gracefully:

1. **Set an appropriate grace period** — 14 days is common for most communities. Larger groups may benefit from 21–30 days.
2. **Communicate clearly before starting** — Post an announcement explaining the transition, why it's happening, and what members need to do.
3. **Upload your member list** — Export members from Telegram Desktop and upload via the bot's export tool for 100% coverage. This ensures the bot knows who is an existing member vs. a new joiner.
4. **Monitor progress** — Use `/admin migrate status` regularly to track how many members have subscribed.
5. **Send personal reminders** — For key community members who haven't subscribed yet, consider reaching out directly.
6. **Adjust if needed** — If too many members are still pending near the deadline, use `/admin migrate adjust <days>` to extend the grace period.
7. **Communicate the deadline** — Post a final reminder a few days before enforcement begins.

!!! tip "Phased Rollout"
    For very large groups, consider starting with a longer grace period (30+ days) and posting weekly progress updates. This gives members ample time while maintaining momentum toward the transition.

---

### Review the Audit Trail Regularly

Use `/admin ledger` to review recent membership actions:

* Check that invites and removals are happening as expected.
* Investigate any unexpected removals — they may indicate a member's subscription expired without their knowledge.
* Use the ledger data to support member inquiries.

---

### Use Multiple Plans Strategically

If your community offers different value propositions:

* Create **separate plans** for different price points or billing cycles (e.g., monthly vs. annual).
* Map all relevant plans to the same group — any active subscription grants access.
* Consider offering a **discounted annual plan** to reduce churn.

---

### Communicate How Billing Works

For transparency and user trust:

* Clearly explain that subscriptions are **non-custodial on-chain transactions**.
* Mention that all payments settle in **SUBS** on Arbitrum (with USDC fallback available for initial payments).
* Let members know that **automatic renewal** requires SUBS balance — encourage them to maintain a small balance.
* Link to the **[Subscrypts MiCAR Whitepaper](https://subscrypts.com/whitepaper)** for broader context if needed.

---

## Member Best Practices

As a member of a Subscrypts-gated Telegram group:

* **Subscribe from the official link** — Only use subscribe links at `telegram.onsubscrypts.com`. Be cautious of links from unknown sources.
* Always check that your wallet is on **Arbitrum One** before subscribing.
* Keep some **ETH on Arbitrum** for gas and enough **SUBS** to cover renewals.
* Use `/status` in a private chat with the bot to check your subscription status across groups.
* If you're removed from a group, check whether your subscription expired — you can resubscribe and rejoin at any time.

---

## Common Troubleshooting Scenarios

### Member Not Receiving Invite Link After Linking

**For members:**

* Wait a moment — the bot needs to verify your on-chain subscription.
* Confirm you subscribed from the **same wallet** you linked.
* Make sure you haven't blocked the bot in Telegram (the invite is sent via DM).
* Try the wallet-link flow again if the link expired.

**For admins:**

* Use `/admin ledger` to check if the bot attempted to send an invite.
* Verify that plans are correctly mapped with `/admin plan`.
* Run `/admin reconcile` to force a sync.

---

### Member Removed from Group Unexpectedly

**For members:**

* Your subscription likely expired. Check with `/status`.
* Resubscribe via the group's subscribe link — your wallet is still linked, so you'll receive a new invite.

**For admins:**

* Check `/admin ledger` to see why the member was removed.
* Common cause: subscription expired between reconciliation cycles.

---

### Bot Not Responding to Commands

* Ensure the bot is still an **admin** in the group.
* Check that you are a **group administrator** (non-admin members can only use commands in private chat with the bot).
* Verify the bot hasn't been removed from the group.
* Run `/admin rpc-health` to check blockchain connectivity.

---

### Migration Mode Issues

**Members not appearing in migration tracking:**

* Upload your member list via the export tool for comprehensive coverage.
* Members who joined after migration started are handled by the join gate, not migration mode.

**Grace period too short:**

* Use `/admin migrate adjust <days>` to extend the deadline.

**Enforcement removed important members:**

* If a member was removed who should have been kept, they can resubscribe and rejoin immediately.
* For VIPs or team members, ensure they have subscribed before ending migration.

---

## When to Contact Support

Consider reaching out through the official [Subscrypts Discord](https://discord.gg/6uYzBUhAj7) if:

* Membership sync issues persist across **many members**, not just one.
* The bot appears to be ignoring valid on-chain subscriptions.
* `/admin check` reports issues that you cannot resolve with the suggested fixes.

---

## Summary Checklist

| For Admins | For Members |
|---|---|
| Ensure the bot has **admin permissions** (invite, ban, delete) | Subscribe only via official links at `telegram.onsubscrypts.com` |
| Pin the **subscribe link** clearly in your group | Keep your wallet on **Arbitrum One** |
| Use **migration mode** for existing groups | Keep some **ETH and SUBS** for gas and renewals |
| Run `/admin check` after setup and changes | Use `/status` to check your subscription status |
| Review `/admin ledger` to audit membership actions | Contact a group admin if removed unexpectedly |
| Use `/admin reconcile` when sync seems delayed | |

!!! ecosystem "Subscrypts Ecosystem"
    Troubleshooting often spans multiple layers. For smart contract behavior, see the [Smart Contract Suite](../smart-contract/introduction.md). For dApp-side issues, see the [Subscrypts dApp](../dapp/introduction.md). The [Subscrypts SDK](../sdk/index.md) provides programmatic tools for advanced debugging.

---

## Related Topics

- [Admin Setup Guide](admin-setup-guide.md) -- Full setup and configuration guidance
- [Member Guide](member-guide.md) -- The subscriber experience from wallet linking to access
- [Commands Reference](commands-reference.md) -- Complete list of admin and member commands
- [Architecture & Integration](architecture.md) -- How the integration works end to end
- [Subscription Synchronization](subscription-sync.md) -- How on-chain state becomes group membership
