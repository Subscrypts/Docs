---
title: Frequently Asked Questions — Subscrypts
description: Answers to common questions about Subscrypts, the SUBS token, subscriptions, merchant setup, developer integration, and tokenomics.
tags:
  - faq
  - subscrypts
  - SUBS
  - help
  - support
  - getting-started
---

# Frequently Asked Questions

Find answers to the most common questions about Subscrypts, organized by topic. Click any question to expand the answer.

---

## General

??? question "Q: What is Subscrypts?"
    Subscrypts is a blockchain-based subscription management protocol on Arbitrum One that lets merchants offer recurring payment services using the SUBS utility token. Smart contracts automate the entire billing lifecycle — plan creation, payments, renewals, and cancellations — without banks, credit cards, or personal data. For a full overview, see [What is Subscrypts?](../getting-started/what-is-subscrypts.md).

??? question "Q: How is Subscrypts different from Stripe or Patreon?"
    Subscrypts charges only a 1% platform fee, compared to 2.9% + $0.30 (Stripe) or 5-12% (Patreon). Settlement is instant and on-chain, chargebacks are impossible, no personal data is collected, and anyone with a crypto wallet can participate regardless of country or banking status. See the comparison table on the [home page](../index.md) for a side-by-side breakdown.

??? question "Q: What blockchain does Subscrypts run on?"
    Subscrypts runs on Arbitrum One (chain ID 42161), an Ethereum Layer-2 network that provides low gas fees, high throughput, and full Ethereum security compatibility. All smart contracts, the SUBS token, and subscription logic are deployed on this network.

??? question "Q: Is Subscrypts open source?"
    The ABI definitions of the deployed contracts are publicly available, allowing anyone to interact with the protocol and verify on-chain events. The React SDK (`@subscrypts/subscrypts-sdk-react`) is also open source. The compiled contract bytecode is deployed on-chain for independent verification, although the full Solidity source code is not publicly distributed. See [ABI Reference](../smart-contract/abi-reference.md) for the published interfaces.

??? question "Q: Does Subscrypts collect personal data?"
    Subscrypts does not collect, store, or process any personal data. You interact with the protocol using only a crypto wallet address — no name, email, phone number, or credit card is required. Some merchants may independently collect additional data to meet local regulations, but the Subscrypts protocol itself handles none. See [Compliance](../subscrypts/compliance.md) for more details.

??? question "Q: Is Subscrypts compliant with EU regulations?"
    Subscrypts is designed from the ground up to align with the EU Markets in Crypto-Assets Regulation (MiCAR) — Regulation (EU) 2023/1114. The project publishes a MiCAR-compliant whitepaper with transparent risk disclosures, token classification, and issuer obligations. For full compliance details, see [Compliance](../subscrypts/compliance.md).

---

## For Subscribers

??? question "Q: What do I need to subscribe?"
    You need three things: a crypto wallet (such as MetaMask), a small amount of ETH on Arbitrum One for gas fees (typically $0.01-$0.05 per transaction), and SUBS or USDC tokens to pay for the subscription. For a step-by-step setup guide, see [Getting Started for Subscribers](../getting-started/for-subscribers.md).

??? question "Q: Can I pay with USDC instead of SUBS?"
    Yes, you can pay with USDC for your initial subscription. The smart contract automatically swaps your USDC to SUBS via Uniswap V3 in a single atomic transaction using Permit2 for gasless approval. However, automatic renewals currently require SUBS in your wallet, so keep some SUBS available if you enable auto-renew. See [Payment & Conversion Mechanics](../smart-contract/payment-conversion.md) for the technical flow.

??? question "Q: How do renewals work?"
    Renewals happen automatically when auto-renewal is enabled and your wallet has enough SUBS (plus a small amount of ETH for gas). The smart contract processes the payment at the scheduled renewal date. If your wallet lacks sufficient funds, the renewal fails and your subscription expires — but you can re-subscribe at any time. See the [Subscriber Guide](../dapp/subscriber-guide.md) for details.

??? question "Q: Can I cancel my subscription?"
    Yes, you can cancel at any time by disabling auto-renewal through the dApp or by simply not renewing when the current billing period ends. Your access continues until the end of the paid period. No one can charge your wallet without your explicit on-chain approval. See [Getting Started for Subscribers](../getting-started/for-subscribers.md).

??? question "Q: What if a merchant changes the subscription price?"
    Your existing subscription continues at the original price until your next renewal. When a merchant changes the subscription amount, all linked subscriptions with auto-renewal enabled have `isRecurring` set to false and `remainingCycles` reset to zero as a safety measure. You must manually re-enable auto-renewal to continue at the new price, preventing silent price increases. See [Core Logic](../smart-contract/core-logic.md) for the full lifecycle details.

??? question "Q: Are there any fees on my side as a subscriber?"
    The 1% platform fee is deducted from the merchant's share, not yours. As a subscriber, you pay only the listed subscription price plus a small Arbitrum gas fee (typically $0.01-$0.05 per transaction). There are no hidden charges.

---

## For Merchants

??? question "Q: How do I start accepting subscriptions?"
    You can start in minutes by connecting your wallet at [app.subscrypts.com](https://app.subscrypts.com){ target=_blank } and creating a subscription plan, or by adding the Subscrypts Discord Bot to your server for community monetization. Both paths require only a wallet with a small amount of ETH on Arbitrum One for gas. See [Getting Started for Merchants](../getting-started/for-merchants.md) for the full walkthrough.

??? question "Q: How much does it cost to use Subscrypts as a merchant?"
    Subscrypts charges a 1% platform fee on each subscription payment — no monthly fees, no setup costs, and no minimum volume requirements. The fee is expressed in basis points (100 bps = 1%) and is capped at a maximum configurable value of 5% (500 bps), though it is currently set at 1%. You receive 99% of every payment, settled instantly in the same on-chain transaction.

??? question "Q: How does payment settlement work?"
    All payments settle through a burn-and-mint mechanism in the SUBS token. When a subscriber pays, the smart contract burns the payment amount from the subscriber's wallet, then mints 99% to your merchant wallet and 1% to the protocol treasury — all in a single atomic transaction. Funds arrive instantly and are verifiable on [Arbiscan](https://arbiscan.io){ target=_blank }. See [Payment & Conversion Mechanics](../smart-contract/payment-conversion.md).

??? question "Q: Can I price my plans in US dollars?"
    Yes, you can create USD-denominated plans. The smart contract uses the Uniswap V3 Quoter to calculate the equivalent SUBS amount at the real-time market rate when each payment occurs. Your subscribers always pay the USD-equivalent value, providing predictable pricing regardless of SUBS price fluctuations. See [Getting Started for Merchants](../getting-started/for-merchants.md) for pricing guidance.

??? question "Q: How do I monetize a Discord community?"
    Add the Subscrypts Discord Bot to your server, run the baseline setup, create a subscription plan, and map it to premium Discord roles. The bot automatically grants and revokes roles based on on-chain subscription status. For the full guide, see [Discord Bot Admin Setup Guide](../discord-bot/admin-setup-guide.md).

??? question "Q: Can I convert my SUBS revenue to stablecoins or fiat?"
    Yes, you can swap SUBS to USDC at any time using the dApp's built-in swap page, any Uniswap interface on Arbitrum, or bridge to Ethereum mainnet for withdrawal through a centralized exchange. See [Getting Started for Merchants](../getting-started/for-merchants.md) for off-ramping details.

---

## For Developers

??? question "Q: What integration options are available?"
    Three integration paths are supported: the React SDK (`@subscrypts/subscrypts-sdk-react`) for drop-in components and hooks, direct ABI calls with ethers.js for non-React apps, and event-based backend integration by listening to on-chain events such as `_subscriptionCreate` and `_subscriptionPay`. See [Getting Started for Developers](../getting-started/for-developers.md) for code examples of each approach.

??? question "Q: What is the smart contract architecture?"
    The Subscrypts Smart Contract Suite uses a hybrid UUPS proxy with four modular facets: FacetSubscription (plans and renewals), FacetPaymentUSDC (USDC quoting and swaps), FacetAdmin (governance and halt states), and FacetView (read-only queries). All facets share a single SubscryptsStorage layer accessed via delegatecall through the proxy. The proxy follows ERC-1967 storage slots. See [Architecture Overview](../smart-contract/architecture.md) for the full design.

??? question "Q: How do I check if a user has an active subscription?"
    Call the `getPlanSubscription(planId, subscriberAddress)` read-only function on the proxy contract. A subscription is active when its `nextPaymentDate` is greater than the current block timestamp. Using the React SDK, the `useSubscriptionStatus(planId)` hook returns `isActive` directly. See [ABI Reference](../smart-contract/abi-reference.md) and [Getting Started for Developers](../getting-started/for-developers.md).

??? question "Q: What events should I listen to for access control?"
    The key events for access control are `_subscriptionCreate` (new subscription), `_subscriptionPay` (payment processed), `_subscriptionStop` (subscription expired or failed renewal), and `_subscriptionRecurring` (auto-renewal toggled). You can also query `FacetView` functions directly for state validation when events are missed. See [Events & Integrations](../smart-contract/events-integrations.md).

??? question "Q: Can the smart contract be upgraded?"
    Yes, the contract uses the UUPS (Universal Upgradeable Proxy Standard) pattern which allows logic upgrades while preserving all stored data. Individual facets can be replaced independently without redeploying the entire suite. All upgrades emit `Upgraded` and `FacetSelectorUpdated` events on-chain and require strict role-based authorization. See [Design Philosophy](../smart-contract/design.md) for upgrade safeguards.

---

## Token & Investment

??? question "Q: What is the SUBS token?"
    SUBS is an ERC-20 utility token deployed on Arbitrum One (chain ID 42161) that serves as the settlement and access token for all subscription services in the Subscrypts ecosystem. It does not represent equity, ownership, voting rights, or dividends — its value is derived exclusively from platform usage and demand. See [Tokenomics](../subscrypts/tokenomics.md).

??? question "Q: What is the total supply of SUBS?"
    The total supply of SUBS is 120 million tokens, all minted at the Token Generation Event (TGE). This represents a fixed supply cap for all practical purposes. While the smart contract retains the technical capability to mint or burn tokens, any such change would require multi-signature approval, on-chain governance, and regulatory disclosure. See [Tokenomics](../subscrypts/tokenomics.md) for the full allocation breakdown.

??? question "Q: How is the token distributed?"
    The 120 million SUBS supply is allocated as follows: 40% Public Sale (IDO), 15% Marketing & Partnerships, 15% Treasury & Operations, 15% Development Fund, 10% Founder, and 5% Ecosystem Reserve. Only 12.5% (15 million SUBS) enters circulation at TGE, with the rest released through multi-year vesting schedules. See [Public Sale (IDO)](../subscrypts/public-sale.md) for the vesting timeline.

??? question "Q: Where can I buy SUBS?"
    SUBS is available through the Initial DEX Offering (IDO) on Uniswap V3 on Arbitrum One, paired with USDC. After launch, it can be traded on any decentralized exchange that supports the token on Arbitrum. You can also use the swap page on the [Subscrypts dApp](https://app.subscrypts.com){ target=_blank } to convert USDC or ETH to SUBS. See [Public Sale (IDO)](../subscrypts/public-sale.md).

??? question "Q: Is SUBS a security or investment product?"
    SUBS is classified as a utility token under the EU Markets in Crypto-Assets Regulation (MiCAR). It is not a security, e-money token, or asset-referenced token and does not confer ownership, profit-sharing, or governance rights. The token may lose its value in part or in full, and no return or appreciation is promised. See [Compliance](../subscrypts/compliance.md) for the full regulatory classification and risk warnings.

??? question "Q: What risks should I be aware of?"
    Purchasing or holding SUBS carries risks including potential loss of value, limited liquidity (especially in early stages), dependency on platform adoption, smart contract vulnerabilities, and evolving regulatory requirements. SUBS tokens are not covered by investor compensation or deposit guarantee schemes. Read the full risk disclosure in the [Compliance](../subscrypts/compliance.md) section and the [Subscrypts Whitepaper](https://subscrypts.com/whitepaper){ target=_blank }.
