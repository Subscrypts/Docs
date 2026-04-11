---
title: Provider Setup — SubscryptsProvider Configuration
description: Configure the SubscryptsProvider for internal wallet management, external providers, or custom connectors.
tags:
  - SDK
  - provider
  - configuration
  - wallet
  - setup
---

# Provider Setup

`SubscryptsProvider` is the root context component for the Subscrypts SDK. It must wrap every component that uses SDK hooks or components. It initializes the wallet connection, smart contract instances, token balances, query cache, and event listeners.

```tsx
import { SubscryptsProvider } from '@subscrypts/subscrypts-sdk-react';
import '@subscrypts/subscrypts-sdk-react/styles';

function App() {
  return (
    <SubscryptsProvider /* ...props */>
      <YourApp />
    </SubscryptsProvider>
  );
}
```

---

## Three Wallet Modes

The SDK supports three mutually exclusive wallet connection patterns. Choose the one that matches your application architecture.

### Mode 1: Internal Wallet Management (Default)

The SDK manages wallet connection directly via `window.ethereum` (MetaMask, Coinbase Wallet, or any injected browser wallet). This is the simplest setup -- no external dependencies required.

```tsx title="Internal mode"
<SubscryptsProvider enableWalletManagement={true}>
  <App />
</SubscryptsProvider>
```

Under the hood, the SDK creates an `InjectedConnector` that handles `eth_requestAccounts`, network switching, and account/chain change events. Users connect via the `useWallet().connect()` method or the `ConnectWalletModal` component.

!!! tip "Default behavior"
    `enableWalletManagement` defaults to `true`, so `<SubscryptsProvider>` with no props is equivalent to internal mode.

### Mode 2: External Provider (Wagmi / RainbowKit)

If your app already manages wallet connections with Wagmi, RainbowKit, or another library, pass the ethers.js `BrowserProvider`, `Signer`, and wallet `address` directly. The SDK will skip internal wallet management entirely.

```tsx title="External mode with Wagmi"
import { SubscryptsProvider } from '@subscrypts/subscrypts-sdk-react';
import { useAccount, useWalletClient } from 'wagmi';
import { BrowserProvider } from 'ethers';

function SubscryptsWrapper({ children }: { children: React.ReactNode }) {
  const { address } = useAccount();
  const { data: walletClient } = useWalletClient();

  // Convert Wagmi's walletClient to ethers.js BrowserProvider + Signer
  const provider = walletClient
    ? new BrowserProvider(walletClient.transport)
    : undefined;

  const [signer, setSigner] = useState(null);

  useEffect(() => {
    if (provider) {
      provider.getSigner().then(setSigner);
    }
  }, [provider]);

  if (!provider || !signer || !address) {
    return <p>Connect your wallet first.</p>;
  }

  return (
    <SubscryptsProvider
      enableWalletManagement={false}
      externalProvider={{
        provider,
        signer,
        address
      }}
    >
      {children}
    </SubscryptsProvider>
  );
}
```

The `ExternalWalletConfig` type:

```typescript
interface ExternalWalletConfig {
  provider: BrowserProvider;
  signer: Signer;
  address: string;
}
```

!!! warning "Important"
    When using external mode, `connect()` and `disconnect()` are **not** exposed by the SDK. Your parent app is responsible for wallet lifecycle management.

### Mode 3: Custom Connectors

For full control over which wallets are available, pass an array of `WalletConnector` instances. This overrides both internal management and external provider mode.

```tsx title="Custom connectors"
import {
  SubscryptsProvider,
  InjectedConnector
} from '@subscrypts/subscrypts-sdk-react';
import { PrivyConnector } from './PrivyConnector'; // Your custom connector

<SubscryptsProvider
  connectors={[
    new InjectedConnector(),         // MetaMask / browser wallet
    new PrivyConnector()             // Email / social login via Privy
  ]}
>
  <App />
</SubscryptsProvider>
```

Users select a connector via `connectWith(connectorId)` from `useWallet()`, or you can use the `ConnectWalletModal` component which lists all available connectors automatically.

See [Wallet Connectors](wallet-connectors.md) for the full `WalletConnector` interface and a step-by-step guide to building custom connectors.

---

## All Provider Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `children` | `ReactNode` | *required* | Child components |
| `enableWalletManagement` | `boolean` | `true` | Enable internal wallet management (MetaMask auto-detect) |
| `externalProvider` | `ExternalWalletConfig` | -- | External wallet config (required if `enableWalletManagement` is `false`) |
| `connectors` | `WalletConnector[]` | -- | Custom wallet connectors (overrides other modes) |
| `network` | `'arbitrum'` | `'arbitrum'` | Target network |
| `rpcUrl` | `string` | -- | Custom RPC URL (optional) |
| `balanceRefreshInterval` | `number` | `30000` | Token balance refresh interval in milliseconds |
| `debug` | `'silent' \| 'info' \| 'debug'` | `'info'` | Console logging level |
| `onAccountChange` | `(newAddress, oldAddress) => void` | -- | Callback when user switches wallet account |
| `onChainChange` | `(newChainId, oldChainId) => void` | -- | Callback when user switches network |
| `persistSession` | `boolean` | `true` | Persist wallet session to localStorage for auto-reconnect |
| `caching` | `CachingConfig` | `{ enabled: true, defaultTTL: 60000, maxEntries: 500 }` | Query cache configuration |

---

## Prop Details

### `debug`

Controls SDK console output. Useful for development and troubleshooting.

| Level | Output |
|---|---|
| `'silent'` | No console output |
| `'info'` | Transaction status, wallet connect/disconnect, errors |
| `'debug'` | Full developer debugging with all data payloads |

```tsx
{/* Development */}
<SubscryptsProvider debug="debug">

{/* Production */}
<SubscryptsProvider debug="silent">
```

### `onAccountChange`

Called when the user switches wallet accounts (e.g., changes the active account in MetaMask).

```tsx
<SubscryptsProvider
  onAccountChange={(newAddress, oldAddress) => {
    console.log(`Account changed: ${oldAddress} -> ${newAddress}`);
    // Refresh page state, clear user-specific caches, etc.
  }}
>
```

### `onChainChange`

Called when the user switches networks. The SDK automatically prompts to switch back to Arbitrum One, but this callback lets you respond to the change.

```tsx
<SubscryptsProvider
  onChainChange={(newChainId, oldChainId) => {
    console.log(`Chain changed: ${oldChainId} -> ${newChainId}`);
    if (newChainId !== 42161) {
      showNetworkWarning();
    }
  }}
>
```

### `persistSession`

When `true` (the default), the SDK saves the active connector ID and wallet address to `localStorage`. On page reload, it silently reconnects without showing a wallet popup.

Sessions expire after **7 days**. Disable this for kiosk-mode or shared-device applications:

```tsx
<SubscryptsProvider persistSession={false}>
```

### `caching`

The SDK includes an in-memory LRU cache that reduces redundant RPC calls. Plans, subscription status, and other query results are cached with configurable TTL.

```typescript
interface CachingConfig {
  /** Enable caching (default: true) */
  enabled?: boolean;
  /** Default time-to-live in milliseconds (default: 60000 = 60 seconds) */
  defaultTTL?: number;
  /** Maximum cache entries before LRU eviction (default: 500) */
  maxEntries?: number;
}
```

=== "Default (recommended)"

    ```tsx
    <SubscryptsProvider>
      {/* Caching is enabled by default with sensible settings */}
    </SubscryptsProvider>
    ```

=== "Custom TTL"

    ```tsx
    <SubscryptsProvider caching={{ enabled: true, defaultTTL: 30000, maxEntries: 1000 }}>
      {/* 30-second TTL, 1000 max entries */}
    </SubscryptsProvider>
    ```

=== "Disable caching"

    ```tsx
    <SubscryptsProvider caching={{ enabled: false }}>
      {/* Every hook call hits the RPC directly */}
    </SubscryptsProvider>
    ```

!!! note "Smart TTL"
    The `useSubscriptionStatus` hook uses smart TTL that adapts based on subscription expiration: 10 seconds when expiring soon, 30 seconds within an hour, 60 seconds otherwise. This ensures responsive updates without excessive RPC calls.

---

## NetworkConfig Type

The SDK targets Arbitrum One exclusively. The `NetworkConfig` type describes the network parameters:

```typescript
interface NetworkConfig {
  chainId: number;        // 42161
  name: string;           // 'Arbitrum One'
  rpcUrl: string;         // 'https://arb1.arbitrum.io/rpc'
  blockExplorer: string;  // 'https://arbiscan.io'
  nativeCurrency: {
    name: string;         // 'Ether'
    symbol: string;       // 'ETH'
    decimals: number;     // 18
  };
}
```

Access the current network config inside components via the `useSubscrypts()` context hook:

```tsx
import { useSubscrypts } from '@subscrypts/subscrypts-sdk-react';

function NetworkInfo() {
  const { network } = useSubscrypts();
  return <p>Connected to {network.name} (Chain ID: {network.chainId})</p>;
}
```

---

## Context Value

The `SubscryptsProvider` exposes a context value accessible via `useSubscrypts()`. While most developers will use the purpose-built hooks (`useWallet`, `useSubscriptionStatus`, etc.), the raw context is available for advanced use cases.

```typescript
interface SubscryptsContextValue {
  wallet: WalletState;
  signer: Signer | null;
  provider: BrowserProvider | null;
  network: NetworkConfig;
  switchNetwork: (chainId: number) => Promise<void>;
  subscryptsContract: Contract | null;
  subsTokenContract: Contract | null;
  usdcTokenContract: Contract | null;
  subsBalance: bigint | null;
  usdcBalance: bigint | null;
  refreshBalances: () => Promise<void>;
  cacheManager: CacheManager;
  connect?: () => Promise<void>;     // Only in internal/connector mode
  disconnect?: () => Promise<void>;  // Only in internal/connector mode
  connectors: WalletConnector[];
  activeConnector: WalletConnector | null;
  connectWith: (connectorId: ConnectorId) => Promise<void>;
}
```

---

## Full Configuration Example

```tsx title="src/App.tsx"
import {
  SubscryptsProvider,
  InjectedConnector
} from '@subscrypts/subscrypts-sdk-react';
import '@subscrypts/subscrypts-sdk-react/styles';

function App() {
  return (
    <SubscryptsProvider
      connectors={[new InjectedConnector()]}
      balanceRefreshInterval={15000}
      debug={import.meta.env.DEV ? 'debug' : 'silent'}
      persistSession={true}
      caching={{ enabled: true, defaultTTL: 45000, maxEntries: 200 }}
      onAccountChange={(newAddr, oldAddr) => {
        console.log(`Account: ${oldAddr} -> ${newAddr}`);
      }}
      onChainChange={(newChain, oldChain) => {
        console.log(`Chain: ${oldChain} -> ${newChain}`);
      }}
    >
      <YourApp />
    </SubscryptsProvider>
  );
}
```

---

## Next Steps

- [Hooks Reference](hooks-reference.md) -- use the headless API for full UI control
- [Components Reference](components-reference.md) -- drop-in pre-built widgets
- [Wallet Connectors](wallet-connectors.md) -- build custom connector implementations
