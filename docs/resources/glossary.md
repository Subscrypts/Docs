---
title: Glossary — Subscrypts Documentation
description: Definitions of key blockchain, crypto, and Subscrypts-specific terms used throughout this documentation.
tags:
  - glossary
  - reference
  - terminology
  - subscrypts
  - blockchain
  - getting-started
---

# Glossary

A reference of terms used throughout the Subscrypts documentation. Definitions are written in plain language for readers of all experience levels.

---

## A

ABI (Application Binary Interface)
:   A standardized description of a smart contract's functions, events, and data types that allows external applications to interact with it. Subscrypts publishes its ABI so developers can integrate with the protocol. See [ABI Reference](../smart-contract/abi-reference.md).

Account Abstraction
:   A blockchain design pattern that allows smart contracts to act as user accounts, enabling features such as gasless transactions, batch operations, and custom authentication logic without requiring a traditional externally owned account (EOA).

Arbitrum One
:   The Ethereum Layer-2 network (chain ID 42161) where all Subscrypts smart contracts and the SUBS token are deployed. It offers low gas fees and high throughput while inheriting Ethereum's security guarantees.

Atomic Transaction
:   A transaction in which all operations succeed or all operations revert together, leaving no partial or intermediate state. Subscrypts uses atomic transactions for payment swaps and subscription creation to prevent stuck funds.

## B

Basis Points (bps)
:   A unit of measurement equal to one hundredth of a percentage point (1 bps = 0.01%). Subscrypts expresses the platform fee in basis points — currently set at 100 bps (1%), with a configurable maximum of 500 bps (5%).

Block Explorer
:   A web tool for browsing blockchain data such as transactions, addresses, and contract interactions. Arbiscan ([arbiscan.io](https://arbiscan.io){ target=_blank }) is the primary block explorer for Arbitrum One.

Burn-and-Mint
:   The settlement mechanism used by Subscrypts for subscription payments. The smart contract burns the payment amount from the subscriber's wallet and mints 99% to the merchant and 1% to the protocol treasury in a single transaction. See [Payment & Conversion Mechanics](../smart-contract/payment-conversion.md).

## C

Chainalysis
:   A blockchain analytics provider whose sanctions oracle is integrated into the Subscrypts smart contracts. The protocol uses it to verify that neither merchants nor subscribers are flagged under applicable sanctions lists before processing payments. See [Core Logic](../smart-contract/core-logic.md).

Commission
:   An optional fee field within a subscription plan that can be configured by merchants for partner integrations or affiliate programs. The commission amount or percentage is defined at plan creation and stored on-chain.

## D

dApp (Decentralized Application)
:   A web application that interacts with smart contracts on a blockchain instead of a centralized backend. The Subscrypts dApp at [app.subscrypts.com](https://app.subscrypts.com){ target=_blank } is the primary interface for creating plans, subscribing, and managing payments. See [dApp Introduction](../dapp/introduction.md).

Decentralized Exchange (DEX)
:   A protocol that allows users to trade tokens directly on-chain without a centralized intermediary. Subscrypts integrates with Uniswap V3 on Arbitrum One for SUBS/USDC liquidity and conversion.

Delegatecall
:   A low-level EVM operation that executes another contract's code in the context of the calling contract's storage. Subscrypts uses delegatecall to route function calls from the proxy to the appropriate facet while maintaining a single shared state.

## E

ERC-20
:   The most widely adopted Ethereum token standard, defining a common interface for fungible tokens (transfer, approve, balanceOf, etc.). SUBS is an ERC-20 token deployed on Arbitrum One. See [Token Integration](../smart-contract/token-integration.md).

ERC-1967
:   An Ethereum standard that defines specific storage slots for proxy contract implementation addresses. Subscrypts uses ERC-1967 to ensure that proxy state and logic addresses are stored in predictable, collision-free locations.

## F

Facet
:   A modular smart contract that handles a specific domain of functionality within the Subscrypts proxy architecture. The four facets are FacetSubscription (plans and renewals), FacetPaymentUSDC (USDC conversion and swaps), FacetAdmin (governance and halts), and FacetView (read-only queries). See [Architecture Overview](../smart-contract/architecture.md).

## G

Gas
:   The unit that measures the computational cost of executing transactions on Ethereum and its Layer-2 networks. On Arbitrum One, gas fees are typically $0.01-$0.05 per transaction, making recurring subscription payments economically viable.

Grace Period
:   A configurable time window during migration mode in which existing Telegram group members retain access without an active subscription, allowing them time to subscribe. Grace periods can be set between 1 and 90 days. See [Telegram Bot Admin Setup Guide](../telegram-bot/admin-setup-guide.md).

Guild
:   Discord's internal term for a server. In the Subscrypts Discord Bot, each guild has isolated plan-to-role mappings, admin scopes, and subscription configurations. See [Discord Bot Introduction](../discord-bot/introduction.md).

## H

Halt States
:   Emergency controls within the FacetAdmin contract that allow authorized administrators to temporarily disable specific protocol operations such as plan creation, subscription payments, or USDC conversions. These safeguards enable rapid incident response. See [Security & Auditing](../smart-contract/security-auditing.md).

## I

IDO (Initial DEX Offering)
:   A token distribution method where tokens are launched directly on a decentralized exchange rather than through a private or centralized sale. The SUBS public sale takes place as an IDO on Uniswap V3 on Arbitrum One. See [Public Sale (IDO)](../subscrypts/public-sale.md).

## J

Join Gate
:   An access control mechanism in the Subscrypts Telegram Bot that prevents non-subscribers from joining a gated Telegram group in real time. When a user attempts to join, the bot checks their subscription status on-chain and blocks unauthorized access before the user can see group content. See [Telegram Bot Subscription Sync](../telegram-bot/subscription-sync.md).

## L

Layer 2 (L2)
:   A scaling solution built on top of an existing blockchain (Layer 1) that processes transactions more quickly and cheaply while inheriting the base layer's security. Arbitrum One is a Layer-2 network on Ethereum.

## M

Migration Mode
:   A feature of the Subscrypts Telegram Bot that allows group owners to transition existing free groups to subscription-gated access. Migration mode provides a configurable grace period, member discovery tools, and automated reminders before enforcement begins. See [Telegram Bot Admin Setup Guide](../telegram-bot/admin-setup-guide.md).

MiCAR (Markets in Crypto-Assets Regulation)
:   The EU regulatory framework — Regulation (EU) 2023/1114 — that establishes disclosure and conduct requirements for crypto-asset offerings. Subscrypts publishes a MiCAR-compliant whitepaper and classifies SUBS as a utility token under this regulation. See [Compliance](../subscrypts/compliance.md).

Mint
:   The process of creating new tokens on a blockchain. In the Subscrypts burn-and-mint settlement model, tokens are minted to the merchant's and treasury's wallets after being burned from the subscriber's wallet during payment.

## N

Non-Custodial
:   A design principle where the protocol never takes possession or control of user funds. In Subscrypts, payments flow directly from subscriber wallets to merchant wallets via smart contract logic — the protocol holds no funds beyond the scope of a single atomic transaction. See [Design Philosophy](../smart-contract/design.md).

## O

On-Chain
:   Refers to data or operations that are recorded and executed directly on the blockchain, making them publicly verifiable and tamper-proof. All Subscrypts subscription states, payments, and plan configurations are stored on-chain.

Oracle
:   An external data source that provides information to smart contracts. Subscrypts uses the Chainalysis sanctions oracle for compliance checks and Uniswap V3's on-chain pricing mechanism for SUBS/USDC conversion rates.

## P

Passive Collection
:   A batch renewal mechanism where an authorized service account calls `subscriptionCollectPassive()` to process multiple subscription renewals in a single transaction. This enables automated renewals without requiring individual subscriber action. See [Core Logic](../smart-contract/core-logic.md).

Permit2
:   A token approval protocol developed by Uniswap that enables gasless, signature-based approvals for ERC-20 token transfers. Subscrypts uses Permit2 so subscribers can authorize USDC payments without a separate on-chain approval transaction.

Plan
:   A subscription offering created by a merchant that defines the price, billing frequency, currency (SUBS or USDC), referral bonus, and metadata. Plans are stored on-chain in SubscryptsStorage and are identified by a unique auto-incremented ID. See [Core Logic](../smart-contract/core-logic.md).

Proxy Contract
:   A smart contract that serves as the permanent entry point for all interactions, forwarding calls to replaceable logic contracts via delegatecall. The Subscrypts proxy stores all persistent state and never changes its address, even as the underlying logic is upgraded. See [Architecture Overview](../smart-contract/architecture.md).

PWA (Progressive Web App)
:   A web application that can be installed on a device's home screen and used like a native app, without requiring an app store download. PWAs support push notifications, offline caching, and standalone mode. Subscrypts Pulse is distributed as a PWA. See [Pulse Installation](../pulse/installation.md).

## R

Reconciler
:   An automated background process in the Subscrypts Discord Bot and Telegram Bot that periodically verifies on-chain subscription states and adjusts access accordingly — granting roles or group membership for active subscriptions, and revoking them for expired ones. The reconciler is self-correcting and acts as a safety net alongside event-driven updates. See [Discord Bot Subscription Sync](../discord-bot/subscription-sync.md) and [Telegram Bot Subscription Sync](../telegram-bot/subscription-sync.md).

Reconciliation
:   The process of verifying that off-chain records (such as in the dApp or Discord Bot) match the authoritative on-chain state. Subscrypts supports reconciliation through FacetView read-only queries and event-driven synchronization.

Referral Bonus
:   An optional reward configured within a subscription plan that incentivizes existing users to refer new subscribers. The bonus amount is defined by the merchant at plan creation and distributed on-chain when a referred subscriber joins.

## S

SIWE (Sign-In with Ethereum)
:   An authentication standard (EIP-4361) that lets users prove wallet ownership by signing a message, without exposing private keys or sharing personal data. The Subscrypts Discord Bot and Telegram Bot use SIWE-based wallet linking for member verification. See [Discord Bot Security & Trust](../discord-bot/security-and-trust.md) and [Telegram Bot Security & Trust](../telegram-bot/security-and-trust.md).

Slippage
:   The difference between the expected price of a token swap and the actual price at execution time, caused by market movement or low liquidity. Subscrypts enforces minimum output thresholds to protect subscribers and merchants during USDC-to-SUBS conversions.

Smart Contract
:   A self-executing program stored on a blockchain that automatically enforces the terms of an agreement. Subscrypts uses smart contracts to manage the entire subscription lifecycle without intermediaries. See [Smart Contract Introduction](../smart-contract/introduction.md).

SUBS Token
:   The native ERC-20 utility token of the Subscrypts ecosystem, deployed on Arbitrum One with a fixed supply of 120 million tokens. SUBS is used for all subscription payments and platform fee settlement. It does not represent equity, voting rights, or profit-sharing. See [Tokenomics](../subscrypts/tokenomics.md).

Subscription
:   An on-chain record linking a subscriber's wallet to a merchant's plan, tracking payment history, renewal dates, and active status. Each subscription has a unique auto-incremented ID and is stored in SubscryptsStorage. See [Core Logic](../smart-contract/core-logic.md).

Subscrypts Pulse
:   A real-time subscription monitoring PWA at [pulse.subscrypts.com](https://pulse.subscrypts.com) that provides dashboards, multi-wallet tracking, and push notifications for Subscrypts subscriptions on Arbitrum One. Pulse is read-only and custodian-free — it never asks for private keys. See [Pulse Introduction](../pulse/introduction.md).

Subscrypts Telegram Bot
:   A multi-tenant automation bot at [telegram.onsubscrypts.com](https://telegram.onsubscrypts.com) that manages Telegram group and channel membership based on on-chain subscription state. Features include join gating, smart reconciliation, SIWE wallet linking, single-use invite links, and migration mode for existing groups. See [Telegram Bot Introduction](../telegram-bot/introduction.md).

## T

Token Generation Event (TGE)
:   The moment when all 120 million SUBS tokens are minted and the token becomes live and tradable on-chain. At TGE, 12.5% of total supply (15 million SUBS) enters circulation. See [Public Sale (IDO)](../subscrypts/public-sale.md).

Treasury
:   The protocol-controlled wallet that receives the 1% platform fee from every subscription payment. Treasury funds are secured by a multi-signature wallet and used exclusively for development, audits, marketing, and operational expenses. See [Tokenomics](../subscrypts/tokenomics.md).

## U

Uniswap V3
:   A decentralized exchange protocol that provides concentrated liquidity pools and precise price quoting. Subscrypts integrates with Uniswap V3 on Arbitrum One for SUBS/USDC conversions, real-time quoting, and the initial token launch (IDO). See [Payment & Conversion Mechanics](../smart-contract/payment-conversion.md).

USDC
:   A US dollar-pegged stablecoin (1 USDC = $1 USD) widely used in decentralized finance. Subscrypts supports USDC-denominated plans and direct USDC payments, which are automatically converted to SUBS on-chain via Uniswap V3. The USDC contract on Arbitrum One is `0xaf88d065e77c8cC2239327C5EDb3A432268e5831`.

UUPS (Universal Upgradeable Proxy Standard)
:   An Ethereum proxy pattern (EIP-1822) where the upgrade logic resides in the implementation contract rather than a separate admin contract. Subscrypts uses UUPS for gas-efficient, role-controlled upgrades while preserving on-chain state across versions. See [Architecture Overview](../smart-contract/architecture.md).

## V

Vesting
:   A schedule that controls the gradual release of locked tokens over a defined period. SUBS allocations outside the initial unlock are subject to vesting periods ranging from 12 to 36 months, preventing sudden oversupply and encouraging long-term alignment. See [Tokenomics](../subscrypts/tokenomics.md).

## W

Wallet
:   A software application (such as MetaMask, Coinbase Wallet, or Trust Wallet) that stores private keys and allows users to sign transactions on a blockchain. In Subscrypts, your wallet is your identity — no username or password is needed.

Wei
:   The smallest denomination of Ether (1 ETH = 10^18 wei). Token amounts in smart contracts, including SUBS, are typically stored and transferred in their smallest unit to avoid floating-point precision issues.

## X

XOR (Exclusive OR)
:   A bitwise operation sometimes used in smart contract selector calculations. Solidity uses XOR of function selectors to compute interface identifiers for standard detection (EIP-165).
