---
title: Getting Started for Developers — Subscrypts Integration Guide
description: Integrate Subscrypts into your application using the React SDK, ABI calls, or smart contract events on Arbitrum One.
tags:
  - developer
  - getting-started
  - SDK
  - integration
  - ABI
  - subscrypts
---

# Getting Started for Developers

Subscrypts offers three integration paths, from drop-in React components to raw ABI calls. Choose the one that fits your stack.

---

## Network & Contract Details

| Parameter | Value |
|---|---|
| **Network** | Arbitrum One (Chain ID `42161`) |
| **RPC** | `https://arb1.arbitrum.io/rpc` |
| **Block Explorer** | [arbiscan.io](https://arbiscan.io) |
| **Subscrypts Proxy** | [`0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac`](https://arbiscan.io/address/0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac) |
| **SUBS Token** | [`0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac`](https://arbiscan.io/address/0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac) (same as proxy) |
| **USDC** | [`0xaf88d065e77c8cC2239327C5EDb3A432268e5831`](https://arbiscan.io/address/0xaf88d065e77c8cC2239327C5EDb3A432268e5831) |
| **ABI Download** | [subscryptsABI-v1.json](https://files.subscrypts.com/abi/subscryptsABI-v1.json) |

!!! tip "Full address registry"
    See [Deployment & Network Information](../smart-contract/deployment.md) for the complete contract address registry including all facets, vesting, and DEX addresses.

---

## Path A: React SDK (Recommended)

The fastest way to add subscriptions to a React app. The SDK provides hooks, components, and wallet connectors out of the box.

### Install

```bash
npm install @subscrypts/subscrypts-sdk-react ethers
```

### Wrap Your App

```tsx title="App.tsx"
import { SubscryptsProvider } from '@subscrypts/subscrypts-sdk-react';

function App() {
  return (
    <SubscryptsProvider>
      <YourApp />
    </SubscryptsProvider>
  );
}
```

### Check Subscription Status

```tsx title="PremiumContent.tsx"
import { useSubscriptionStatus } from '@subscrypts/subscrypts-sdk-react';

function PremiumContent({ planId }: { planId: string }) {
  const { isActive, isLoading } = useSubscriptionStatus(planId);

  if (isLoading) return <p>Checking subscription...</p>;
  if (!isActive) return <p>Subscribe to access this content.</p>;

  return <div>Welcome, premium member!</div>;
}
```

### Gate Content with a Component

```tsx title="Paywall.tsx"
import { SubscriptionGuard } from '@subscrypts/subscrypts-sdk-react';

function App() {
  return (
    <SubscriptionGuard planId="42" fallbackUrl="/subscribe">
      <PremiumDashboard />
    </SubscriptionGuard>
  );
}
```

For the complete SDK reference, see the [SDK Documentation](../sdk/index.md).

---

## Path B: Direct ABI + ethers.js

For non-React apps or when you need full control.

### Setup

```javascript title="setup.js"
import { ethers } from 'ethers';
import subscryptsAbi from './subscryptsABI-v1.json';

const provider = new ethers.JsonRpcProvider('https://arb1.arbitrum.io/rpc');
const contractAddress = '0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac';
const subscrypts = new ethers.Contract(contractAddress, subscryptsAbi, provider);
```

### Read Plans

```javascript title="read-plans.js"
const plans = await subscrypts.getPlans(0n, 10n);

for (const plan of plans) {
  console.log(`Plan ${plan.id}: ${plan.subscriptionAmount} per ${plan.paymentFrequency}s`);
}
```

### Check a Subscription

```javascript title="check-subscription.js"
const sub = await subscrypts.getPlanSubscription(planId, subscriberAddress);

const isActive = sub.nextPaymentDate > BigInt(Math.floor(Date.now() / 1000));
console.log(`Subscription active: ${isActive}`);
```

### Create a Subscription (with signer)

```javascript title="subscribe.js"
const signer = new ethers.Wallet(privateKey, provider);
const contract = subscrypts.connect(signer);

const tx = await contract.subscriptionCreate(planId);
const receipt = await tx.wait();

console.log(`Subscribed! TX: ${receipt.hash}`);
```

For the full ABI reference, see [ABI & Developer Reference](../smart-contract/abi-reference.md).

---

## Path C: Event Listening (Backend Integration)

Listen for on-chain events to automate access control, notifications, or fulfillment in your backend.

### Key Events

| Event | When It Fires |
|---|---|
| `_subscriptionCreate` | New subscription created |
| `_subscriptionPay` | Payment processed (initial or renewal) |
| `_subscriptionStop` | Subscription expired or failed renewal |
| `_subscriptionRecurring` | Auto-renewal toggled on/off |
| `_planCreate` | New plan created |

### Listen for Payments

```javascript title="event-listener.js"
subscrypts.on('_subscriptionPay', (subscriptionId, planId, subscriber, amount) => {
  console.log(`Payment: sub=${subscriptionId}, plan=${planId}, from=${subscriber}, amount=${amount}`);

  // Grant access, send notification, update database, etc.
});
```

### Listen for Expirations

```javascript title="expiry-listener.js"
subscrypts.on('_subscriptionStop', (subscriptionId, merchant, planId, subscriber) => {
  console.log(`Expired: sub=${subscriptionId}, subscriber=${subscriber}`);

  // Revoke access, send reminder, etc.
});
```

---

## Quick Reference: Key Functions

### Read-Only (no gas, no signer)

| Function | Returns |
|---|---|
| `getPlans(start, end)` | Array of Plan structs |
| `getPlan(planId)` | Single Plan struct |
| `getSubscription(subId)` | Single Subscription struct |
| `getPlanSubscription(planId, subscriber)` | Subscription for a specific user on a plan |
| `getSubscriptionsByAddress(address, start, end)` | All subscriptions for a wallet |
| `getSubscriptionsByPlan(planId, start, end)` | All subscriptions for a plan |

### Write Operations (requires signer)

| Function | Purpose |
|---|---|
| `planCreate(currency, amount, frequency, description, attributes, referralBonus)` | Create a new subscription plan (costs ETH) |
| `subscriptionCreate(planId, ...)` | Subscribe to a plan (burns SUBS) |
| `subscriptionRecurringCHG(subId, enabled, cycles)` | Toggle auto-renewal |
| `subscriptionGift(planId, subscriber, ...)` | Gift a subscription |
| `paySubscriptionWithUsdc(planId, ...)` | Pay with USDC (Permit2 + Uniswap swap) |

For full function signatures and parameters, see the [ABI Reference](../smart-contract/abi-reference.md).

---

## Ecosystem Integrations

The same on-chain events and view functions that power your custom integration also power the Subscrypts ecosystem tools:

* **[Discord Bot](../discord-bot/introduction.md)** — Listens to `_subscriptionPay` and `_subscriptionStop` to manage Discord role access
* **[Telegram Bot](../telegram-bot/introduction.md)** — Uses the same events for Telegram group membership enforcement
* **[Subscrypts Pulse](../pulse/introduction.md)** — Monitors subscription state and sends push notifications to subscribers

All ecosystem integrations are cross-platform: a subscription created via the SDK or ABI can be verified and enforced by the Discord Bot, Telegram Bot, Pulse, and any other service reading on-chain state.

---

## What's Next?

<div class="grid cards" markdown>

-   [:octicons-arrow-right-24: **SDK Quick Start**](../sdk/quick-start.md) — Full React integration tutorial

-   [:octicons-arrow-right-24: **ABI Reference**](../smart-contract/abi-reference.md) — Complete function and event reference

-   [:octicons-arrow-right-24: **Core Logic**](../smart-contract/core-logic.md) — How subscription lifecycle works on-chain

-   [:octicons-arrow-right-24: **Code Examples**](../sdk/code-examples.md) — Paywall, dashboard, and event recipes

</div>
