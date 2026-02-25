---
title: Hooks API Reference
description: Complete API reference for all Subscrypts React SDK hooks with signatures, return types, and code examples.
status: new
tags:
  - SDK
  - hooks
  - API
  - reference
  - React
---

# Hooks API Reference

The Subscrypts SDK exports 15 hooks that provide a headless API for building custom subscription UIs. All hooks require `SubscryptsProvider` as an ancestor component.

Import hooks from the main package or the dedicated hooks entry point:

```tsx
// Main entry
import { useSubscriptionStatus, useSubscribe } from '@subscrypts/subscrypts-sdk-react';

// Hooks-only entry (tree-shakeable)
import { useSubscriptionStatus, useSubscribe } from '@subscrypts/subscrypts-sdk-react/hooks';
```

---

=== "Subscription"

    ## useSubscriptionStatus

    Check whether a wallet has an active subscription to a specific plan. This is the primary hook for access control and content gating.

    ### Signature

    ```typescript
    function useSubscriptionStatus(
      planId: string,
      subscriber?: string
    ): UseSubscriptionStatusReturn
    ```

    ### Parameters

    | Parameter | Type | Required | Description |
    |---|---|---|---|
    | `planId` | `string` | Yes | Plan ID to check |
    | `subscriber` | `string` | No | Wallet address to check (defaults to connected wallet) |

    ### Return Type

    ```typescript
    interface UseSubscriptionStatusReturn {
      status: SubscriptionStatus | null;
      isLoading: boolean;
      error: Error | null;
      refetch: () => Promise<void>;
    }

    interface SubscriptionStatus {
      isActive: boolean;
      expirationDate: Date | null;
      isAutoRenewing: boolean;
      remainingCycles: number;
      subscriptionId: string | null;
    }
    ```

    ### Example

    ```tsx
    const { status, isLoading, error, refetch } = useSubscriptionStatus('1');

    if (isLoading) return <Spinner />;
    if (error) return <p>Error: {error.message}</p>;
    if (!status?.isActive) return <SubscribeCTA />;

    return (
      <div>
        <p>Active until {status.expirationDate?.toLocaleDateString()}</p>
        <p>Auto-renewing: {status.isAutoRenewing ? 'Yes' : 'No'}</p>
        <p>Remaining cycles: {status.remainingCycles}</p>
        <button onClick={refetch}>Refresh</button>
      </div>
    );
    ```

    !!! note "Smart caching"
        This hook uses adaptive cache TTL: 10s when the subscription expires within 5 minutes, 30s within 1 hour, and 60s otherwise.

    ---

    ## useSubscribe

    Execute a subscription purchase transaction with SUBS or USDC payment.

    ### Signature

    ```typescript
    function useSubscribe(): UseSubscribeReturn
    ```

    ### Return Type

    ```typescript
    interface UseSubscribeReturn {
      subscribe: (params: SubscribeParams) => Promise<string>;
      isSubscribing: boolean;
      txState: 'idle' | 'approving' | 'waiting_approval' | 'subscribing'
             | 'waiting_subscribe' | 'success' | 'error';
      error: Error | null;
      txHash: string | null;
      subscriptionId: string | null;
    }

    interface SubscribeParams {
      planId: string;
      cycleLimit: number;
      autoRenew: boolean;
      paymentMethod: 'SUBS' | 'USDC';
      referralAddress?: string;
    }
    ```

    ### Example

    ```tsx
    const { subscribe, isSubscribing, txState, error, subscriptionId } = useSubscribe();

    const handleSubscribe = async () => {
      try {
        const subId = await subscribe({
          planId: '1',
          cycleLimit: 12,
          autoRenew: true,
          paymentMethod: 'SUBS'
        });
        console.log('Subscription created:', subId);
      } catch (err) {
        console.error('Subscription failed:', err);
      }
    };

    return (
      <div>
        <button onClick={handleSubscribe} disabled={isSubscribing}>
          {isSubscribing ? `Status: ${txState}` : 'Subscribe'}
        </button>
        {error && <p>Error: {error.message}</p>}
        {subscriptionId && <p>Subscription ID: {subscriptionId}</p>}
      </div>
    );
    ```

    !!! info "Transaction flow"
        The `txState` progresses through: `idle` -> `approving` -> `subscribing` -> `success`. For USDC payments, the flow includes PERMIT2 signature generation and Uniswap swap.

    ---

    ## useMySubscriptions

    Fetch paginated subscriptions for a wallet address with client-side pagination.

    ### Signature

    ```typescript
    function useMySubscriptions(
      address?: string,
      pageSize?: number,
      planIds?: string[]
    ): UseMySubscriptionsReturn
    ```

    ### Parameters

    | Parameter | Type | Default | Description |
    |---|---|---|---|
    | `address` | `string` | Connected wallet | Wallet address to fetch subscriptions for |
    | `pageSize` | `number` | `10` | Number of subscriptions per page |
    | `planIds` | `string[]` | -- | Optional plan IDs to filter (also used as fallback lookup) |

    ### Return Type

    ```typescript
    interface UseMySubscriptionsReturn {
      subscriptions: Subscription[];
      total: number;
      page: number;
      pageSize: number;
      hasMore: boolean;
      isLoading: boolean;
      error: Error | null;
      nextPage: () => void;
      prevPage: () => void;
      refetch: () => Promise<void>;
    }
    ```

    ### Example

    ```tsx
    const { subscriptions, total, page, hasMore, isLoading, nextPage, prevPage } =
      useMySubscriptions(undefined, 10, ['1', '2', '3']);

    if (isLoading) return <Spinner />;

    return (
      <div>
        <h2>My Subscriptions ({total})</h2>
        {subscriptions.map(sub => (
          <div key={sub.id}>
            Plan {sub.planId} -- {sub.isAutoRenewing ? 'Auto-renewing' : 'Manual'}
          </div>
        ))}
        <button onClick={prevPage} disabled={page === 1}>Previous</button>
        <button onClick={nextPage} disabled={!hasMore}>Next</button>
      </div>
    );
    ```

    !!! tip "Plan ID filtering"
        Passing `planIds` enables a fallback lookup strategy. If the primary `getSubscriptionsByAddress` call returns empty results, the hook checks each plan individually via `getPlanSubscription`. This is more reliable for edge cases.

    ---

    ## useManageSubscription

    Manage an existing subscription: cancel, toggle auto-renewal, update cycles, or change custom attributes.

    ### Signature

    ```typescript
    function useManageSubscription(
      subscriptionId: string
    ): UseManageSubscriptionReturn
    ```

    ### Parameters

    | Parameter | Type | Required | Description |
    |---|---|---|---|
    | `subscriptionId` | `string` | Yes | The subscription ID to manage |

    ### Return Type

    ```typescript
    interface UseManageSubscriptionReturn {
      cancelSubscription: () => Promise<void>;
      toggleAutoRenew: (enabled: boolean) => Promise<void>;
      updateCycles: (cycles: number) => Promise<void>;
      updateAttributes: (attributes: string) => Promise<void>;
      txState: TransactionState;
      error: Error | null;
      isProcessing: boolean;
    }

    type TransactionState =
      | 'idle' | 'approving' | 'waiting_approval'
      | 'subscribing' | 'waiting_subscribe'
      | 'success' | 'error';
    ```

    ### Example

    ```tsx
    const {
      cancelSubscription,
      toggleAutoRenew,
      updateCycles,
      updateAttributes,
      isProcessing,
      txState,
      error
    } = useManageSubscription('42');

    return (
      <div>
        <button onClick={() => toggleAutoRenew(false)} disabled={isProcessing}>
          Disable Auto-Renew
        </button>
        <button onClick={() => updateCycles(6)} disabled={isProcessing}>
          Set to 6 Cycles
        </button>
        <button onClick={() => updateAttributes('tier=premium')} disabled={isProcessing}>
          Update Attributes
        </button>
        <button onClick={cancelSubscription} disabled={isProcessing}>
          Cancel Subscription
        </button>
        {isProcessing && <p>Processing: {txState}</p>}
        {error && <p>Error: {error.message}</p>}
      </div>
    );
    ```

=== "Plan"

    ## usePlan

    Fetch a single subscription plan by ID from the smart contract.

    ### Signature

    ```typescript
    function usePlan(planId: string): UsePlanReturn
    ```

    ### Parameters

    | Parameter | Type | Required | Description |
    |---|---|---|---|
    | `planId` | `string` | Yes | Plan ID to fetch |

    ### Return Type

    ```typescript
    interface UsePlanReturn {
      plan: Plan | null;
      isLoading: boolean;
      error: Error | null;
      refetch: () => Promise<void>;
    }

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

    ### Example

    ```tsx
    const { plan, isLoading, error } = usePlan('1');

    if (isLoading) return <Spinner />;
    if (error) return <p>Error: {error.message}</p>;
    if (!plan) return <p>Plan not found</p>;

    return (
      <div>
        <h2>{plan.description}</h2>
        <p>Subscribers: {plan.subscriberCount.toString()}</p>
        <p>Active: {plan.isActive ? 'Yes' : 'No'}</p>
      </div>
    );
    ```

    !!! note "Infinite cache"
        Plan data is cached with infinite TTL because plans are static on-chain. Use `refetch()` to force a fresh read.

    ---

    ## usePlans

    Fetch multiple plans by IDs in parallel.

    ### Signature

    ```typescript
    function usePlans(planIds: string[]): UsePlansReturn
    ```

    ### Parameters

    | Parameter | Type | Required | Description |
    |---|---|---|---|
    | `planIds` | `string[]` | Yes | Array of plan IDs to fetch |

    ### Return Type

    ```typescript
    interface UsePlansReturn {
      plans: Plan[];
      isLoading: boolean;
      error: Error | null;
      refetch: () => Promise<void>;
    }
    ```

    ### Example

    ```tsx
    const { plans, isLoading, error } = usePlans(['1', '2', '3']);

    if (isLoading) return <Spinner />;

    return (
      <div className="grid">
        {plans.map(plan => (
          <div key={plan.id.toString()}>
            <h3>{plan.description}</h3>
            <p>{plan.subscriberCount.toString()} subscribers</p>
          </div>
        ))}
      </div>
    );
    ```

    ---

    ## usePlansByMerchant

    Fetch all plans created by a specific merchant address.

    ### Signature

    ```typescript
    function usePlansByMerchant(
      merchantAddress: string
    ): UsePlansByMerchantReturn
    ```

    ### Parameters

    | Parameter | Type | Required | Description |
    |---|---|---|---|
    | `merchantAddress` | `string` | Yes | Ethereum address of the merchant |

    ### Return Type

    ```typescript
    interface UsePlansByMerchantReturn {
      plans: Plan[];
      total: number;
      isLoading: boolean;
      error: Error | null;
      refetch: () => Promise<void>;
    }
    ```

    ### Example

    ```tsx
    const { plans, total, isLoading } = usePlansByMerchant('0x1234...abcd');

    if (isLoading) return <Spinner />;

    return (
      <div>
        <h2>{total} plans found</h2>
        {plans.map(plan => (
          <div key={plan.id.toString()}>
            {plan.description} -- {plan.subscriberCount.toString()} subscribers
          </div>
        ))}
      </div>
    );
    ```

    !!! info "Fetch strategy"
        This hook fetches all plans from the contract and filters client-side by `merchantAddress`. For merchants with many plans across a large plan registry, this is efficient because plan data is small.

=== "Token"

    ## useTokenBalance

    Get the current token balance for SUBS or USDC.

    ### Signature

    ```typescript
    function useTokenBalance(token: TokenType): UseTokenBalanceReturn
    ```

    ### Parameters

    | Parameter | Type | Required | Description |
    |---|---|---|---|
    | `token` | `'SUBS' \| 'USDC'` | Yes | Token to get balance for |

    ### Return Type

    ```typescript
    interface UseTokenBalanceReturn {
      balance: bigint | null;
      formatted: string;
      isLoading: boolean;
      refetch: () => Promise<void>;
    }
    ```

    ### Example

    ```tsx
    const subs = useTokenBalance('SUBS');
    const usdc = useTokenBalance('USDC');

    return (
      <div>
        <p>SUBS: {subs.formatted}</p>
        <p>USDC: {usdc.formatted}</p>
        <button onClick={subs.refetch}>Refresh Balances</button>
      </div>
    );
    ```

    !!! note "Auto-refresh"
        Balances are automatically refreshed at the interval configured via `balanceRefreshInterval` on `SubscryptsProvider` (default: 30 seconds).

    ---

    ## useSUBSPrice

    Fetch the current SUBS/USD price from the on-chain oracle. Auto-refreshes every 60 seconds.

    ### Signature

    ```typescript
    function useSUBSPrice(
      refreshInterval?: number
    ): UseSUBSPriceReturn
    ```

    ### Parameters

    | Parameter | Type | Default | Description |
    |---|---|---|---|
    | `refreshInterval` | `number` | `60000` | Refresh interval in milliseconds |

    ### Return Type

    ```typescript
    interface UseSUBSPriceReturn {
      priceUsd: number | null;
      rawPrice: bigint | null;
      isLoading: boolean;
      error: Error | null;
      refetch: () => Promise<void>;
    }
    ```

    ### Example

    ```tsx
    const { priceUsd, isLoading, error } = useSUBSPrice();

    if (isLoading) return <p>Loading price...</p>;
    if (priceUsd === null) return <p>Price unavailable</p>;

    return <p>1 SUBS = ${priceUsd.toFixed(4)} USD</p>;
    ```

    ---

    ## usePlanPrice

    Fetch comprehensive price information for a plan, including SUBS amount, USDC equivalent (via Uniswap), and USD value. Handles both SUBS-denominated and USD-denominated plans.

    ### Signature

    ```typescript
    function usePlanPrice(
      planId: string,
      refreshInterval?: number
    ): UsePlanPriceReturn
    ```

    ### Parameters

    | Parameter | Type | Default | Description |
    |---|---|---|---|
    | `planId` | `string` | *required* | Plan ID to fetch pricing for |
    | `refreshInterval` | `number` | `60000` | Refresh interval in milliseconds |

    ### Return Type

    ```typescript
    interface UsePlanPriceReturn {
      price: PlanPriceInfo | null;
      isLoading: boolean;
      error: Error | null;
      refetch: () => Promise<void>;
    }

    interface PlanPriceInfo {
      subsAmount: bigint;
      subsFormatted: string;
      usdcAmount: bigint | null;
      usdcFormatted: string | null;
      usdValue: number | null;
      frequency: string;
      isUsdDenominated: boolean;
    }
    ```

    ### Example

    ```tsx
    const { price, isLoading } = usePlanPrice('1');

    if (isLoading || !price) return <Spinner />;

    return (
      <div>
        <p>{price.subsFormatted} SUBS / {price.frequency}</p>
        {price.usdcFormatted && <p>or {price.usdcFormatted} USDC</p>}
        {price.usdValue && <p>~${price.usdValue.toFixed(2)} USD</p>}
        {price.isUsdDenominated && <span>USD-denominated plan</span>}
      </div>
    );
    ```

=== "Merchant"

    ## useMerchantPlans

    Fetch all plans owned by the connected wallet. Convenience wrapper around `usePlansByMerchant` that automatically uses the connected wallet address.

    ### Signature

    ```typescript
    function useMerchantPlans(): UseMerchantPlansReturn
    ```

    ### Return Type

    ```typescript
    // Same as UsePlansByMerchantReturn
    interface UseMerchantPlansReturn {
      plans: Plan[];
      total: number;
      isLoading: boolean;
      error: Error | null;
      refetch: () => Promise<void>;
    }
    ```

    ### Example

    ```tsx
    const { plans, total, isLoading } = useMerchantPlans();

    if (isLoading) return <Spinner />;

    return (
      <div>
        <h2>My Plans ({total})</h2>
        {plans.map(plan => (
          <div key={plan.id.toString()}>
            {plan.description} -- {plan.subscriberCount.toString()} subscribers
          </div>
        ))}
      </div>
    );
    ```

    ---

    ## useMerchantSubscribers

    Fetch paginated subscribers for a specific plan with active/total counts.

    ### Signature

    ```typescript
    function useMerchantSubscribers(
      planId: string,
      pageSize?: number
    ): UseMerchantSubscribersReturn
    ```

    ### Parameters

    | Parameter | Type | Default | Description |
    |---|---|---|---|
    | `planId` | `string` | *required* | Plan ID to fetch subscribers for |
    | `pageSize` | `number` | `10` | Subscribers per page |

    ### Return Type

    ```typescript
    interface UseMerchantSubscribersReturn {
      subscribers: Subscription[];
      total: number;
      activeCount: number;
      page: number;
      pageSize: number;
      hasMore: boolean;
      isLoading: boolean;
      error: Error | null;
      nextPage: () => void;
      prevPage: () => void;
      refetch: () => Promise<void>;
    }
    ```

    ### Example

    ```tsx
    const {
      subscribers, activeCount, total, page, hasMore, nextPage, prevPage, isLoading
    } = useMerchantSubscribers('1');

    if (isLoading) return <Spinner />;

    return (
      <div>
        <h3>{activeCount} active / {total} total subscribers</h3>
        {subscribers.map(sub => (
          <div key={sub.id}>
            {sub.subscriber} -- {sub.isAutoRenewing ? 'Recurring' : 'One-time'}
          </div>
        ))}
        <button onClick={prevPage} disabled={page === 1}>Prev</button>
        <button onClick={nextPage} disabled={!hasMore}>Next</button>
      </div>
    );
    ```

    !!! note "Active count scope"
        The `activeCount` reflects the current page only, not the total across all pages. Counting all active subscribers would require fetching all pages, which is expensive for large subscriber bases.

    ---

    ## useMerchantRevenue

    Calculate Monthly Recurring Revenue (MRR) from active subscriptions across all merchant plans.

    ### Signature

    ```typescript
    function useMerchantRevenue(
      planIds?: string[]
    ): UseMerchantRevenueReturn
    ```

    ### Parameters

    | Parameter | Type | Default | Description |
    |---|---|---|---|
    | `planIds` | `string[]` | All merchant plans | Optional subset of plan IDs to calculate revenue for |

    ### Return Type

    ```typescript
    interface UseMerchantRevenueReturn {
      revenue: MerchantRevenueData | null;
      isLoading: boolean;
      error: Error | null;
      refetch: () => Promise<void>;
    }

    interface MerchantRevenueData {
      totalSubscribers: number;
      activeSubscribers: number;
      monthlyRecurringRevenue: bigint;
      mrrFormatted: string;
      mrrUsdEstimate: number | null;
    }
    ```

    ### Example

    ```tsx
    const { revenue, isLoading } = useMerchantRevenue();

    if (isLoading || !revenue) return <Spinner />;

    return (
      <div>
        <h2>Revenue Dashboard</h2>
        <p>MRR: {revenue.mrrFormatted} SUBS</p>
        {revenue.mrrUsdEstimate !== null && (
          <p>~${revenue.mrrUsdEstimate.toFixed(2)} USD/month</p>
        )}
        <p>
          {revenue.activeSubscribers} active / {revenue.totalSubscribers} total
        </p>
      </div>
    );
    ```

    !!! info "MRR calculation"
        MRR is calculated by normalizing each active subscription's payment amount to a 30-day period: `(subscriptionAmount / paymentFrequency) * 2,592,000`. The USD estimate uses the current on-chain SUBS/USD oracle price.

=== "Events"

    ## useSubscryptsEvents

    Subscribe to real-time Subscrypts protocol events. Automatically cleans up listeners on component unmount.

    ### Signature

    ```typescript
    function useSubscryptsEvents(
      callbacks: SubscryptsEventCallbacks
    ): UseSubscryptsEventsReturn
    ```

    ### Parameters

    ```typescript
    interface SubscryptsEventCallbacks {
      onSubscriptionCreated?: (event: {
        subscriptionId: bigint;
        planId: bigint;
        subscriber: string;
        referral: string;
      }) => void;

      onSubscriptionPaid?: (event: {
        subscriptionId: bigint;
        payer: string;
        amount: bigint;
      }) => void;

      onSubscriptionStopped?: (event: {
        subscriptionId: bigint;
        subscriber: string;
        enabled: boolean;
      }) => void;
    }
    ```

    ### Return Type

    ```typescript
    interface UseSubscryptsEventsReturn {
      isListening: boolean;
      error: Error | null;
    }
    ```

    ### Example

    ```tsx
    const { isListening, error } = useSubscryptsEvents({
      onSubscriptionCreated: (event) => {
        console.log('New subscription:', event.subscriptionId.toString());
        console.log('Plan:', event.planId.toString());
        console.log('Subscriber:', event.subscriber);
        refetchDashboard();
      },
      onSubscriptionPaid: (event) => {
        console.log('Payment received:', event.amount.toString());
        refreshRevenue();
      },
      onSubscriptionStopped: (event) => {
        console.log('Subscription stopped:', event.subscriptionId.toString());
        if (!event.enabled) {
          revokeAccess(event.subscriber);
        }
      }
    });

    return (
      <div>
        <p>Event listener: {isListening ? 'Active' : 'Inactive'}</p>
        {error && <p>Listener error: {error.message}</p>}
      </div>
    );
    ```

    !!! info "Contract events"
        The hook listens to these on-chain events: `_subscriptionCreate`, `_subscriptionPay`, and `_subscriptionRecurring`. See [ABI Reference](../smart-contract/abi-reference.md) for full event signatures.

=== "Wallet"

    ## useWallet

    Access wallet connection state, connect/disconnect actions, and connector information.

    ### Signature

    ```typescript
    function useWallet(): UseWalletReturn
    ```

    ### Return Type

    ```typescript
    interface UseWalletReturn extends WalletState {
      connect?: () => Promise<void>;
      disconnect?: () => Promise<void>;
      switchNetwork: (chainId: number) => Promise<void>;
      connectors: WalletConnector[];
      activeConnector: WalletConnector | null;
      connectWith: (connectorId: ConnectorId) => Promise<void>;
    }

    interface WalletState {
      address: string | null;
      chainId: number | null;
      isConnected: boolean;
      isConnecting: boolean;
      error: Error | null;
    }
    ```

    ### Example

    ```tsx
    const {
      address, isConnected, isConnecting,
      connect, disconnect, switchNetwork,
      connectors, connectWith
    } = useWallet();

    if (isConnecting) return <p>Connecting...</p>;

    if (!isConnected) {
      return (
        <div>
          {/* Connect with first available connector */}
          <button onClick={connect}>Connect Wallet</button>

          {/* Or let user choose */}
          {connectors.filter(c => c.isAvailable()).map(c => (
            <button key={c.id} onClick={() => connectWith(c.id)}>
              {c.name}
            </button>
          ))}
        </div>
      );
    }

    return (
      <div>
        <p>Connected: {address?.slice(0, 6)}...{address?.slice(-4)}</p>
        <button onClick={disconnect}>Disconnect</button>
      </div>
    );
    ```

    !!! note "connect / disconnect availability"
        `connect` and `disconnect` are only available when using internal wallet management or connector mode. In external mode (Wagmi), they are `undefined` because the parent app manages the wallet lifecycle.

---

## Related

- [Provider Setup](provider-setup.md) -- configure `SubscryptsProvider` before using hooks
- [Components Reference](components-reference.md) -- pre-built UI components that use these hooks internally
- [Code Examples](code-examples.md) -- full integration recipes combining multiple hooks
- [ABI Reference](../smart-contract/abi-reference.md) -- smart contract functions the hooks call under the hood
