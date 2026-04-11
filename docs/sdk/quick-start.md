---
title: SDK Quick Start — Build Your First Integration
description: Add decentralized subscriptions to your React app in 5 minutes with the Subscrypts SDK.
tags:
  - SDK
  - quick-start
  - tutorial
  - React
  - integration
---

# Quick Start -- Build Your First Integration

This guide walks you through adding Subscrypts to a React app in five steps. By the end you will have a working subscription gate that checks on-chain status and shows or hides content accordingly.

**Time required:** ~5 minutes

**Prerequisites:**

- A React 18+ or 19+ project (Vite, Next.js, CRA, etc.)
- Node.js 18+
- A browser with MetaMask installed (or any injected Ethereum wallet)

---

## Step 1 -- Install the SDK

```bash
npm install @subscrypts/subscrypts-sdk-react ethers
```

!!! info "Peer dependencies"
    The SDK requires `react >= 18`, `react-dom >= 18`, and `ethers >= 6` as peer dependencies. If your project already has them installed, you only need the SDK package itself.

---

## Step 2 -- Wrap Your App in `SubscryptsProvider`

The provider initializes the wallet connection, smart contract instances, and query cache. Place it at the root of your component tree.

```tsx title="src/App.tsx"
import { SubscryptsProvider } from '@subscrypts/subscrypts-sdk-react';
import '@subscrypts/subscrypts-sdk-react/styles';
import { Dashboard } from './Dashboard';

function App() {
  return (
    <SubscryptsProvider enableWalletManagement={true}>
      <Dashboard />
    </SubscryptsProvider>
  );
}

export default App;
```

`enableWalletManagement={true}` (the default) lets the SDK manage the MetaMask connection for you. For Wagmi/RainbowKit setups, see [Provider Setup](provider-setup.md).

---

## Step 3 -- Check Subscription Status with `useSubscriptionStatus`

Use the `useSubscriptionStatus` hook to query whether the connected wallet has an active subscription to a specific plan.

```tsx title="src/Dashboard.tsx"
import { useSubscriptionStatus, useWallet } from '@subscrypts/subscrypts-sdk-react';

export function Dashboard() {
  const { isConnected, connect } = useWallet();
  const { status, isLoading, error } = useSubscriptionStatus('1'); // (1)!

  if (!isConnected) {
    return (
      <div>
        <h1>Welcome</h1>
        <p>Connect your wallet to check your subscription.</p>
        <button onClick={connect}>Connect Wallet</button>
      </div>
    );
  }

  if (isLoading) return <p>Checking subscription...</p>;
  if (error) return <p>Error: {error.message}</p>;

  if (!status?.isActive) {
    return (
      <div>
        <h1>No Active Subscription</h1>
        <p>Subscribe to Plan 1 to access premium content.</p>
      </div>
    );
  }

  return (
    <div>
      <h1>Premium Content</h1>
      <p>Your subscription is active until {status.expirationDate?.toLocaleDateString()}.</p>
      <p>Auto-renewing: {status.isAutoRenewing ? 'Yes' : 'No'}</p>
    </div>
  );
}
```

1. Replace `'1'` with your actual plan ID from the Subscrypts smart contract.

!!! tip "Plan IDs"
    Plan IDs are assigned sequentially when a merchant creates plans on-chain. You can find your plan IDs in the [Subscrypts dApp](https://app.subscrypts.com) or by querying the smart contract directly. See [ABI Reference](../smart-contract/abi-reference.md) for details.

---

## Step 4 -- Gate Content with `SubscriptionGuard`

For a declarative approach, use the `SubscriptionGuard` component. It automatically checks subscription status and renders children only if the wallet has an active subscription.

```tsx title="src/App.tsx"
import { SubscryptsProvider, SubscriptionGuard } from '@subscrypts/subscrypts-sdk-react';
import '@subscrypts/subscrypts-sdk-react/styles';

function App() {
  return (
    <SubscryptsProvider enableWalletManagement={true}>
      <h1>My App</h1>

      {/* Public content -- always visible */}
      <p>Welcome to our platform.</p>

      {/* Protected content -- subscription required */}
      <SubscriptionGuard
        planId="1"
        fallbackUrl="/subscribe"
      >
        <PremiumDashboard />
      </SubscriptionGuard>
    </SubscryptsProvider>
  );
}

function PremiumDashboard() {
  return <h2>You have access to premium features.</h2>;
}

export default App;
```

**What happens:**

- While checking: shows a loading spinner (customizable via `loadingComponent`).
- If active: renders `<PremiumDashboard />`.
- If not active: redirects to `/subscribe` (or renders nothing if no `fallbackUrl`).

You can also gate on multiple plans:

```tsx
{/* User needs ANY of these plans */}
<SubscriptionGuard planIds={['1', '2', '3']}>
  <PremiumContent />
</SubscriptionGuard>

{/* User needs ALL of these plans */}
<SubscriptionGuard planIds={['1', '2']} requireAll>
  <BundleContent />
</SubscriptionGuard>
```

---

## Step 5 -- Add a Subscribe Button

Let users purchase a subscription directly from your app with the `SubscryptsButton` component. It opens a full checkout wizard modal with payment method selection, cycle configuration, and transaction handling.

```tsx title="src/SubscribePage.tsx"
import { SubscryptsButton } from '@subscrypts/subscrypts-sdk-react';

export function SubscribePage() {
  return (
    <div>
      <h1>Subscribe</h1>
      <p>Get access to premium features.</p>

      <SubscryptsButton
        planId="1"
        variant="primary"
        size="lg"
        onSuccess={(subscriptionId) => {
          console.log('Subscribed! ID:', subscriptionId);
          window.location.href = '/dashboard';
        }}
      >
        Subscribe Now
      </SubscryptsButton>
    </div>
  );
}
```

The button handles wallet connection, network switching, token approval, and the subscription transaction -- all in a guided multi-step modal.

---

## Complete Working Example

Here is the full minimal app combining all steps:

```tsx title="src/App.tsx"
import {
  SubscryptsProvider,
  SubscriptionGuard,
  SubscryptsButton,
  useWallet,
  useSubscriptionStatus
} from '@subscrypts/subscrypts-sdk-react';
import '@subscrypts/subscrypts-sdk-react/styles';

function App() {
  return (
    <SubscryptsProvider enableWalletManagement={true}>
      <AppContent />
    </SubscryptsProvider>
  );
}

function AppContent() {
  const { isConnected, address, connect, disconnect } = useWallet();
  const { status, isLoading } = useSubscriptionStatus('1');

  return (
    <div style={{ padding: '2rem', maxWidth: '600px', margin: '0 auto' }}>
      <h1>Subscrypts Demo</h1>

      {/* Wallet connection */}
      {!isConnected ? (
        <button onClick={connect}>Connect Wallet</button>
      ) : (
        <p>
          Connected: {address?.slice(0, 6)}...{address?.slice(-4)}{' '}
          <button onClick={disconnect}>Disconnect</button>
        </p>
      )}

      {/* Subscription status */}
      {isConnected && (
        <>
          {isLoading ? (
            <p>Checking subscription...</p>
          ) : status?.isActive ? (
            <div>
              <h2>Premium Content</h2>
              <p>Active until {status.expirationDate?.toLocaleDateString()}</p>
            </div>
          ) : (
            <div>
              <h2>Subscribe to Access Premium</h2>
              <SubscryptsButton
                planId="1"
                variant="primary"
                size="lg"
                onSuccess={() => window.location.reload()}
              >
                Subscribe Now
              </SubscryptsButton>
            </div>
          )}
        </>
      )}
    </div>
  );
}

export default App;
```

---

## Next Steps

- [Provider Setup](provider-setup.md) -- configure wallet modes, caching, and debug logging
- [Hooks Reference](hooks-reference.md) -- explore all 15 hooks for headless integration
- [Components Reference](components-reference.md) -- drop-in UI widgets
- [Code Examples](code-examples.md) -- copy-paste recipes for common patterns
