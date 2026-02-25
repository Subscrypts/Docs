---
title: Subscrypts React SDK
description: Official React SDK for Subscrypts decentralized subscriptions on Arbitrum. Hooks, components, and wallet connectors.
status: new
tags:
  - SDK
  - React
  - developer
  - integration
  - hooks
  - components
---

# Subscrypts React SDK

The **`@subscrypts/subscrypts-sdk-react`** package is the official React SDK for the Subscrypts decentralized subscription protocol on Arbitrum One. It provides a complete toolkit of React hooks, pre-built UI components, and a pluggable wallet connector architecture so you can add on-chain subscriptions to any React application in minutes.

**Version:** `1.6.0` | **License:** MIT | **Source:** [GitHub](https://github.com/Subscrypts/subscrypts-sdk-react)

---

## Installation

```bash
npm install @subscrypts/subscrypts-sdk-react ethers react react-dom
```

Or with Yarn / pnpm:

=== "Yarn"

    ```bash
    yarn add @subscrypts/subscrypts-sdk-react ethers react react-dom
    ```

=== "pnpm"

    ```bash
    pnpm add @subscrypts/subscrypts-sdk-react ethers react react-dom
    ```

Import the bundled styles in your app entry point:

```tsx
import '@subscrypts/subscrypts-sdk-react/styles';
```

### Peer Dependencies

| Package | Version |
|---|---|
| `react` | `^18.0.0 \|\| ^19.0.0` |
| `react-dom` | `^18.0.0 \|\| ^19.0.0` |
| `ethers` | `^6.0.0` |

The SDK has **zero runtime dependencies** beyond these peer dependencies.

---

## Feature Matrix

| Feature | Category | Since |
|---|---|---|
| `SubscryptsProvider` | Context / Setup | v1.0.0 |
| `useSubscriptionStatus` | Hook | v1.0.0 |
| `useSubscribe` | Hook | v1.0.0 |
| `useTokenBalance` | Hook | v1.0.0 |
| `useWallet` | Hook | v1.0.0 |
| `usePlan` / `usePlans` | Hook | v1.0.0 |
| `SubscriptionGuard` | Component | v1.0.0 |
| `CheckoutWizard` | Component | v1.0.0 |
| `PlanCard` / `PricingTable` | Component | v1.0.0 |
| `SubscryptsButton` | Component | v1.0.0 |
| `InjectedConnector` | Wallet | v1.1.0 |
| `useSUBSPrice` / `usePlanPrice` | Hook | v1.2.0 |
| `useManageSubscription` | Hook | v1.2.0 |
| `usePlansByMerchant` | Hook | v1.2.0 |
| `ManageSubscriptionModal` | Component | v1.2.0 |
| `useMySubscriptions` | Hook | v1.3.0 |
| `useSubscryptsEvents` | Hook | v1.3.0 |
| `SubscriptionCard` / `SubscriptionDashboard` | Component | v1.3.0 |
| `useMerchantPlans` / `useMerchantSubscribers` / `useMerchantRevenue` | Hook | v1.4.0 |
| `MerchantDashboard` | Component | v1.4.0 |
| Built-in query caching (LRU) | Provider | v1.5.0 |
| Session persistence | Wallet | v1.5.0 |

---

## Architecture Overview

The SDK follows a layered **Provider -- Hooks -- Components** architecture:

```
SubscryptsProvider          <-- Wallet + Contract + Cache context
    |
    +-- Hooks (headless)    <-- useSubscriptionStatus, useSubscribe, usePlan, ...
    |       |
    |       +-- Components  <-- SubscriptionGuard, CheckoutWizard, PricingTable, ...
    |
    +-- Wallet Connectors   <-- InjectedConnector, ExternalConnector, custom
```

### Provider Layer

[`SubscryptsProvider`](provider-setup.md) is the root context component. It initializes the ethers.js provider, wallet connection, smart contract instances, token balances, and the query cache. Every hook and component requires this provider as an ancestor.

### Hooks Layer (Headless API)

[Hooks](hooks-reference.md) are the primary API for developers who want full control over their UI. Each hook encapsulates a single responsibility -- checking subscription status, executing a purchase, fetching plans, listening to events, etc. All hooks return typed state objects and are fully tree-shakeable.

### Components Layer

[Pre-built components](components-reference.md) are ready-to-use UI widgets that compose hooks internally. Drop in a `<PricingTable>` or `<SubscriptionDashboard>` and get a working UI in seconds. All components use CSS class names prefixed with `subscrypts-` and can be styled via the bundled stylesheet or overridden.

### Wallet Connector Layer

The [wallet connector architecture](wallet-connectors.md) provides a pluggable interface for wallet providers. Use the built-in `InjectedConnector` for MetaMask, pass an external Wagmi/RainbowKit provider, or implement the `WalletConnector` interface for Privy, Web3Auth, or any custom solution.

---

## Supported Wallet Modes

The SDK supports three wallet connection patterns:

| Mode | Use Case | Config |
|---|---|---|
| **Internal** (default) | Auto-detect MetaMask / browser wallet | `enableWalletManagement={true}` |
| **External** | Wagmi, RainbowKit, or other provider | `externalProvider={{ provider, signer, address }}` |
| **Custom connectors** | Privy, Web3Auth, multi-wallet | `connectors={[new InjectedConnector(), myConnector]}` |

See [Provider Setup](provider-setup.md) for detailed configuration examples.

---

## Import Paths

The SDK exposes three entry points:

```tsx
// Main entry -- hooks, components, types, utilities
import { useSubscriptionStatus, SubscriptionGuard } from '@subscrypts/subscrypts-sdk-react';

// Hooks only (tree-shakeable)
import { useSubscribe } from '@subscrypts/subscrypts-sdk-react/hooks';

// Components only (tree-shakeable)
import { PricingTable } from '@subscrypts/subscrypts-sdk-react/components';

// Styles (CSS)
import '@subscrypts/subscrypts-sdk-react/styles';
```

---

## Quick Links

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Quick Start**

    ---

    Build your first integration in 5 minutes.

    [:octicons-arrow-right-24: Quick Start](quick-start.md)

-   :material-cog:{ .lg .middle } **Provider Setup**

    ---

    Configure `SubscryptsProvider` for your wallet mode.

    [:octicons-arrow-right-24: Provider Setup](provider-setup.md)

-   :material-hook:{ .lg .middle } **Hooks Reference**

    ---

    Complete API reference for all 15 hooks.

    [:octicons-arrow-right-24: Hooks Reference](hooks-reference.md)

-   :material-puzzle:{ .lg .middle } **Components Reference**

    ---

    Props, examples, and usage for all UI components.

    [:octicons-arrow-right-24: Components Reference](components-reference.md)

-   :material-wallet:{ .lg .middle } **Wallet Connectors**

    ---

    Built-in connectors and how to build custom ones.

    [:octicons-arrow-right-24: Wallet Connectors](wallet-connectors.md)

-   :material-code-braces:{ .lg .middle } **Code Examples**

    ---

    Copy-paste integration recipes for common use cases.

    [:octicons-arrow-right-24: Code Examples](code-examples.md)

</div>

---

## Related Resources

- [Getting Started for Developers](../getting-started/for-developers.md) -- integration overview including non-SDK paths
- [ABI & Developer Reference](../smart-contract/abi-reference.md) -- raw smart contract interface for direct calls
- [GitHub Repository](https://github.com/Subscrypts/subscrypts-sdk-react) -- source code, issues, and contributions
