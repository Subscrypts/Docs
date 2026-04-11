---
title: Installing Subscrypts Pulse
description: How to install Subscrypts Pulse as a PWA on iOS, Android, and desktop browsers — no app store required.
status: new
tags:
  - subscrypts
  - pulse
  - pwa
  - installation
  - mobile
  - desktop
---

# Installing Subscrypts Pulse

Subscrypts Pulse is a **Progressive Web App (PWA)** — a web application that can be installed directly on your device and used like a native app, without downloading anything from an app store.

---

## What Is a PWA?

A Progressive Web App is a website that behaves like a native application:

* **Installable** — Add it to your home screen or taskbar
* **Standalone** — Opens in its own window, without a browser address bar
* **Push notifications** — Receives alerts even when the app is closed
* **Offline capable** — Cached data is available without an internet connection
* **Always up to date** — Updates automatically, no manual app store updates needed

PWAs require **fewer permissions** than native apps. Because Pulse runs in a browser sandbox, it cannot access your files, contacts, camera, or other device resources unless you explicitly grant permission. This makes it **more privacy-friendly** than a traditional app store download.

---

## Installing on iOS (Safari)

1. Open **Safari** on your iPhone or iPad
2. Navigate to [pulse.subscrypts.com](https://pulse.subscrypts.com)
3. Tap the **Share** button (the square with an upward arrow)
4. Scroll down and tap **Add to Home Screen**
5. Give it a name (or keep the default "Subscrypts Pulse") and tap **Add**

Pulse now appears on your home screen as an app icon. When opened, it runs in standalone mode — full screen, no Safari address bar.

!!! info "iOS Notifications"
    Push notifications on iOS require iOS 16.4 or later. After installing the PWA, enable notifications when prompted during the onboarding wizard.

---

## Installing on Android (Chrome)

1. Open **Chrome** on your Android device
2. Navigate to [pulse.subscrypts.com](https://pulse.subscrypts.com)
3. Chrome may show an **"Install app"** banner at the bottom — tap **Install**
4. If no banner appears:
    * Tap the **three-dot menu** (⋮) in the top right
    * Tap **Install app** or **Add to Home Screen**
5. Confirm the installation

Pulse now appears in your app drawer and home screen like any other app. Push notifications work immediately.

---

## Installing on Desktop (Chrome / Edge)

1. Open **Chrome** or **Edge** on your computer
2. Navigate to [pulse.subscrypts.com](https://pulse.subscrypts.com)
3. Look for the **install icon** in the address bar (a monitor with a down arrow, or a "+" icon)
4. Click it and confirm the installation

Pulse opens in its own window, separate from your browser. It appears in your taskbar and can be pinned for quick access.

---

## First-Time Setup (Onboarding)

When you first open Pulse, a four-step onboarding wizard guides you through setup:

1. **Welcome** — Introduction to Subscrypts Pulse
2. **Read-Only & Secure** — Explains the custodian-free model (no private keys needed)
3. **Stay Informed** — Overview of push notification benefits
4. **Add Your Wallet** — Enter your first wallet address to start monitoring

After completing onboarding:

* The app requests **push notification permission** — allow this to receive alerts
* You're taken to the dashboard, which begins loading your subscription data

!!! tip "Skip and Set Up Later"
    You can skip the onboarding wizard and set up your wallet later in Settings. However, you'll need at least one wallet address to see any data.

---

## Updating Pulse

Pulse updates automatically — no app store visits required. When a new version is deployed:

* The service worker detects the update
* New content is cached in the background
* The next time you open Pulse, you're running the latest version

---

## Uninstalling

### iOS
Long-press the Pulse icon on your home screen and select **Remove App**.

### Android
Long-press the Pulse icon, then select **Uninstall** or drag it to the **Remove** area.

### Desktop
Right-click the Pulse icon in your taskbar or applications menu and select **Uninstall**.

To also **delete your data** from Pulse's servers, use the **Unregister Device** option in Settings before uninstalling. This triggers a complete data erasure. See [Privacy & Data](privacy-and-data.md) for details.

---

## Related Topics

- [Features & Dashboard](features.md) -- What you'll see after installation
- [Push Notifications](notifications.md) -- Configure your notification preferences
- [Wallet Management](wallet-management.md) -- Add wallets to start monitoring
- [Privacy & Data](privacy-and-data.md) -- Data handling and unregistration
