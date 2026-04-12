---
title: Subscrypts Architecture Overview
description: Architecture combining on-chain smart contracts and off-chain interfaces like the dApp and Discord Bot for decentralized subscriptions.
tags:
  - subscrypts
  - architecture
  - smart-contracts
  - arbitrum
  - web3
  - subscriptions
  - system-design
  - erc-20
---

# Architecture

[Subscrypts](https://subscrypts.com)' architecture combines on-chain smart contracts with off-chain components to deliver a seamless subscription service.

## Blockchain Layer (Arbitrum One)

At the core of [Subscrypts](https://subscrypts.com) is a set of smart contracts deployed on **Arbitrum One** (an Ethereum Layer-2 chain). Arbitrum provides high throughput and low transaction fees while inheriting the security of Ethereum, which is crucial for handling potentially frequent microtransactions. The choice of Arbitrum means users pay only minimal gas fees for subscription transactions, making the system efficient for small, recurring payments.

### Key Smart Contracts

**Subscription Smart Contracts** – These handle the logic of subscriptions: storing subscription terms, scheduling payments, and executing transfers of SUBS tokens from subscribers to merchants according to the set intervals. Each time a payment is due, the contract triggers a transfer (using the subscriber's prior approval) of the required SUBS amount. The contract also enforces rules like the 1% platform fee and can be configured (by the project's administrators) to adjust parameters if needed (for example, changing the fee rate for all or specific subscriptions).

**SUBS Token Contract** – An ERC-20 token contract (standard Ethereum token) governing the [Subscrypts](https://subscrypts.com) utility token. It defines the total supply of SUBS and enables transfers between users.

The token contract includes admin-controlled functions for supply adjustment (minting or burning tokens), as well as pausing or upgrading the contract. These functions are protected by a multi-signature governance wallet, meaning no single party can unilaterally alter token behavior. Any supply-related change would require explicit multi-signature approval, on-chain governance actions, and advance disclosure to the community.

In practice, the total SUBS supply is **fixed at 120 million tokens**, all minted at the Token Generation Event (TGE). There are **no plans to use mint or burn capabilities** outside of exceptional governance-approved circumstances, making the effective supply cap fixed for the foreseeable future.

**Price Oracle / DEX Integration** – To support fiat-denominated pricing, the subscription contracts interact with on-chain price sources (specifically a SUBS/USDC decentralized exchange pair on Uniswap). This allows the system to determine how many SUBS are required to match a fiat-denominated subscription price (e.g., $10) at the time of payment. The integration is fully on-chain and trustless, relying on real-time liquidity pool data without off-chain price feeds.

*For more technical details on these on-chain components, refer to the [Subscrypts Smart Contract Suite](../smart-contract/introduction.md) documentation.*

---

## Off-Chain Components

On top of the blockchain layer, [Subscrypts](https://subscrypts.com) provides user-facing applications that simplify interaction with the smart contracts. These are **official reference integrations** — they exist to accelerate adoption by giving merchants and subscribers batteries-included entry points. They are not the only way to use the protocol: any third party can build equivalent (or entirely different) integrations directly against the Smart Contract Suite. See [Platform-Agnostic Protocol](platform-agnostic.md) for the full developer-integration story.

**[Subscrypts dApp](https://app.subscrypts.com)** – A web-based interface allowing merchants to create and manage subscription plans and subscribers to manage their subscriptions. The dApp abstracts blockchain complexity by handling contract interactions after users confirm actions in their wallet.

**[Subscrypts Discord Bot](https://discord.onsubscrypts.com)** – A community-focused integration that allows subscription status checks, notifications, and role-based access control within Discord servers. The bot interacts with the same on-chain contracts and does not custody funds.

**[Subscrypts Telegram Bot](https://telegram.onsubscrypts.com)** – A community-focused integration that manages Telegram group and channel membership based on on-chain subscription state. Like the Discord Bot, it reads from the same smart contracts and does not custody funds. Features include join gating, smart reconciliation, and single-use invite links.

**[Subscrypts Pulse](https://pulse.subscrypts.com)** – A read-only subscription monitoring PWA that provides real-time dashboards and push notifications. It reads on-chain state but never writes or holds private keys.

*The dApp, Discord Bot, Telegram Bot, and Pulse all act as convenience layers only; all value transfer and enforcement occur on-chain.*

Because the blockchain holds every subscription's authoritative state, **Subscrypts is a platform-agnostic protocol**: any application that can speak blockchain RPC — in any language, on any runtime, on any platform — can read subscription state and transact against the same contracts as the official clients. The dApp, bots, Pulse, and React SDK are examples of what that looks like; third-party integrators can build any other client against the same surface. See [Platform-Agnostic Protocol](platform-agnostic.md) for the full picture, including how a single subscription can gate access across multiple platforms simultaneously.

---

## Architecture Diagram

```mermaid
flowchart TD
    %% Participants
    subgraph OffChain["Off-Chain"]
        WebApp["Subscrypts dApp (Web Interface)"]
        DiscordBot["Subscrypts Discord Bot"]
        TelegramBot["Subscrypts Telegram Bot"]
        PulseApp["Subscrypts Pulse (monitoring)"]
    end
    subgraph OnChain["On-Chain (Arbitrum One)"]
        TokenContract["SUBS Token Contract"]
        SubContract["Subscription Contract(s)"]
        DEX["Uniswap SUBS/USDC Pool"]
        TreasuryWallet["Subscrypts Treasury Wallet"]
    end

    Subscriber["Subscriber (User)"] -->|uses| WebApp
    Merchant["Merchant (Service Provider)"] -->|uses| WebApp
    Subscriber -->|can also use| DiscordBot
    Subscriber -->|can also use| TelegramBot
    Subscriber -->|monitors via| PulseApp

    WebApp -->|triggers txns| SubContract
    DiscordBot -->|triggers txns| SubContract
    TelegramBot -->|reads state| SubContract
    PulseApp -->|reads state| SubContract

    SubContract -->|pulls SUBS from| Subscriber
    SubContract -->|transfers SUBS to| Merchant
    SubContract -->|routes fee to| TreasuryWallet
    SubContract -->|queries rate| DEX
    SubContract -->|interacts with| TokenContract
```

---

## Security and Governance

All critical operations within the Subscrypts architecture are executed by smart contracts on Arbitrum, ensuring transparency and deterministic behavior. Administrative actions are controlled via a multi-signature wallet, preventing unilateral changes and enforcing collective governance.

Because the system operates on a public blockchain, transactions and contract behavior are independently verifiable. Users interact directly with decentralized infrastructure through the [Subscrypts dApp](https://app.subscrypts.com) or [Discord Bot](https://discord.onsubscrypts.com), preserving user custody, transparency, and trust minimization.

!!! ecosystem "Related Components"
    - [Smart Contract Architecture](../smart-contract/architecture.md) — Detailed on-chain architecture and contract interactions
    - [Smart Contract Security & Auditing](../smart-contract/security-auditing.md) — Security measures and audit processes
    - [dApp Features](../dapp/features.md) — Full feature set of the web interface
    - [Discord Bot Architecture](../discord-bot/architecture.md) — Bot design and integration patterns

---

## Related Topics

- [How Subscrypts Works](solution.md) — Solution approach and payment flow mechanics
- [SUBS Tokenomics](tokenomics.md) — Token supply and economic model details
- [Smart Contract Core Logic](../smart-contract/core-logic.md) — Deep dive into subscription contract logic
- [Smart Contract Access Control](../smart-contract/access-control.md) — Multi-sig governance and admin functions
- [Payment & Conversion Logic](../smart-contract/payment-conversion.md) — On-chain price oracle integration
