---
title: ABI & Developer Reference
description: Developer reference for interacting with the Subscrypts Smart Contract Suite, including ABI structure, usage examples, and integration guidance.
tags:
  - smart-contracts
  - abi
  - developer-reference
  - solidity
  - web3
---

Download latest Subscrypts ABI: [https://files.subscrypts.com/abi/subscryptsABI-v1.json](https://files.subscrypts.com/abi/subscryptsABI-v1.json)

---

# ABI & Developer Reference

The **Application Binary Interface (ABI)** defines how external applications interact with the **Subscrypts Smart Contract Suite**. It includes all callable functions, events, and data structures — allowing developers to build integrations using **ethers.js, web3.js, web3.py, viem, web3j (Java), or ethers-rs (Rust)**, or the upcoming **Subscrypts SDK**.

This reference explains how the ABI is structured, how to use it safely, and how versioning ensures long-term compatibility.

---

## ABI Overview

The **Application Binary Interface (ABI)** defines how external applications interact with the **Subscrypts Smart Contract Suite**. It includes all callable functions, events, and data structures — allowing developers to build integrations using **ethers.js, web3.js, web3.py, viem, web3j (Java), or ethers-rs (Rust)**, or the upcoming **Subscrypts SDK**.

Within the **Subscrypts ecosystem**, there are two primary ways of interacting with the protocol:

1. **Through user interfaces** — such as the official **[Subscrypts dApp](https://app.subscrypts.com)**, the **[Discord Bot](https://discord.onsubscrypts.com)**, or other **third-party integrations**. These interfaces abstract the blockchain layer and handle all ABI interactions under the hood, allowing end users to manage subscriptions, payments, and accounts without requiring technical knowledge or direct contract interaction.

2. **Direct on-chain interaction** — for developers and integrators who want to build their own tools, automate operations, or create systems that interact directly with the Subscrypts Smart Contract Suite. In this case, the **ABI is essential**, as it acts as the **blueprint** describing how to call smart contract functions, interpret return data, and listen to emitted events.

The ABI essentially defines the “language” of the smart contract — specifying what functions exist, their expected inputs and outputs, and the structure of all emitted events. Without it, direct communication with the Subscrypts protocol would not be possible.
The ABI is the canonical definition of the Subscrypts protocol’s callable interface. It enables:

* Wallets, dApps, and bots to interact with deployed contracts.
* Developers to access on-chain data via **view functions**.
* Off-chain systems to listen for and react to **events** emitted by the smart contracts

While the Subscrypts source code and bytecode remain private, the verified ABI provides a standardized and secure access layer for all on-chain interactions. This ensures that while the protocol’s internal logic is protected, developers can still integrate Subscrypts into their products in a safe, transparent, and reliable way.

---

## ABI Structure

The Subscrypts ABI contains all callable functions and events from the modular smart contract suite — including **FacetSubscription**, **FacetPaymentUSDC**, **FacetAdmin**, **FacetView**, and the **Proxy Logic** layer.

Example structure:

```json
[
  {
    "type": "function",
    "name": "subscriptionCreate",
    "inputs": [ ... ],
    "outputs": [ ... ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "event",
    "name": "_subscriptionPay",
    "inputs": [ ... ],
    "anonymous": false
  }
]
```

This JSON structure allows any Web3-compatible framework to decode and interact with the contract.

---

## ABI Maintenance and Versioning

The **Subscrypts ABI** follows an independent versioning system to reflect real interface changes. Not every smart contract update modifies the ABI.

A new ABI version will only be released when:

* New external functions or events are added.
* Function signatures or parameter structures change.
* Deprecated functions are removed or replaced.

Each ABI release will include:

* ABI version number (`subscryptsABI-v1`, `v2`, etc.).
* Associated contract release version.
* Change summary and checksum for verification.

Versioned ABIs will be made available in a **public repository** for developers to fetch directly, ensuring reproducibility across builds.

---

## ABI Validation and Integrity

To ensure reliability and prevent mismatches:

* ABIs are auto-generated from verified internal deployments.
* A SHA256 checksum will be published for each ABI file.
* Developers can compare the checksum to confirm authenticity.

By validating ABI integrity, developers can ensure that their integrations always match the active contract logic deployed on-chain — even without access to the private source code or bytecode.

---

## Developer Integration Guide

To integrate Subscrypts contracts in your dApp or backend service:

**Import the ABI**

```js
import subscryptsAbi from "./abi/subscryptsABI-v1.json";
```

**Initialize the Contract**

```js
import { ethers } from "ethers";

const rpcUrl = "https://your-arbitrum-rpc-url";
const provider = new ethers.JsonRpcProvider(rpcUrl);

const contractAddress = "0xYourSubscryptsProxyAddress";
const privateKey = "0xYourPrivateKey"; // never hardcode in production
const signer = new ethers.Wallet(privateKey, provider);

const subscrypts = new ethers.Contract(contractAddress, subscryptsAbi, signer);
```

**Call Functions or Subscribe to Events**

```js
subscrypts.on("_subscriptionPay", (subscriptionId, planId, subscriber, amount, event) => {
  console.log(
   `Payment received — subscriptionId: ${subscriptionId.toString()}, ` +
   `planId: ${planId.toString()}, subscriber: ${subscriber}, ` +
   `amount: ${amount.toString()} SUBS`
  );
  // event.blockNumber, event.transactionHash, etc. are also available
});
```

### End-to-End Example (ethers.js)

The example below shows a minimal, end-to-end flow:

* Connect to the Subscrypts contract
* Fetch plans via view functions
* Create a subscription for a given plan
* React to `_subscriptionCreate` and `_subscriptionPay` events

```js
import { ethers } from "ethers";
import subscryptsAbi from "./abi/subscryptsABI-v1.json";

const rpcUrl = "https://your-arbitrum-rpc-url";
const provider = new ethers.JsonRpcProvider(rpcUrl);

const contractAddress = "0xYourSubscryptsProxyAddress";
const privateKey = "0xYourPrivateKey"; // load from env/secret manager in real apps
const signer = new ethers.Wallet(privateKey, provider);

const subscrypts = new ethers.Contract(contractAddress, subscryptsAbi, signer);

async function main() {
  // 1) Listen for new subscriptions and payments
  subscrypts.on("_subscriptionCreate", (subscriptionId, planId, subscriber, recurring, remainingCycles, referral) => {
    console.log(
      `New subscription — id: ${subscriptionId.toString()}, plan: ${planId.toString()}, ` +
      `subscriber: ${subscriber}, recurring: ${recurring}, remainingCycles: ${remainingCycles.toString()}`
    );
  });

  subscrypts.on("_subscriptionPay", (subscriptionId, planId, subscriber, amount) => {
    console.log(
      `Payment received — subscriptionId: ${subscriptionId.toString()}, planId: ${planId.toString()}, ` +
      `subscriber: ${subscriber}, amount: ${amount.toString()} SUBS`
    );
  });

  // 2) Query first batch of plans via FacetView-compatible function
  const indexStart = 0n;
  const indexEnd = 10n;
  const plans = await subscrypts.getPlans(indexStart, indexEnd);
  console.log("Plans:", plans);

  if (plans.length === 0) {
    console.log("No plans available yet.");
    return;
  }

  // 3) Pick the first plan and create a subscription
  const planId = plans[0].id ?? plans[0][0]; // depending on ABI struct decoding
  console.log(`Creating subscription for planId: ${planId.toString()}`);

  const tx = await subscrypts.subscriptionCreate(planId);
  const receipt = await tx.wait();

  console.log("subscriptionCreate tx hash:", receipt.hash);
}

main().catch(console.error);
```

---

## Summary

The ABI is the **core access layer** of the Subscrypts ecosystem — acting as the technical blueprint for how external systems, dApps, and services communicate with the Subscrypts Smart Contract Suite. It defines every callable function, view endpoint, and event signature, ensuring that developers can interact directly with the protocol in a standardized, verifiable way.

By offering **versioned and publicly available ABI releases**, Subscrypts enables developers to build integrations that remain compatible across upgrades while maintaining security and consistency. The ABI ensures that interactions between wallets, bots, analytics platforms, and backend services remain transparent, reliable, and future-proof — without exposing the proprietary source code or bytecode.

Through this structured interface, Subscrypts bridges the gap between **on-chain logic** and **off-chain innovation**, empowering developers to integrate subscription-based Web3 services with confidence and precision.
