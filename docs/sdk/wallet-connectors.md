---
title: SDK Wallet Connectors
description: Architecture guide for the Subscrypts SDK wallet connector system, built-in connectors, and building custom connectors.
status: new
tags:
  - sdk
  - wallet
  - connectors
  - metamask
  - wagmi
---

# Wallet Connectors

The Subscrypts SDK uses a **connector architecture** that abstracts wallet interaction behind a common `WalletConnector` interface. This lets you support MetaMask, WalletConnect, Privy, Wagmi, RainbowKit, or any other wallet provider with a single integration pattern.

```tsx
import {
  InjectedConnector,
  type WalletConnector,
  type ConnectorId,
  type ConnectResult
} from '@subscrypts/subscrypts-sdk-react';
```

---

## WalletConnector Interface

Every connector -- built-in or custom -- implements the `WalletConnector` interface. The interface defines required methods for connection lifecycle and optional methods for event handling and network management.

```typescript title="WalletConnector interface"
import { BrowserProvider, Signer } from 'ethers';

type ConnectorId = 'injected' | 'external' | (string & {});

interface WalletConnector {
  /** Unique connector identifier */
  readonly id: ConnectorId;

  /** Human-readable connector name (e.g. 'MetaMask', 'WalletConnect') */
  readonly name: string;

  /** Optional icon URL or data URI */
  readonly icon?: string;

  /** Check if this connector is available (e.g. MetaMask installed?) */
  isAvailable(): boolean;

  /** Connect the wallet. Shows popup/modal as needed. */
  connect(): Promise<ConnectResult>;

  /** Disconnect the wallet */
  disconnect(): Promise<void>;

  /**
   * Silent reconnect without popup (for session persistence).
   * Returns null if reconnection is not possible.
   */
  reconnect?(): Promise<ConnectResult | null>;

  /** Listen to account changes */
  onAccountsChanged?(callback: (accounts: string[]) => void): void;

  /** Listen to chain/network changes */
  onChainChanged?(callback: (chainId: number) => void): void;

  /** Remove all event listeners */
  removeListeners?(): void;

  /** Switch to a specific network */
  switchNetwork?(chainId: number): Promise<void>;
}
```

### Required Methods

| Method | Description |
|---|---|
| `isAvailable()` | Returns `true` if this connector can be used in the current environment. For injected wallets, this checks `window.ethereum`. For external providers, this typically returns `true`. |
| `connect()` | Initiates the wallet connection. May trigger a popup or modal. Returns a `ConnectResult` on success. |
| `disconnect()` | Tears down the connection and cleans up internal state. |

### Optional Methods

| Method | Description |
|---|---|
| `reconnect()` | Silent reconnection without user interaction. Used by session persistence to restore connections on page reload. Returns `null` if reconnection is not possible. |
| `onAccountsChanged()` | Registers a callback that fires when the user switches accounts in their wallet. |
| `onChainChanged()` | Registers a callback that fires when the user switches networks. |
| `removeListeners()` | Unsubscribes all registered event listeners. Called during disconnect and cleanup. |
| `switchNetwork()` | Programmatically requests the wallet to switch to a specific chain ID. |

---

## ConnectResult Type

The `ConnectResult` type is returned by `connect()` and `reconnect()`. It provides everything the SDK needs to initialize contract instances and execute transactions.

```typescript title="ConnectResult"
import { BrowserProvider, Signer } from 'ethers';

interface ConnectResult {
  /** ethers.js v6 BrowserProvider instance */
  provider: BrowserProvider;

  /** ethers.js v6 Signer for signing transactions */
  signer: Signer;

  /** Checksummed wallet address */
  address: string;

  /** Current chain ID (e.g. 42161 for Arbitrum One) */
  chainId: number;
}
```

!!! info "ethers.js v6"
    The SDK uses ethers.js v6. All connectors must return a `BrowserProvider` (not the legacy `Web3Provider` from ethers v5) and a corresponding `Signer`.

---

## Built-in Connectors

### InjectedConnector

Connects to browser-injected wallets such as MetaMask, Coinbase Wallet, or any wallet that exposes `window.ethereum`. This is the default connector when `enableWalletManagement={true}`.

```typescript title="InjectedConnector"
import { InjectedConnector } from '@subscrypts/subscrypts-sdk-react';

const metamask = new InjectedConnector();
// or with options:
const customInjected = new InjectedConnector({
  name: 'My Wallet',
  icon: 'https://example.com/icon.svg'
});
```

#### Properties

| Property | Value |
|---|---|
| `id` | `'injected'` |
| `name` | Auto-detected: `'MetaMask'`, `'Coinbase Wallet'`, or `'Browser Wallet'` |
| `icon` | Optional, passed via constructor |

#### Behavior

- **`isAvailable()`** -- Returns `true` if `window.ethereum` exists.
- **`connect()`** -- Calls `eth_requestAccounts` (triggers popup). Creates an ethers `BrowserProvider` and `Signer`.
- **`disconnect()`** -- Removes event listeners and resets internal provider state. Does not revoke MetaMask permissions (browser wallets do not support programmatic disconnect).
- **`reconnect()`** -- Calls `eth_accounts` (no popup). Returns `null` if no accounts are authorized.
- **`onAccountsChanged()`** -- Listens to the `accountsChanged` event on `window.ethereum`.
- **`onChainChanged()`** -- Listens to the `chainChanged` event on `window.ethereum`. Parses the hex chain ID to a number.
- **`switchNetwork(chainId)`** -- Calls `wallet_switchEthereumChain`. If the chain is unknown (error code 4902), attempts to add the network via `wallet_addEthereumChain`.

#### Example: Default Setup

```tsx title="SubscryptsProvider with InjectedConnector (implicit)"
import { SubscryptsProvider } from '@subscrypts/subscrypts-sdk-react';

// enableWalletManagement defaults to true, which auto-creates InjectedConnector
<SubscryptsProvider>
  <App />
</SubscryptsProvider>
```

#### Example: Explicit Connector

```tsx title="Explicit InjectedConnector with options"
import { SubscryptsProvider, InjectedConnector } from '@subscrypts/subscrypts-sdk-react';

<SubscryptsProvider
  connectors={[
    new InjectedConnector({ name: 'MetaMask', icon: '/metamask.svg' })
  ]}
>
  <App />
</SubscryptsProvider>
```

---

### ExternalConnector

Wraps an externally-managed wallet provider (Wagmi, RainbowKit, or any library that provides an ethers `BrowserProvider` and `Signer`) into the `WalletConnector` interface. The external app manages the full connection lifecycle; this connector simply exposes the provider and signer to the SDK.

!!! note "Internal use"
    `ExternalConnector` is created automatically when you use `externalProvider` mode. You typically do not instantiate it directly.

```typescript title="ExternalConnector (internal)"
import { ExternalConnector } from '@subscrypts/subscrypts-sdk-react';

const connector = new ExternalConnector(
  { provider, signer, address },  // ExternalWalletConfig
  42161                             // chainId
);
```

#### Properties

| Property | Value |
|---|---|
| `id` | `'external'` |
| `name` | `'External Provider'` |

#### Behavior

- **`isAvailable()`** -- Always returns `true` (the external app ensures availability).
- **`connect()`** -- Returns the provided `provider`, `signer`, `address`, and `chainId` directly.
- **`disconnect()`** -- No-op. The external app manages disconnect.
- **`reconnect()`** -- Returns the same result as `connect()` (already connected).

#### Example: Wagmi Integration

```tsx title="External mode with Wagmi"
import { SubscryptsProvider } from '@subscrypts/subscrypts-sdk-react';
import { useAccount, useWalletClient } from 'wagmi';
import { BrowserProvider } from 'ethers';

function SubscryptsWrapper({ children }: { children: React.ReactNode }) {
  const { address } = useAccount();
  const { data: walletClient } = useWalletClient();

  if (!address || !walletClient) return <>{children}</>;

  const provider = new BrowserProvider(walletClient.transport);
  const signer = provider.getSigner();

  return (
    <SubscryptsProvider
      enableWalletManagement={false}
      externalProvider={{ provider, signer: await signer, address }}
    >
      {children}
    </SubscryptsProvider>
  );
}
```

---

## Building a Custom Connector

To integrate any wallet provider, implement the `WalletConnector` interface. The following example shows a complete Privy connector that uses email/social login.

### Step 1: Implement the Interface

```typescript title="PrivyConnector.ts"
import { BrowserProvider, Signer } from 'ethers';
import type {
  WalletConnector,
  ConnectResult
} from '@subscrypts/subscrypts-sdk-react';

// Import your Privy SDK
import { PrivyClient } from '@privy-io/react-auth';

export class PrivyConnector implements WalletConnector {
  readonly id = 'privy';
  readonly name = 'Email / Social Login';
  readonly icon = 'https://your-cdn.com/privy-icon.svg';

  private privyClient: PrivyClient;
  private provider: BrowserProvider | null = null;

  constructor(privyClient: PrivyClient) {
    this.privyClient = privyClient;
  }

  /**
   * Privy is always available (it uses email/social, no extension needed)
   */
  isAvailable(): boolean {
    return true;
  }

  /**
   * Connect via Privy login flow
   */
  async connect(): Promise<ConnectResult> {
    // Trigger Privy login (shows email/social modal)
    const user = await this.privyClient.login();

    // Get the embedded wallet
    const wallet = user.wallet;
    if (!wallet) {
      throw new Error('No wallet found after Privy login');
    }

    // Get ethers provider from Privy's embedded wallet
    const ethereumProvider = await wallet.getEthereumProvider();
    this.provider = new BrowserProvider(ethereumProvider);
    const signer = await this.provider.getSigner();
    const network = await this.provider.getNetwork();

    return {
      provider: this.provider,
      signer,
      address: wallet.address,
      chainId: Number(network.chainId)
    };
  }

  /**
   * Disconnect: log out of Privy
   */
  async disconnect(): Promise<void> {
    await this.privyClient.logout();
    this.provider = null;
  }

  /**
   * Silent reconnect: check if user is already authenticated
   */
  async reconnect(): Promise<ConnectResult | null> {
    const user = this.privyClient.user;
    if (!user || !user.wallet) return null;

    const ethereumProvider = await user.wallet.getEthereumProvider();
    this.provider = new BrowserProvider(ethereumProvider);
    const signer = await this.provider.getSigner();
    const network = await this.provider.getNetwork();

    return {
      provider: this.provider,
      signer,
      address: user.wallet.address,
      chainId: Number(network.chainId)
    };
  }

  /**
   * Switch network via Privy's embedded wallet
   */
  async switchNetwork(chainId: number): Promise<void> {
    const user = this.privyClient.user;
    if (!user?.wallet) throw new Error('No wallet connected');

    await user.wallet.switchChain(chainId);
  }

  // Privy embedded wallets do not emit account/chain change events,
  // so these are intentionally omitted.
}
```

### Step 2: Register with SubscryptsProvider

```tsx title="App.tsx"
import { SubscryptsProvider, InjectedConnector } from '@subscrypts/subscrypts-sdk-react';
import '@subscrypts/subscrypts-sdk-react/styles';
import { PrivyConnector } from './PrivyConnector';
import { usePrivy } from '@privy-io/react-auth';

function App() {
  const privyClient = usePrivy();

  const connectors = [
    new InjectedConnector(),             // MetaMask / browser wallet
    new PrivyConnector(privyClient)      // Email / social login
  ];

  return (
    <SubscryptsProvider connectors={connectors}>
      <YourApp />
    </SubscryptsProvider>
  );
}
```

### Step 3: Let Users Choose

Use the `ConnectWalletModal` component to present all available connectors to the user.

```tsx title="ConnectButton.tsx"
import { useState } from 'react';
import { ConnectWalletModal, useSubscrypts } from '@subscrypts/subscrypts-sdk-react';

function ConnectButton() {
  const [showModal, setShowModal] = useState(false);
  const { connectors, connectWith, wallet } = useSubscrypts();

  if (wallet.isConnected) {
    return <span>Connected: {wallet.address?.slice(0, 6)}...</span>;
  }

  return (
    <>
      <button onClick={() => setShowModal(true)}>Connect</button>

      <ConnectWalletModal
        isOpen={showModal}
        onClose={() => setShowModal(false)}
        connectors={connectors}
        onConnect={async (connectorId) => {
          await connectWith(connectorId);
        }}
      />
    </>
  );
}
```

---

## Session Persistence

The SDK persists wallet sessions across page reloads using `localStorage`. When a user connects, the SDK saves a lightweight session record. On the next page load, it silently reconnects via the connector's `reconnect()` method -- no popup, no user interaction.

### Session Functions

The following functions manage the session store. They are used internally by `SubscryptsProvider` but are exported for advanced use cases.

```typescript title="Session store API"
import type { ConnectorId } from '@subscrypts/subscrypts-sdk-react';

interface WalletSession {
  connectorId: ConnectorId;
  address: string;
  timestamp: number;
}

/** Save a wallet session to localStorage */
function saveSession(connectorId: ConnectorId, address: string): void;

/** Load a wallet session (returns null if none exists or invalid) */
function loadSession(): WalletSession | null;

/** Check if a session has expired */
function isSessionStale(session: WalletSession): boolean;

/** Clear the stored session */
function clearSession(): void;
```

### Session Validity

Sessions expire after **7 days** (configured via `SESSION_MAX_AGE_MS`). On page load, the SDK:

1. Loads the session from `localStorage`.
2. Checks if the session is stale via `isSessionStale()`.
3. Finds the connector matching `session.connectorId` from the resolved connectors list.
4. Calls `connector.reconnect()` for a silent (no-popup) reconnection.
5. If reconnection fails or the session is stale, it clears the session and waits for a manual connect.

### Configuration

Session persistence is enabled by default and can be controlled via `SubscryptsProvider`:

```tsx title="Disable session persistence"
<SubscryptsProvider persistSession={false}>
  <App />
</SubscryptsProvider>
```

!!! tip "SSR safety"
    All `localStorage` operations are wrapped in try/catch blocks. Session persistence gracefully degrades in environments where `localStorage` is unavailable (server-side rendering, private browsing, etc.).

---

## Connector Resolution

`SubscryptsProvider` resolves the active connectors based on the props you provide. The resolution order is:

| Priority | Condition | Result |
|---|---|---|
| 1 | `connectors` prop is provided | Uses the provided connectors directly |
| 2 | `enableWalletManagement={false}` + `externalProvider` | Creates an `ExternalConnector` wrapping the external provider |
| 3 | `enableWalletManagement={true}` (default) | Creates an `InjectedConnector` |
| 4 | None of the above | No connectors (wallet features are disabled) |

!!! warning "Mutually exclusive"
    The `connectors` prop takes highest priority. When provided, it overrides both `enableWalletManagement` and `externalProvider`.
