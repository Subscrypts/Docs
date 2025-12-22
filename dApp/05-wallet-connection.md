---
title: Subscrypts dApp – Wallet Connection
description: Explanation of how wallet connections work in the Subscrypts dApp, including supported wallets, network detection, permissions, and transaction security.
tags:
 - dapp
 - wallet
 - connection
 - arbitrum
 - crypto wallet
 - subscrypts
---

# Wallet Connection

Connecting a crypto wallet is the first and most important step in using the [**Subscrypts dApp**](https://app.subscrypts.com). The dApp leverages **wallet-based authentication** to enable secure, private, and direct blockchain interaction without traditional logins or user accounts.

This page explains how the wallet connection process works, which wallets are supported, and how Subscrypts ensures user security and transparency.

---

## Supported Wallets

The Subscrypts dApp supports all **Ethereum-compatible wallets** capable of connecting to **Arbitrum One**, including:

* **MetaMask** (browser extension and mobile app)
* **WalletConnect** (QR-based mobile wallet linking)
* **Coinbase Wallet**
* **Brave Wallet**
* **Trust Wallet**

Other wallets that integrate via WalletConnect are also supported by default.

> 💡 **Tip:** Ensure your wallet has the latest version and supports the Arbitrum network before connecting.

---

## How Wallet Authentication Works

The dApp replaces conventional username/password systems with **cryptographic authentication** through your blockchain wallet. When you connect:

1. The dApp sends a standard connection request (e.g., `ethereum.request({ method: 'eth_requestAccounts' })`).
2. Your wallet displays a prompt asking you to authorize the connection.
3. Once confirmed, the dApp retrieves your **public address** — no private keys or personal information are ever shared.
4. This address becomes your on-chain identity for all actions.

All subsequent interactions (such as creating plans or subscribing) happen under this wallet identity and require **explicit approval** in the wallet UI.

---

## Network Detection and Switching

The Subscrypts platform operates on **Arbitrum One** — an Ethereum Layer-2 network known for low gas fees and high speed.

If your wallet is connected to another network, the dApp automatically detects it and prompts you to switch.

### Automatic Network Switching

When needed, the dApp sends a request to add or switch networks using standard RPC parameters:

```json
{
  "chainId": "0xA4B1", // Arbitrum One
  "chainName": "Arbitrum One",
  "rpcUrls": ["https://arb1.arbitrum.io/rpc"],
  "blockExplorerUrls": ["https://arbiscan.io"]
}
```

Once confirmed, your wallet switches to Arbitrum One, and all dApp actions become available.

> ⚠️ **Important:** Subscrypts transactions will not function correctly on other networks such as Ethereum Mainnet or Polygon.

---

## Connecting the Wallet

After ensuring the correct network, click **“Connect Wallet”** in the dApp header.

* Your wallet will ask for confirmation.
* Once approved, the dApp displays your **shortened wallet address** (e.g., `0x8Ed1...3fd27`).
* You can now browse plans, create subscriptions, or manage your existing ones.

### Multi-Account Handling

If your wallet holds multiple accounts, the dApp will use the **currently active address**. You can switch accounts from your wallet extension, and the dApp will automatically update to reflect the change.

---

## Transaction Authorization

The Subscrypts dApp is fully **non-custodial** — meaning it cannot execute transactions on your behalf. Every on-chain action requires explicit confirmation in your wallet.

### Subscription Payments

- **For SUBS-based payments** (using `subscriptionCreate(planId)`):  
  The contract handles all payment logic internally through the **burn-and-mint** mechanism that occurs atomically within `subscriptionCreate → subscriptionPay`.  
  **No token approval transaction is required**, as the SUBS payment is executed in a single step.

- **For USDC-based payments** (using `paySubscriptionWithUsdc(planId)`):  
  The function includes a built-in **Permit2** signature flow. The user signs a one-time USDC spending authorization as part of the same transaction — there is **no separate ERC-20 approval step**.

### Other Actions Requiring Confirmation

- **Creating Plans:** Merchants must confirm each plan creation transaction in their wallet.  
- **Canceling or Managing Subscriptions:** Subscribers confirm renewal toggles or cancellations (e.g., via `subscriptionRecurringCHG()` or `subscriptionStop()`).  

In all cases, the wallet clearly displays transaction details, network fees, and gas cost estimates before confirmation, ensuring transparency and user control at every step.

---

## Security Model

Subscrypts follows Web3 best practices for wallet security:

- **No Private Keys Stored:** Your private keys never leave your wallet.  
- **User-Controlled Permissions:** Approvals are explicit and can be revoked anytime from within your wallet.  
- **Transparent Calls:** The dApp displays all contract addresses and interactions in a readable format before confirmation.  
- **HTTPS & TLS Encryption:** All frontend communication is served securely.

Users can independently verify contract addresses against the official [Subscrypts ABI Reference](../smart-contract/11-abi-reference.md).

> ⚙️ **Note:** Broader adoption of the **Subscrypts ABI** by Web3 wallet providers is encouraged to improve transaction readability and UX.  
> When wallets natively recognize the Subscrypts ABI, users will see contract interactions presented in clear, human-readable descriptions directly in the wallet interface — reducing confusion and strengthening trust during transaction signing.

---

## Troubleshooting Connection Issues

If your wallet fails to connect or authorize:

- Ensure your wallet extension is unlocked.  
- Check that your browser supports injected Web3 providers.  
- Manually add the **Arbitrum One** network if not prompted.  
- Try disconnecting and reconnecting the wallet.  
- Clear your browser’s cache and reload the dApp.

If issues persist, verify the official site URL: **[https://app.subscrypts.com](https://app.subscrypts.com)** — never enter wallet credentials on third-party or lookalike sites.

> ⚙️ **Note:** Many mobile browsers shipped by phone manufacturers — such as **Apple Safari**, **Google Chrome (mobile)**, and **Samsung Internet Browser** — do **not** natively support injected Web3 providers like MetaMask or WalletConnect.  
> For the best experience on mobile, use a **Web3-enabled browser** such as:  
> - **Brave Browser** (built-in wallet and Web3 support)  
> - **MetaMask Mobile** (includes browser with wallet integration)  
> - **Trust Wallet Browser**  
> - **Rainbow Wallet**  
> - **Opera Crypto Browser**  
>   
> These browsers provide native Web3 compatibility, allowing the Subscrypts dApp to detect and interact with wallets correctly.

---

## Disconnecting or Switching Wallets

You can disconnect your wallet anytime from the dApp menu. This action:

* Removes the session link between your browser and wallet.
* Clears any cached address references.
* Does **not** revoke blockchain permissions (those must be revoked manually in your wallet if desired).

To switch wallets, simply connect another address through your wallet extension or mobile app.

---

## Summary

Connecting your wallet establishes your **on-chain identity** in the Subscrypts ecosystem. From that moment, every click in the [Subscrypts dApp](https://app.subscrypts.com) translates into verifiable, secure smart contract interactions on **Arbitrum One**.

| Step                 | Description                                  | Result                      |
| -------------------- | -------------------------------------------- | --------------------------- |
| Connect Wallet       | Authorize dApp access to your wallet address | Establish on-chain identity |
| Switch Network       | Prompt user to Arbitrum One                  | Ensure compatibility        |
| Confirm Transactions | Execute contract calls via wallet            | Complete on-chain actions   |

---

## What’s Next

Continue to [Interact Page](06-interact-page.md) to learn how advanced users and developers can directly call Subscrypts smart contract functions through the dApp.

For external resources, visit:

* [Subscrypts Homepage](https://subscrypts.com)
* [MiCAR Whitepaper](https://subscrypts.com/whitepaper)
* [Smart Contract Suite Overview](../smart-contract/01-introduction.md)
