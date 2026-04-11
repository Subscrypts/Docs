---
title: SDK Code Examples — Integration Recipes
description: Complete, copy-paste-ready integration recipes for common Subscrypts SDK use cases including paywalls, merchant dashboards, event listeners, and custom wallets.
tags:
  - sdk
  - examples
  - integration
  - react
---

# Code Examples -- Integration Recipes

Complete, copy-paste-ready recipes for common Subscrypts SDK integration patterns. Every example assumes you have installed the SDK and wrapped your app with `SubscryptsProvider`.

```bash
npm install @subscrypts/subscrypts-sdk-react
```

---

## Recipe 1: Paywall Gate

Check subscription status for a specific plan and conditionally render premium content. Free users see a subscribe CTA; active subscribers see the gated content.

```tsx title="PaywallGate.tsx"
import {
  SubscryptsProvider,
  SubscriptionGuard,
  SubscryptsButton,
  useSubscriptionStatus
} from '@subscrypts/subscrypts-sdk-react';
import '@subscrypts/subscrypts-sdk-react/styles';

/**
 * Option A: Declarative guard (recommended)
 *
 * SubscriptionGuard handles loading, access checking, and redirection.
 */
function PremiumArticleGuarded() {
  return (
    <SubscriptionGuard
      planId="1"
      loadingComponent={<ArticleSkeleton />}
      onAccessDenied={() => console.log('User hit paywall')}
    >
      <article>
        <h1>Premium Analysis: DeFi Trends 2026</h1>
        <p>This content is only visible to active subscribers...</p>
      </article>
    </SubscriptionGuard>
  );
}

/**
 * Option B: Hook-based (full control)
 *
 * Use useSubscriptionStatus for custom UI logic.
 */
function PremiumArticleHook() {
  const { status, isLoading, error, refetch } = useSubscriptionStatus('1');

  if (isLoading) {
    return <ArticleSkeleton />;
  }

  if (error) {
    return (
      <div className="error-banner">
        <p>Could not verify subscription: {error.message}</p>
        <button onClick={refetch}>Retry</button>
      </div>
    );
  }

  if (!status?.isActive) {
    return (
      <div className="paywall">
        <h2>Subscribe to unlock this article</h2>
        <p>Get full access to all premium content.</p>

        {status?.subscriptionId && (
          <p className="notice">
            Your subscription expired on{' '}
            {status.expirationDate?.toLocaleDateString()}.
          </p>
        )}

        <SubscryptsButton
          planId="1"
          variant="primary"
          size="lg"
          onSuccess={() => refetch()}
        >
          Subscribe Now
        </SubscryptsButton>
      </div>
    );
  }

  return (
    <article>
      <h1>Premium Analysis: DeFi Trends 2026</h1>
      <p>This content is only visible to active subscribers...</p>
      <footer>
        <small>
          Subscription renews on {status.expirationDate?.toLocaleDateString()}
          {status.isAutoRenewing ? ' (auto-renewal on)' : ''}
        </small>
      </footer>
    </article>
  );
}

/**
 * App wrapper
 */
function App() {
  return (
    <SubscryptsProvider>
      <PremiumArticleGuarded />
    </SubscryptsProvider>
  );
}

function ArticleSkeleton() {
  return (
    <div className="skeleton">
      <div className="skeleton-title" />
      <div className="skeleton-line" />
      <div className="skeleton-line" />
      <div className="skeleton-line short" />
    </div>
  );
}

export default App;
```

---

## Recipe 2: Merchant Dashboard

Display plans, subscriber counts, and revenue metrics for the connected merchant wallet. Uses `useMerchantPlans`, `useMerchantRevenue`, and `useMerchantSubscribers` hooks.

```tsx title="MerchantDashboardPage.tsx"
import {
  SubscryptsProvider,
  useMerchantPlans,
  useMerchantRevenue,
  useMerchantSubscribers,
  SubscriptsErrorBoundary,
  LoadingSpinner,
  ErrorDisplay
} from '@subscrypts/subscrypts-sdk-react';
import '@subscrypts/subscrypts-sdk-react/styles';
import { useState } from 'react';

function MerchantOverview() {
  const { plans, total: planCount, isLoading: plansLoading, error: plansError } = useMerchantPlans();
  const { revenue, isLoading: revenueLoading, error: revenueError } = useMerchantRevenue();
  const [selectedPlanId, setSelectedPlanId] = useState<string | null>(null);

  const {
    subscribers,
    total: subscriberTotal,
    activeCount,
    page,
    hasMore,
    isLoading: subsLoading,
    nextPage,
    prevPage
  } = useMerchantSubscribers(selectedPlanId || '0', 10);

  // Loading
  if (plansLoading || revenueLoading) {
    return <LoadingSpinner />;
  }

  // Error
  const error = plansError || revenueError;
  if (error) {
    return <ErrorDisplay error={error} />;
  }

  return (
    <div className="merchant-dashboard">
      {/* Revenue Metrics */}
      {revenue && (
        <section className="revenue-cards">
          <div className="metric-card">
            <h3>Monthly Recurring Revenue</h3>
            <p className="metric-value">{revenue.mrrFormatted} SUBS</p>
            {revenue.mrrUsdEstimate !== null && (
              <p className="metric-subtitle">
                ≈ ${revenue.mrrUsdEstimate.toFixed(2)} USD
              </p>
            )}
          </div>

          <div className="metric-card">
            <h3>Active Subscribers</h3>
            <p className="metric-value">{revenue.activeSubscribers}</p>
            <p className="metric-subtitle">of {revenue.totalSubscribers} total</p>
          </div>

          <div className="metric-card">
            <h3>Active Plans</h3>
            <p className="metric-value">
              {plans.filter(p => p.isActive).length}
            </p>
            <p className="metric-subtitle">of {planCount} total</p>
          </div>
        </section>
      )}

      {/* Plan List */}
      <section>
        <h2>Your Plans</h2>
        <div className="plan-grid">
          {plans.map((plan) => (
            <div
              key={plan.id.toString()}
              className={`plan-item ${selectedPlanId === plan.id.toString() ? 'selected' : ''}`}
              onClick={() => setSelectedPlanId(plan.id.toString())}
            >
              <h4>Plan #{plan.id.toString()}</h4>
              <p>{plan.description || 'No description'}</p>
              <p>{plan.subscriberCount.toString()} subscribers</p>
              <span className={`badge ${plan.isActive ? 'active' : 'inactive'}`}>
                {plan.isActive ? 'Active' : 'Inactive'}
              </span>
            </div>
          ))}
        </div>
      </section>

      {/* Subscriber Details */}
      {selectedPlanId && (
        <section>
          <h2>Subscribers for Plan #{selectedPlanId}</h2>
          <p>{activeCount} active out of {subscriberTotal} total</p>

          {subsLoading ? (
            <LoadingSpinner />
          ) : (
            <>
              <table>
                <thead>
                  <tr>
                    <th>Address</th>
                    <th>Renewal</th>
                    <th>Remaining Cycles</th>
                  </tr>
                </thead>
                <tbody>
                  {subscribers.map((sub) => (
                    <tr key={sub.id}>
                      <td>{sub.subscriber.slice(0, 6)}...{sub.subscriber.slice(-4)}</td>
                      <td>{sub.isAutoRenewing ? 'Auto' : 'Manual'}</td>
                      <td>{sub.remainingCycles === 0 ? 'Unlimited' : sub.remainingCycles}</td>
                    </tr>
                  ))}
                </tbody>
              </table>

              <div className="pagination">
                <button onClick={prevPage} disabled={page === 1}>Previous</button>
                <span>Page {page}</span>
                <button onClick={nextPage} disabled={!hasMore}>Next</button>
              </div>
            </>
          )}
        </section>
      )}
    </div>
  );
}

function App() {
  return (
    <SubscryptsProvider>
      <MerchantOverview />
    </SubscryptsProvider>
  );
}

export default App;
```

!!! tip "Pre-built alternative"
    If you do not need a custom layout, use the `<MerchantDashboard />` component directly. It renders all three sections (revenue, plans, subscribers) with default styling.

    ```tsx
    import { MerchantDashboard } from '@subscrypts/subscrypts-sdk-react';

    <MerchantDashboard />
    ```

---

## Recipe 3: Event Listener

React to real-time Subscrypts protocol events emitted by the smart contract. The `useSubscryptsEvents` hook listens for `_subscriptionCreate`, `_subscriptionPay`, and `_subscriptionRecurring` events and automatically cleans up listeners on unmount.

```tsx title="EventListener.tsx"
import {
  SubscryptsProvider,
  useSubscryptsEvents
} from '@subscrypts/subscrypts-sdk-react';
import '@subscrypts/subscrypts-sdk-react/styles';
import { useState, useCallback } from 'react';

interface EventLogEntry {
  type: 'created' | 'paid' | 'stopped';
  timestamp: Date;
  data: Record<string, string>;
}

function EventMonitor() {
  const [events, setEvents] = useState<EventLogEntry[]>([]);

  const addEvent = useCallback((entry: EventLogEntry) => {
    setEvents((prev) => [entry, ...prev].slice(0, 50)); // Keep last 50
  }, []);

  const { isListening, error } = useSubscryptsEvents({
    onSubscriptionCreated: (event) => {
      addEvent({
        type: 'created',
        timestamp: new Date(),
        data: {
          subscriptionId: event.subscriptionId.toString(),
          planId: event.planId.toString(),
          subscriber: event.subscriber,
          referral: event.referral
        }
      });

      // Trigger any side effects
      console.log('New subscription created:', event.subscriptionId.toString());
    },

    onSubscriptionPaid: (event) => {
      addEvent({
        type: 'paid',
        timestamp: new Date(),
        data: {
          subscriptionId: event.subscriptionId.toString(),
          payer: event.payer,
          amount: event.amount.toString()
        }
      });
    },

    onSubscriptionStopped: (event) => {
      addEvent({
        type: 'stopped',
        timestamp: new Date(),
        data: {
          subscriptionId: event.subscriptionId.toString(),
          subscriber: event.subscriber,
          enabled: event.enabled.toString()
        }
      });
    }
  });

  return (
    <div className="event-monitor">
      <h2>Live Event Feed</h2>

      <div className="status-bar">
        <span className={`status-dot ${isListening ? 'active' : 'inactive'}`} />
        {isListening ? 'Listening for events...' : 'Not connected'}
        {error && <span className="error"> Error: {error.message}</span>}
      </div>

      <div className="event-list">
        {events.length === 0 && <p>No events yet. Waiting...</p>}

        {events.map((entry, index) => (
          <div key={index} className={`event-entry event-${entry.type}`}>
            <div className="event-header">
              <span className="event-type">{entry.type.toUpperCase()}</span>
              <span className="event-time">
                {entry.timestamp.toLocaleTimeString()}
              </span>
            </div>
            <pre className="event-data">
              {JSON.stringify(entry.data, null, 2)}
            </pre>
          </div>
        ))}
      </div>
    </div>
  );
}

function App() {
  return (
    <SubscryptsProvider debug="debug">
      <EventMonitor />
    </SubscryptsProvider>
  );
}

export default App;
```

!!! info "Event names on-chain"
    The smart contract emits these Solidity events:

    - `_subscriptionCreate(uint256 subscriptionId, uint256 planId, address subscriber, address referral)`
    - `_subscriptionPay(uint256 subscriptionId, address payer, uint256 amount)`
    - `_subscriptionRecurring(uint256 subscriptionId, address subscriber, bool enabled)`

    The `useSubscryptsEvents` hook maps these to the `onSubscriptionCreated`, `onSubscriptionPaid`, and `onSubscriptionStopped` callbacks respectively.

---

## Recipe 4: USDC Payment Flow

The `CheckoutWizard` supports both SUBS and USDC payment methods out of the box. Users select their preferred method during the configuration step. For USDC payments, the SDK handles Uniswap v3 price quotes, Permit2 signatures, and the on-chain swap-and-subscribe transaction.

This recipe shows how to embed the full checkout flow with a pre-selected payment context.

```tsx title="UsdcCheckout.tsx"
import {
  SubscryptsProvider,
  CheckoutWizard,
  PricingTable,
  useSubscribe,
  useWallet,
  useTokenBalance
} from '@subscrypts/subscrypts-sdk-react';
import '@subscrypts/subscrypts-sdk-react/styles';
import { useState } from 'react';

/**
 * Option A: Using CheckoutWizard (recommended)
 *
 * The wizard handles payment method selection, Permit2 signatures,
 * Uniswap quotes, and the full transaction lifecycle.
 */
function CheckoutWithWizard() {
  const [checkoutPlanId, setCheckoutPlanId] = useState<string | null>(null);

  return (
    <>
      <PricingTable
        plans={[
          { planId: '1', title: 'Basic', subscribeLabel: 'Choose Basic' },
          { planId: '2', title: 'Pro', featured: true, subscribeLabel: 'Choose Pro' },
          { planId: '3', title: 'Enterprise', subscribeLabel: 'Choose Enterprise' }
        ]}
        currency="USDC"
        columns={3}
        onSubscribe={(planId) => setCheckoutPlanId(planId)}
      />

      {checkoutPlanId && (
        <CheckoutWizard
          planId={checkoutPlanId}
          isOpen={true}
          onClose={() => setCheckoutPlanId(null)}
          onSuccess={(subId) => {
            console.log('Subscribed with USDC! ID:', subId);
            setCheckoutPlanId(null);
          }}
          onError={(err) => {
            console.error('Checkout failed:', err);
          }}
        />
      )}
    </>
  );
}

/**
 * Option B: Hook-based USDC flow (full control)
 *
 * Use useSubscribe directly to execute a USDC subscription
 * with complete control over the UI and flow.
 */
function ManualUsdcSubscribe({ planId }: { planId: string }) {
  const { subscribe, isSubscribing, txState, error, subscriptionId } = useSubscribe();
  const { isConnected, connect } = useWallet();
  const { balance: usdcBalance } = useTokenBalance('USDC');

  const handleSubscribe = async () => {
    if (!isConnected) {
      await connect();
      return;
    }

    try {
      const subId = await subscribe({
        planId,
        cycleLimit: 12,
        autoRenew: true,
        paymentMethod: 'USDC',      // Pay with USDC
        referralAddress: undefined
      });

      console.log('Subscription created:', subId);
    } catch (err) {
      console.error('Subscribe failed:', err);
    }
  };

  return (
    <div className="usdc-subscribe">
      {usdcBalance !== null && (
        <p>Your USDC balance: {(Number(usdcBalance) / 1e6).toFixed(2)} USDC</p>
      )}

      <button onClick={handleSubscribe} disabled={isSubscribing}>
        {isSubscribing ? `${txState}...` : 'Subscribe with USDC'}
      </button>

      {error && <p className="error">{error.message}</p>}
      {subscriptionId && <p className="success">Subscription ID: {subscriptionId}</p>}

      {/* Transaction state indicator */}
      {isSubscribing && (
        <div className="tx-progress">
          <ProgressStep label="Approving USDC" active={txState === 'approving'} />
          <ProgressStep label="Signing Permit2" active={txState === 'waiting_approval'} />
          <ProgressStep label="Creating Subscription" active={txState === 'subscribing'} />
          <ProgressStep label="Confirming" active={txState === 'waiting_subscribe'} />
        </div>
      )}
    </div>
  );
}

function ProgressStep({ label, active }: { label: string; active: boolean }) {
  return (
    <div className={`progress-step ${active ? 'active' : ''}`}>
      {active && <span className="spinner" />}
      {label}
    </div>
  );
}

function App() {
  return (
    <SubscryptsProvider>
      <h1>Subscribe with USDC</h1>
      <CheckoutWithWizard />
    </SubscryptsProvider>
  );
}

export default App;
```

!!! info "How USDC payments work"
    When the user selects USDC as the payment method, the SDK:

    1. Fetches the plan's SUBS cost from the smart contract.
    2. Queries the Uniswap v3 QuoterV2 for the exact USDC amount needed (with 0.5% slippage buffer).
    3. Ensures USDC allowance for Permit2.
    4. Generates a Permit2 signature (gasless approval).
    5. Calls `paySubscriptionWithUsdcVerified()` on the smart contract, which swaps USDC to SUBS and creates the subscription in a single transaction.

---

## Recipe 5: Custom Wallet Integration (Privy)

Integrate a custom wallet provider (Privy for email/social login) alongside MetaMask using the connector architecture. Users choose their preferred connection method from a modal.

```tsx title="App.tsx — Full Privy + MetaMask integration"
import {
  SubscryptsProvider,
  InjectedConnector,
  ConnectWalletModal,
  SubscriptionDashboard,
  SubscryptsErrorBoundary,
  useSubscrypts,
  type WalletConnector,
  type ConnectResult
} from '@subscrypts/subscrypts-sdk-react';
import '@subscrypts/subscrypts-sdk-react/styles';
import { PrivyProvider, usePrivy, useWallets } from '@privy-io/react-auth';
import { BrowserProvider } from 'ethers';
import { useState, useMemo } from 'react';

// ──────────────────────────────────────────────
// Step 1: Implement the Privy connector
// ──────────────────────────────────────────────

class PrivyConnector implements WalletConnector {
  readonly id = 'privy';
  readonly name = 'Email / Social Login';
  readonly icon = '/privy-icon.svg';

  private privyHook: ReturnType<typeof usePrivy>;
  private walletsHook: ReturnType<typeof useWallets>;

  constructor(
    privyHook: ReturnType<typeof usePrivy>,
    walletsHook: ReturnType<typeof useWallets>
  ) {
    this.privyHook = privyHook;
    this.walletsHook = walletsHook;
  }

  isAvailable(): boolean {
    return true; // Privy works everywhere (email, social, etc.)
  }

  async connect(): Promise<ConnectResult> {
    // If not authenticated, trigger Privy login
    if (!this.privyHook.authenticated) {
      await this.privyHook.login();
    }

    // Wait for embedded wallet
    const wallet = this.walletsHook.wallets[0];
    if (!wallet) {
      throw new Error('No wallet available after login');
    }

    const ethereumProvider = await wallet.getEthereumProvider();
    const provider = new BrowserProvider(ethereumProvider);
    const signer = await provider.getSigner();
    const network = await provider.getNetwork();

    return {
      provider,
      signer,
      address: wallet.address,
      chainId: Number(network.chainId)
    };
  }

  async disconnect(): Promise<void> {
    await this.privyHook.logout();
  }

  async reconnect(): Promise<ConnectResult | null> {
    if (!this.privyHook.authenticated) return null;

    const wallet = this.walletsHook.wallets[0];
    if (!wallet) return null;

    const ethereumProvider = await wallet.getEthereumProvider();
    const provider = new BrowserProvider(ethereumProvider);
    const signer = await provider.getSigner();
    const network = await provider.getNetwork();

    return {
      provider,
      signer,
      address: wallet.address,
      chainId: Number(network.chainId)
    };
  }

  async switchNetwork(chainId: number): Promise<void> {
    const wallet = this.walletsHook.wallets[0];
    if (wallet) {
      await wallet.switchChain(chainId);
    }
  }
}

// ──────────────────────────────────────────────
// Step 2: Wire up SubscryptsProvider
// ──────────────────────────────────────────────

function SubscryptsApp() {
  const privyHook = usePrivy();
  const walletsHook = useWallets();

  const connectors = useMemo(() => [
    new InjectedConnector(),
    new PrivyConnector(privyHook, walletsHook)
  ], [privyHook, walletsHook]);

  return (
    <SubscryptsProvider connectors={connectors} persistSession={true}>
      <SubscryptsErrorBoundary>
        <AppContent />
      </SubscryptsErrorBoundary>
    </SubscryptsProvider>
  );
}

// ──────────────────────────────────────────────
// Step 3: Build the UI
// ──────────────────────────────────────────────

function AppContent() {
  const { wallet, connectors, connectWith, disconnect } = useSubscrypts();
  const [showConnectModal, setShowConnectModal] = useState(false);

  return (
    <div className="app">
      <header>
        <h1>My Subscription App</h1>

        {wallet.isConnected ? (
          <div className="wallet-info">
            <span>{wallet.address?.slice(0, 6)}...{wallet.address?.slice(-4)}</span>
            <button onClick={disconnect}>Disconnect</button>
          </div>
        ) : (
          <button onClick={() => setShowConnectModal(true)}>
            Connect Wallet
          </button>
        )}
      </header>

      {/* Connect modal with MetaMask + Privy options */}
      <ConnectWalletModal
        isOpen={showConnectModal}
        onClose={() => setShowConnectModal(false)}
        connectors={connectors}
        onConnect={async (connectorId) => {
          await connectWith(connectorId);
        }}
      />

      {/* Main content */}
      {wallet.isConnected ? (
        <SubscriptionDashboard
          pageSize={10}
          onSubscriptionCancelled={(id) => {
            console.log('Cancelled subscription:', id);
          }}
        />
      ) : (
        <div className="landing">
          <h2>Connect your wallet to manage subscriptions</h2>
          <p>
            Use MetaMask, Coinbase Wallet, or sign in with email
            via Privy.
          </p>
        </div>
      )}
    </div>
  );
}

// ──────────────────────────────────────────────
// Step 4: Wrap with Privy provider
// ──────────────────────────────────────────────

function App() {
  return (
    <PrivyProvider
      appId="your-privy-app-id"
      config={{
        embeddedWallets: { createOnLogin: 'users-without-wallets' }
      }}
    >
      <SubscryptsApp />
    </PrivyProvider>
  );
}

export default App;
```

!!! tip "Why connectors?"
    The connector architecture lets you support multiple wallet types with a single `SubscryptsProvider` configuration. Users who prefer browser wallets use MetaMask; users who prefer email login use Privy. The SDK handles session persistence, reconnection, and event forwarding uniformly across all connectors.
