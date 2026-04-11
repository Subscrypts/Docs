---
title: SDK Components Reference
description: Complete reference for all Subscrypts React SDK UI components with props, types, and usage examples.
tags:
  - sdk
  - components
  - react
  - subscrypts
---

# SDK Components Reference

The Subscrypts SDK exports pre-built React components for common subscription workflows. All components require `SubscryptsProvider` as an ancestor and ship with default styling via `@subscrypts/subscrypts-sdk-react/styles`.

```tsx
import {
  SubscriptionGuard,
  CheckoutWizard,
  SubscriptionCard,
  SubscriptionDashboard,
  ManageSubscriptionModal,
  PlanCard,
  PricingTable,
  SubscryptsButton,
  ConnectWalletModal,
  MerchantDashboard,
  LoadingSpinner,
  Modal,
  ErrorDisplay,
  NetworkSwitchPrompt,
  SubscryptsErrorBoundary
} from '@subscrypts/subscrypts-sdk-react';
```

---

## Access Control

### SubscriptionGuard

Gate content behind an active subscription. Supports single-plan and multi-plan access checks. When the connected wallet does not have an active subscription, the guard either redirects to `fallbackUrl`, fires `onAccessDenied`, or renders nothing.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `planId` | `string` | -- | Single plan ID to check (backward-compatible mode) |
| `planIds` | `string[]` | -- | Multiple plan IDs to check |
| `requireAll` | `boolean` | `false` | When `true`, the user must be subscribed to **all** plans in `planIds`. When `false`, any single active plan grants access. Only applies when `planIds` is provided. |
| `fallbackUrl` | `string` | -- | URL to redirect to when access is denied |
| `loadingComponent` | `ReactNode` | `<LoadingSpinner />` | Custom loading UI shown while subscription status is being fetched |
| `children` | `ReactNode` | -- | **Required.** Protected content rendered when access is granted |
| `onAccessDenied` | `() => void` | -- | Callback fired when the subscription check completes and the user does not have access |

#### TypeScript Interface

```typescript
interface SubscriptionGuardProps {
  planId?: string;
  planIds?: string[];
  requireAll?: boolean;
  fallbackUrl?: string;
  loadingComponent?: ReactNode;
  children: ReactNode;
  onAccessDenied?: () => void;
}
```

#### Examples

```tsx title="Single plan gate"
<SubscriptionGuard planId="1" fallbackUrl="/subscribe">
  <PremiumContent />
</SubscriptionGuard>
```

```tsx title="Multi-plan: any of these plans grants access"
<SubscriptionGuard planIds={['1', '2', '3']}>
  <PremiumContent />
</SubscriptionGuard>
```

```tsx title="Multi-plan: require ALL plans (bundle gate)"
<SubscriptionGuard planIds={['1', '2']} requireAll>
  <BundleContent />
</SubscriptionGuard>
```

```tsx title="Custom loading and access-denied handling"
<SubscriptionGuard
  planId="5"
  loadingComponent={<MySkeletonLoader />}
  onAccessDenied={() => analytics.track('paywall_hit')}
>
  <ExclusiveArticle />
</SubscriptionGuard>
```

!!! info "How access is determined"
    For single-plan mode (`planId`), the guard uses the `useSubscriptionStatus` hook. For multi-plan mode (`planIds`), it queries the smart contract directly for each plan and aggregates results based on the `requireAll` flag.

---

## Checkout

### CheckoutWizard

Multi-step subscription checkout flow presented inside a modal. The wizard guides the user through configuration (cycle limit, auto-renewal, payment method) and transaction execution. Supports both SUBS and USDC payment methods.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `planId` | `string` | -- | **Required.** Plan ID to subscribe to |
| `isOpen` | `boolean` | -- | **Required.** Controls modal visibility |
| `onClose` | `() => void` | -- | **Required.** Called when the modal is closed |
| `referralAddress` | `string` | -- | Optional referrer wallet address for referral bonus |
| `onSuccess` | `(subscriptionId: string) => void` | -- | Called after a successful subscription with the new subscription ID |
| `onError` | `(error: Error) => void` | -- | Called when the subscription transaction fails |

#### TypeScript Interface

```typescript
interface CheckoutWizardProps {
  planId: string;
  isOpen: boolean;
  onClose: () => void;
  referralAddress?: string;
  onSuccess?: (subscriptionId: string) => void;
  onError?: (error: Error) => void;
}
```

#### Example

```tsx title="CheckoutWizard with callbacks"
import { useState } from 'react';
import { CheckoutWizard } from '@subscrypts/subscrypts-sdk-react';

function SubscribePage() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <button onClick={() => setIsOpen(true)}>Subscribe to Plan #1</button>

      <CheckoutWizard
        planId="1"
        isOpen={isOpen}
        onClose={() => setIsOpen(false)}
        onSuccess={(subId) => {
          console.log('Subscribed! ID:', subId);
          setIsOpen(false);
        }}
        onError={(err) => console.error('Subscription failed:', err)}
      />
    </>
  );
}
```

!!! tip "Payment methods"
    The `CheckoutWizard` internally manages payment method selection. Users can choose between SUBS (native token) and USDC. USDC payments use Uniswap v3 for on-chain conversion and Permit2 for gasless approvals.

### SubscryptsButton

Pre-styled CTA button with a built-in `CheckoutWizard`. Clicking the button opens the checkout flow in a modal. If the wallet is not connected, it triggers wallet connection first.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `planId` | `string` | -- | **Required.** Plan ID to subscribe to |
| `variant` | `'primary' \| 'secondary' \| 'outline'` | `'primary'` | Button style variant |
| `size` | `'sm' \| 'md' \| 'lg'` | `'md'` | Button size |
| `children` | `ReactNode` | `'Subscribe'` | Button label |
| `referralAddress` | `string` | -- | Optional referrer wallet address |
| `onSuccess` | `(subscriptionId: string) => void` | -- | Called after successful subscription |

#### TypeScript Interface

```typescript
interface SubscryptsButtonProps {
  planId: string;
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'sm' | 'md' | 'lg';
  children?: ReactNode;
  referralAddress?: string;
  onSuccess?: (subscriptionId: string) => void;
}
```

#### Example

```tsx title="Subscribe button with custom label"
<SubscryptsButton
  planId="1"
  variant="primary"
  size="lg"
  onSuccess={(subId) => navigate('/dashboard')}
>
  Subscribe Now
</SubscryptsButton>
```

---

## Subscription Management

### SubscriptionCard

Displays a single subscription with a status badge, payment amount, frequency, and an optional manage button. Clicking "Manage" opens a `ManageSubscriptionModal` by default.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `subscription` | `Subscription` | -- | **Required.** Subscription data object |
| `showManageButton` | `boolean` | `true` | Show or hide the manage button |
| `showFiatPrice` | `boolean` | `false` | Display fiat price alongside SUBS amount |
| `onManage` | `(subscriptionId: string) => void` | -- | Custom manage handler (overrides the default modal) |
| `onCancelled` | `() => void` | -- | Called when the subscription is cancelled via the manage modal |
| `onUpdated` | `() => void` | -- | Called when the subscription is updated via the manage modal |
| `className` | `string` | `''` | Additional CSS class name |

#### TypeScript Interface

```typescript
interface SubscriptionCardProps {
  subscription: Subscription;
  showManageButton?: boolean;
  showFiatPrice?: boolean;
  onManage?: (subscriptionId: string) => void;
  onCancelled?: () => void;
  onUpdated?: () => void;
  className?: string;
}
```

#### Example

```tsx title="Subscription card with callbacks"
<SubscriptionCard
  subscription={subscription}
  showManageButton={true}
  onCancelled={() => refetchSubscriptions()}
  onUpdated={() => refetchSubscriptions()}
/>
```

!!! info "Status badges"
    The card automatically resolves subscription status and renders one of four badge variants: **Active**, **Expiring Soon**, **Expired**, or **Cancelled**.

### SubscriptionDashboard

Full subscription management dashboard that fetches and displays all subscriptions for the connected wallet (or a specified address). Includes pagination, loading states, empty states, and error handling.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `address` | `string` | Connected wallet | Wallet address to fetch subscriptions for |
| `pageSize` | `number` | `10` | Number of subscriptions per page |
| `showFiatPrices` | `boolean` | `false` | Show fiat prices on subscription cards |
| `emptyComponent` | `ReactNode` | Default empty state | Custom component shown when no subscriptions exist |
| `loadingComponent` | `ReactNode` | `<LoadingSpinner />` | Custom loading component |
| `className` | `string` | `''` | Additional CSS class name |
| `onSubscriptionCancelled` | `(subscriptionId: string) => void` | -- | Called when any subscription is cancelled |
| `onSubscriptionUpdated` | `(subscriptionId: string) => void` | -- | Called when any subscription is updated |

#### TypeScript Interface

```typescript
interface SubscriptionDashboardProps {
  address?: string;
  pageSize?: number;
  showFiatPrices?: boolean;
  emptyComponent?: React.ReactNode;
  loadingComponent?: React.ReactNode;
  className?: string;
  onSubscriptionCancelled?: (subscriptionId: string) => void;
  onSubscriptionUpdated?: (subscriptionId: string) => void;
}
```

#### Example

```tsx title="Dashboard with custom page size"
<SubscriptionDashboard
  pageSize={10}
  showFiatPrices={true}
  onSubscriptionCancelled={(id) => console.log('Cancelled:', id)}
/>
```

### ManageSubscriptionModal

Modal for managing an existing subscription. Provides actions for cancelling, toggling auto-renewal, and updating payment cycles. Includes a confirmation dialog for destructive actions.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `isOpen` | `boolean` | -- | **Required.** Controls modal visibility |
| `onClose` | `() => void` | -- | **Required.** Close handler |
| `subscriptionId` | `string` | -- | **Required.** Subscription ID to manage |
| `subscription` | `Subscription` | -- | Pre-loaded subscription data (skips additional contract fetch) |
| `onCancelled` | `() => void` | -- | Called when the subscription is cancelled |
| `onUpdated` | `() => void` | -- | Called when the subscription is updated |

#### TypeScript Interface

```typescript
interface ManageSubscriptionModalProps {
  isOpen: boolean;
  onClose: () => void;
  subscriptionId: string;
  subscription?: Subscription;
  onCancelled?: () => void;
  onUpdated?: () => void;
}
```

#### Example

```tsx title="Manage subscription modal"
<ManageSubscriptionModal
  isOpen={showManage}
  onClose={() => setShowManage(false)}
  subscriptionId="42"
  subscription={subscriptionData}
  onCancelled={() => {
    setShowManage(false);
    refetchSubscriptions();
  }}
  onUpdated={() => refetchSubscriptions()}
/>
```

---

## Plan Display

### PlanCard

Displays a single subscription plan with configurable fields and a subscribe CTA. Supports featured highlighting and custom field selection.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `plan` | `Plan` | -- | **Required.** Plan data from the smart contract |
| `currency` | `'SUBS' \| 'USDC'` | `'SUBS'` | Currency for price display |
| `showFields` | `PlanField[]` | `['description', 'amount', 'frequency']` | Fields to display on the card |
| `onSubscribe` | `(planId: string) => void` | -- | Called when the subscribe button is clicked |
| `subscribeLabel` | `string` | `'Subscribe'` | Custom label for the subscribe button |
| `className` | `string` | `''` | Additional CSS class name |
| `showSubscribeButton` | `boolean` | `true` | Show or hide the subscribe button |
| `featured` | `boolean` | `false` | Highlight the card as a featured plan |
| `title` | `string` | -- | Custom card title (overrides `plan.description`) |

#### Available PlanField Values

```typescript
type PlanField =
  | 'description'
  | 'amount'
  | 'frequency'
  | 'subscribers'
  | 'merchant'
  | 'referralBonus'
  | 'attributes';
```

#### TypeScript Interface

```typescript
interface PlanCardProps {
  plan: Plan;
  currency?: 'SUBS' | 'USDC';
  showFields?: PlanField[];
  onSubscribe?: (planId: string) => void;
  subscribeLabel?: string;
  className?: string;
  showSubscribeButton?: boolean;
  featured?: boolean;
  title?: string;
}
```

#### Example

```tsx title="Featured plan card with custom fields"
<PlanCard
  plan={plan}
  currency="SUBS"
  showFields={['description', 'amount', 'frequency', 'subscribers']}
  onSubscribe={(planId) => openCheckout(planId)}
  subscribeLabel="Get Started"
  featured={true}
  title="Pro Plan"
/>
```

### PricingTable

Displays multiple plans in a responsive grid layout. Fetches plan data from the smart contract and renders each plan as a `PlanCard`. Includes a built-in `CheckoutWizard` that opens when a user clicks "Subscribe" on any plan.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `plans` | `(string \| PlanConfig)[]` | -- | **Required.** Array of plan IDs or plan configurations |
| `currency` | `'SUBS' \| 'USDC'` | `'SUBS'` | Currency for price display |
| `showFields` | `PlanField[]` | `['description', 'amount', 'frequency']` | Fields to display on each plan card |
| `columns` | `1 \| 2 \| 3 \| 4` | Auto | Number of grid columns (auto-calculated from plan count) |
| `onSubscribe` | `(planId: string) => void` | -- | Custom subscribe handler (overrides built-in checkout) |
| `subscribeLabel` | `string` | `'Subscribe'` | Default subscribe button label |
| `className` | `string` | `''` | Additional CSS class name |
| `onSubscriptionSuccess` | `(subscriptionId: string, planId: string) => void` | -- | Called after successful subscription |
| `onSubscriptionError` | `(error: Error, planId: string) => void` | -- | Called when subscription fails |
| `referralAddress` | `string` | -- | Referral address passed to the checkout wizard |
| `loadingComponent` | `ReactNode` | Default spinner | Custom loading UI |
| `errorComponent` | `ReactNode` | Default error message | Custom error UI |

#### PlanConfig Type

```typescript
interface PlanConfig {
  planId: string;
  title?: string;
  featured?: boolean;
  subscribeLabel?: string;
}
```

#### TypeScript Interface

```typescript
interface PricingTableProps {
  plans: (string | PlanConfig)[];
  currency?: 'SUBS' | 'USDC';
  showFields?: PlanField[];
  columns?: 1 | 2 | 3 | 4;
  onSubscribe?: (planId: string) => void;
  subscribeLabel?: string;
  className?: string;
  onSubscriptionSuccess?: (subscriptionId: string, planId: string) => void;
  onSubscriptionError?: (error: Error, planId: string) => void;
  referralAddress?: string;
  loadingComponent?: React.ReactNode;
  errorComponent?: React.ReactNode;
}
```

#### Examples

```tsx title="Simple pricing table with plan IDs"
<PricingTable
  plans={['1', '2', '3']}
  currency="SUBS"
  showFields={['description', 'amount', 'frequency', 'subscribers']}
/>
```

```tsx title="Pricing table with per-plan configuration"
<PricingTable
  plans={[
    { planId: '1', title: 'Basic', subscribeLabel: 'Start Free' },
    { planId: '2', title: 'Pro', featured: true, subscribeLabel: 'Go Pro' },
    { planId: '3', title: 'Enterprise', subscribeLabel: 'Contact Us' }
  ]}
  columns={3}
  onSubscriptionSuccess={(subId, planId) => {
    console.log(`Subscribed to plan ${planId}, subscription ID: ${subId}`);
  }}
/>
```

---

## Wallet

### ConnectWalletModal

Modal that lists all available wallet connectors and handles the connection flow. Automatically filters connectors to show only those that are currently available (e.g., MetaMask is installed).

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `isOpen` | `boolean` | -- | **Required.** Controls modal visibility |
| `onClose` | `() => void` | -- | **Required.** Close handler |
| `connectors` | `WalletConnector[]` | -- | **Required.** Available wallet connectors |
| `onConnect` | `(connectorId: string) => Promise<void>` | -- | **Required.** Called when a connector is selected |
| `className` | `string` | `''` | Additional CSS class name |

#### TypeScript Interface

```typescript
interface ConnectWalletModalProps {
  isOpen: boolean;
  onClose: () => void;
  connectors: WalletConnector[];
  onConnect: (connectorId: string) => Promise<void>;
  className?: string;
}
```

#### Example

```tsx title="Connect wallet modal"
import { ConnectWalletModal, useSubscrypts } from '@subscrypts/subscrypts-sdk-react';

function ConnectButton() {
  const [showModal, setShowModal] = useState(false);
  const { connectors, connectWith } = useSubscrypts();

  return (
    <>
      <button onClick={() => setShowModal(true)}>Connect Wallet</button>

      <ConnectWalletModal
        isOpen={showModal}
        onClose={() => setShowModal(false)}
        connectors={connectors}
        onConnect={async (id) => {
          await connectWith(id);
        }}
      />
    </>
  );
}
```

---

## Merchant

### MerchantDashboard

Complete merchant overview dashboard with revenue metrics (MRR), plan listing, and subscriber details. Uses `useMerchantRevenue`, `useMerchantPlans`, and `useMerchantSubscribers` hooks internally.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `merchantAddress` | `string` | Connected wallet | Merchant address to display dashboard for |
| `className` | `string` | `''` | Additional CSS class name |

#### TypeScript Interface

```typescript
interface MerchantDashboardProps {
  merchantAddress?: string;
  className?: string;
}
```

#### Example

```tsx title="Merchant dashboard (connected wallet)"
import { MerchantDashboard } from '@subscrypts/subscrypts-sdk-react';

function MerchantPage() {
  return <MerchantDashboard />;
}
```

!!! info "Dashboard sections"
    The `MerchantDashboard` renders three sections:

    1. **Revenue Overview** -- Monthly Recurring Revenue (MRR) in SUBS with USD estimate, active subscriber count, and active plan count.
    2. **Your Plans** -- Clickable plan cards showing plan ID, description, status, and subscriber count.
    3. **Subscribers** -- When a plan is selected, shows a paginated list of subscribers with address, renewal status, and remaining cycles.

---

## Utility Components

### LoadingSpinner

Accessible animated loading spinner with ARIA attributes.

```tsx title="Usage"
import { LoadingSpinner } from '@subscrypts/subscrypts-sdk-react';

<LoadingSpinner />
```

The spinner renders with `role="status"` and `aria-label="Loading"` for screen reader support. No props are required.

---

### Modal

Generic modal wrapper with overlay, escape-key dismissal, and body scroll lock. Used internally by `CheckoutWizard`, `ManageSubscriptionModal`, and `ConnectWalletModal`.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `isOpen` | `boolean` | -- | **Required.** Controls visibility |
| `onClose` | `() => void` | -- | **Required.** Called when the modal is dismissed (overlay click or Escape key) |
| `title` | `string` | -- | Optional header title |
| `children` | `ReactNode` | -- | **Required.** Modal body content |
| `size` | `'sm' \| 'md' \| 'lg'` | `'md'` | Modal width |

#### TypeScript Interface

```typescript
interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title?: string;
  children: React.ReactNode;
  size?: 'sm' | 'md' | 'lg';
}
```

#### Example

```tsx title="Custom modal"
<Modal isOpen={isOpen} onClose={() => setIsOpen(false)} title="Confirm Action" size="sm">
  <p>Are you sure you want to proceed?</p>
  <button onClick={handleConfirm}>Confirm</button>
</Modal>
```

---

### ErrorDisplay

Context-aware error display that automatically maps blockchain errors (revert reasons, user rejection, insufficient balance) to human-readable messages. Supports retry and dismiss actions.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `error` | `Error \| null` | -- | **Required.** The error to display (renders nothing if `null`) |
| `onRetry` | `() => void` | -- | Retry callback (only shown if the error is retryable) |
| `onDismiss` | `() => void` | -- | Dismiss callback |
| `compact` | `boolean` | `false` | Compact mode for inline display |
| `className` | `string` | `''` | Additional CSS class name |

#### TypeScript Interface

```typescript
interface ErrorDisplayProps {
  error: Error | null;
  onRetry?: () => void;
  onDismiss?: () => void;
  compact?: boolean;
  className?: string;
}
```

#### Example

```tsx title="Error display with retry"
<ErrorDisplay
  error={subscriptionError}
  onRetry={() => subscribe(params)}
  onDismiss={() => setError(null)}
/>
```

---

### NetworkSwitchPrompt

Warning banner displayed when the user is connected to a network other than Arbitrum One. Provides a one-click "Switch to Arbitrum" button.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `currentChainId` | `number \| null` | -- | **Required.** Current chain ID the user is connected to |
| `onSwitch` | `() => void` | -- | **Required.** Callback to trigger network switch |
| `onDismiss` | `() => void` | -- | Optional dismiss callback |
| `className` | `string` | `''` | Additional CSS class name |

#### TypeScript Interface

```typescript
interface NetworkSwitchPromptProps {
  currentChainId: number | null;
  onSwitch: () => void;
  onDismiss?: () => void;
  className?: string;
}
```

#### Example

```tsx title="Network switch prompt"
import { NetworkSwitchPrompt, useWallet } from '@subscrypts/subscrypts-sdk-react';

function NetworkBanner() {
  const { walletState, switchNetwork } = useWallet();

  if (!walletState.chainId || walletState.chainId === 42161) return null;

  return (
    <NetworkSwitchPrompt
      currentChainId={walletState.chainId}
      onSwitch={() => switchNetwork(42161)}
    />
  );
}
```

---

### SubscryptsErrorBoundary

React error boundary wrapper for Subscrypts SDK components. Catches rendering errors in child components and displays a fallback UI with a "Try Again" button.

#### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `children` | `ReactNode` | -- | **Required.** Child components to wrap |
| `fallback` | `ReactNode \| ((error: Error, resetError: () => void) => ReactNode)` | Default error UI | Custom fallback UI. Can be a static element or a render function receiving the error and a reset callback. |
| `onError` | `(error: Error, errorInfo: ErrorInfo) => void` | -- | Callback when an error is caught (useful for analytics/logging) |

#### TypeScript Interface

```typescript
interface SubscryptsErrorBoundaryProps {
  children: ReactNode;
  fallback?: ReactNode | ((error: Error, resetError: () => void) => ReactNode);
  onError?: (error: Error, errorInfo: ErrorInfo) => void;
}
```

#### Example

```tsx title="Error boundary with custom fallback"
<SubscryptsErrorBoundary
  fallback={(error, reset) => (
    <div>
      <p>Something went wrong: {error.message}</p>
      <button onClick={reset}>Try Again</button>
    </div>
  )}
  onError={(error) => analytics.trackError(error)}
>
  <SubscriptionDashboard />
</SubscryptsErrorBoundary>
```

!!! warning "Class component"
    `SubscryptsErrorBoundary` is a React class component (error boundaries cannot be function components). It exposes `getDerivedStateFromError` and `componentDidCatch` lifecycle methods.

---

## Type Reference

### Subscription

```typescript
interface Subscription {
  id: string;
  merchantAddress: string;
  planId: string;
  subscriber: string;
  currencyCode: bigint;
  subscriptionAmount: bigint;
  paymentFrequency: bigint;
  isAutoRenewing: boolean;
  remainingCycles: number;
  customAttributes: string;
  lastPaymentDate: Date;
  nextPaymentDate: Date;
}
```

### Plan

```typescript
interface Plan {
  id: bigint;
  merchantAddress: string;
  currencyCode: bigint;
  subscriptionAmount: bigint;
  paymentFrequency: bigint;
  referralBonus: bigint;
  commission: bigint;
  description: string;
  defaultAttributes: string;
  verificationExpiryDate: bigint;
  subscriberCount: bigint;
  isActive: boolean;
}
```

### PaymentMethod

```typescript
type PaymentMethod = 'SUBS' | 'USDC';
```
