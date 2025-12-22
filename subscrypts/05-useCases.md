---
title: Use Cases
description: Practical, real-world use cases showing how Subscrypts supports SaaS, media, IoT, gaming, and online communities through decentralized subscription payments.
tags:
  - use cases
  - subscription
  - web3
  - SaaS
  - media
  - gaming
  - IoT
  - communities
---

# Use Cases

[Subscrypts](https://subscrypts.com) can be integrated into virtually any application or service layer capable of communicating with the blockchain. Whether you're working in **JavaScript**, **Python**, **Java**, **Go**, **Rust**, or **TypeScript**, you can connect to the [Subscrypts](https://subscrypts.com) protocol using standard Web3 libraries such as **ethers.js**, **web3.js**, **web3.py**, **viem**, **web3j** (Java), or **ethers-rs** (Rust).

Integration can be direct — embedding smart contract calls in your frontend/backend — or via middleware like Node.js, Python, or cloud services that listen for events or manage user state. Developers can:

* React to on-chain events (`OnSubscribed`, `subscriptionPay`, `subscriptionStop`) to automate access control.
* Query subscription states per Ethereum address, subscription, or all subscription records.
* Build dashboards or analytics tools to track renewals, churn, and payment failures.

Thanks to [Subscrypts](https://subscrypts.com)’ modular, event-driven design, integrations scale from browser-based apps and SaaS dashboards to IoT firmware and game servers. Wherever your stack can interface with the blockchain, [Subscrypts](https://subscrypts.com) enables programmable, trustless recurring payments.

---

## Online Communities

**Scenario:** A global gaming and art community offers a premium tier at **50 SUBS/month**, but faces:

* High fees on Patreon/PayPal.
* Payment exclusion in Africa/Asia.
* Pseudonymous members wary of personal data and linking identities.

**Subscrypts Solution:**

* Deploy subscription plans with [Subscrypts Discord Bot](https://discord.onsubscrypts.com) integration.
* Members link their Ethereum wallet to Discord.
* The Discord bot checks on-chain status and assigns roles based on subscription.
* Failed or expired subscriptions revoke access to gated channels.

**Added Value:**

* No chargebacks or fraud.
* Automated, on-chain access control.
* Privacy-respecting and borderless.

> A user in Vietnam subscribes without a bank account. They cancel/resume at will, retaining full control and privacy.

---

## Online Gaming

**Scenario:** A game studio offers premium features at **$10/month**. Traditional payments are expensive or inaccessible in some regions.

**Subscrypts Solution:**

* Players subscribe via a custom paywall and authorize a contract for 12 billing cycles.
* Game backend reacts to `subscriptionPay` and `subscriptionStop` events.
* SUBS-based subscription logic is embedded in the web launcher.

**Outcomes:**

* Higher net revenue (~99% retention on SUBS vs. ~70% via app stores).
* Reduced churn and fraud.
* Transparent subscriber history and optional blockchain-based perks.

---

## SaaS Subscriptions

**Scenario:** A SaaS company charges **$50/user/month** for a project management platform. Payment failures, regional taxes, and card fees reduce margin.

**Subscrypts Solution:**

* Publish a [Subscrypts](https://subscrypts.com) plan denominated in $50/month worth of SUBS.
* Clients subscribe and pre-approve their wallet.
* Each billing cycle pulls SUBS equivalent to the fiat value.
* Events like `subscriptionStop` notify of failed renewals.
* Volume licenses via multi-user plans (on roadmap).

**Benefits:**

* Lower fees (1% vs. 3–5%).
* Seamless onboarding globally.
* Fully auditable transaction history.

> A client in Argentina pays via [Subscrypts dApp](https://app.subscrypts.com), avoiding currency blocks and reducing churn.

---

## Streaming Media

**Scenario:** A niche streaming platform charges **$5/month**. Many users in Southeast Asia and Africa are excluded by legacy payments.

**Subscrypts Solution:**

* Integrate [Subscrypts](https://subscrypts.com)-powered crypto checkout.
* Users pay with SUBS or USDC (atomically converted to SUBS).
* Access is granted while subscription is active on-chain.

**Enhancements:**

* USDC conversion enables non-SUBS holders to subscribe easily.
* Real-time access control via chain status.
* Expands reach to unbanked or underbanked users.

> A Nigerian viewer pays using SUBS from a mobile wallet. Streaming access is immediate.

---

## IoT & Smart Devices

**Scenario:** An EV maker monetizes premium features like fast charging ($20/month) and autopilot ($100/month) via subscriptions.

**Subscrypts Solution:**

* Vehicle or companion app connects to wallet.
* SUBS payments are triggered monthly by the vehicle or app.
* Dashboard displays live subscription status from-chain.

**Forward-Looking Extensions:**

* Machine-to-machine (M2M) billing for autonomous fleets.
* Wallet-embedded IoT devices handle their own subscriptions.

> A logistics firm’s EV fleet auto-subscribes to data feeds and charging networks — no human input required.

---

## Summary

These examples highlight [Subscrypts](https://subscrypts.com)’ flexibility across:

* **Industries** (SaaS, gaming, media, IoT).
* **Pricing models** (fixed SUBS or fiat-equivalent).
* **Subscribers** (individuals, businesses, machines).

By combining crypto-native programmability with global accessibility, [Subscrypts](https://subscrypts.com) creates new revenue paths and unlocks markets underserved by traditional billing platforms.
