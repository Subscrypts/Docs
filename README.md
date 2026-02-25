# Subscrypts Documentation

Official documentation for the [Subscrypts](https://subscrypts.com) ecosystem — a decentralized subscription platform built on Arbitrum One.

**Live site: [docs.subscrypts.com](https://docs.subscrypts.com)**

---

## What's Covered

| Section | Description |
|---------|-------------|
| [Subscrypts](https://docs.subscrypts.com/subscrypts/) | Introduction, vision, architecture, tokenomics, and roadmap |
| [Smart Contract](https://docs.subscrypts.com/smart-contract/) | Contract design, core logic, security, ABI reference, and deployment |
| [dApp](https://docs.subscrypts.com/dapp/) | Features, wallet connection, swap guide, and merchant dashboard |
| [Discord Bot](https://docs.subscrypts.com/discord-bot/) | Setup guide, slash commands, role management, and security |
| [SDK](https://docs.subscrypts.com/sdk/) | React SDK quick start, hooks, components, and code examples |
| [Resources](https://docs.subscrypts.com/resources/) | FAQ, glossary, comparisons, and crypto subscription guide |

---

## Tech Stack

- **[MkDocs Material](https://squidfunk.github.io/mkdocs-material/)** — static site generator with Material Design theme
- **Python 3.12** — build and server runtime
- **Docker** — containerized deployment

---

## Building Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Build and validate (strict mode — warnings are errors)
mkdocs build --strict

# Preview locally
mkdocs serve
```

The built site is output to the `site/` directory.

---

## Links

- **Website**: [subscrypts.com](https://subscrypts.com)
- **dApp**: [app.subscrypts.com](https://app.subscrypts.com)
- **X (Twitter)**: [@Subscrypts_com](https://x.com/Subscrypts_com)
- **Discord**: [discord.gg/subscrypts](https://discord.gg/subscrypts)
- **Arbiscan**: [0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac](https://arbiscan.io/address/0xE2E5409C4B4Be5b67C69Cc2C6507B0598D069Eac)

---

© 2025–2026 Subscrypts. All rights reserved. The documentation content in this repository is proprietary. The source code files (build tooling, server, hooks) are provided for reference. Reproduction of the documentation content without permission is not permitted.
