---
title: Solution
description: Explanation of how Subscrypts leverages smart contracts to power automated, transparent, and user-controlled subscription payments in Web3.
tags:
  - solution
  - subscrypts
  - smart-contracts
  - subscriptions
  - web3
---

# Solution

## Subscrypts Solution Approach

Instead of relying on banks and billing platforms, [Subscrypts](https://subscrypts.com) uses self-executing smart contracts to manage subscriptions. Subscribers and merchants connect directly through code on the blockchain, removing middlemen entirely. This peer-to-peer model means the platform never holds users’ funds; payments flow straight from the subscriber’s wallet to the merchant, triggered automatically by the smart contract on the agreed schedule. A small platform fee (only 1% of each transaction) is collected in SUBS as part of the payment, significantly lower than typical payment processor fees.

### Example Scenario

To illustrate how it works, consider a simple example:

1. A merchant creates a subscription plan for premium content at a price of **100 SUBS per month**.  
2. A user subscribes to this plan via the [Subscrypts dApp](https://app.subscrypts.com). In doing so, the user approves the subscription smart contract to pull **100 SUBS** from their crypto wallet every month.  
3. Once the user confirms the subscription (one on-chain transaction to set it up), the merchant immediately grants the user access to the service (e.g., unlocks the premium content).  
4. Each billing cycle, the smart contract automatically transfers **100 SUBS** from the user’s wallet to the merchant’s address when payment is due. The contract simultaneously takes a **1% fee (1 SUBS)** out of that amount and routes it to the [Subscrypts](https://subscrypts.com) treasury as the platform’s fee. The merchant receives the remaining **99 SUBS** each month without having to do anything.

This cycle repeats every period. The user doesn’t need to sign a new payment each time – the smart contract does it automatically – but the user retains control: they can at any point revoke the contract’s permission to charge them, which would stop future payments immediately. If the user’s wallet doesn’t have sufficient SUBS when a payment is due, that payment simply fails (and the subscription can be halted until funds are available), rather than accumulating debt.

If the user cancels (or fails to pay), the merchant’s service can be automatically revoked for that user, ending the subscription term. Everything is enforced by code, so neither party has to manually intervene each cycle.

### Fiat-Denominated Subscriptions

One powerful feature of [Subscrypts](https://subscrypts.com) is the ability to denominate subscriptions in stable fiat terms while still using SUBS. A merchant can price a plan at, say, **“$10 per month”** instead of a fixed SUBS amount. The smart contracts will then determine how many SUBS equals $10 at the moment of each payment by consulting an on-chain SUBS/USDC exchange rate (via a decentralized exchange or price oracle). This means subscribers pay in SUBS, but merchants effectively receive a stable value – shielding both parties from cryptocurrency price volatility during the transaction. It removes the need for off-chain conversion: the rate lookup and swap calculation happen automatically on-chain, so neither the user nor merchant has to manually convert between SUBS and fiat value.

### Why this matters

**Global Reach:** Anyone with an internet connection and a crypto wallet can become a subscriber or merchant. There’s no need for a bank account or supported country—subscriptions are open to a worldwide user base. A content creator in one country can easily accept subscribers from anywhere, since SUBS transactions ignore international borders and banking systems.

**User Control:** Subscribers remain in control of their payments at all times. Unlike the traditional model where you hand over your credit card and a company can charge you until you cancel, [Subscrypts](https://subscrypts.com) is **non-custodial and permission-based**. You only give the smart contract the right to make the specified subscription charge; you can revoke that permission any time with a click, immediately stopping future charges. This drastically reduces the chance of unwanted charges and puts the user in the driver’s seat.

**Transparency:** Every subscription payment is recorded on the public blockchain. Both users and merchants have a clear, tamper-proof history of what was paid and when. This builds trust—**for example, a merchant can prove how many subscriptions have been paid for**, and a user can verify that they were charged the correct amount each period. There’s no opaque billing system; it’s all visible if you wish to inspect it.

**Programmability & Integration:** Because SUBS is a standard Ethereum-based token, it’s easy to integrate with other Web3 tools and platforms. Developers can build additional utilities—such as analytics dashboards, automated reward systems, or access management layers—on top of [Subscrypts](https://subscrypts.com)’ open smart contract framework.
