# 🔑 Key Logger

> A Python-based keystroke logger built for **educational purposes** as part of the **Arch Technologies Cybersecurity Internship** — Month 2.
> Demonstrates how input-capture attacks work at the OS level and maps to **MITRE ATT&CK T1056.001**.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Library](https://img.shields.io/badge/Library-pynput-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square)
![MITRE](https://img.shields.io/badge/MITRE%20ATT%26CK-T1056.001-red?style=flat-square)
![License](https://img.shields.io/badge/License-Educational%20Only-orange?style=flat-square)

</div>

---

## ⚠️ Disclaimer

> **This project is strictly for educational and research purposes.**
> Deploying keyloggers on systems without explicit written consent is **illegal** under computer-misuse and privacy laws in most jurisdictions.
> All testing must be performed **only on machines you own or have written permission to test**.
> The author takes no responsibility for any misuse of this code.

---

## 📖 About

This project was built as **Task 2** of the Arch Technologies Cybersecurity Internship. It simulates a basic keylogger in a controlled, safe lab environment to understand:

- How **keystroke interception** works at the OS level
- How **special keys** (Space, Shift, Enter) are handled and normalised
- How **append-mode file persistence** accumulates a credential log
- Why **endpoint detection controls** specifically monitor input-hooking API calls

The script uses Python's `pynput` library to hook into the OS keyboard API, captures every key press, maps special keys to human-readable characters, and silently appends each keystroke to a local `log.txt` file.

---

## 🎯 MITRE ATT&CK Mapping

| Field | Detail |
|---|---|
| **Tactic** | Collection — TA0009 |
| **Technique** | Input Capture — T1056 |
| **Sub-technique** | Keylogging — T1056.001 |
| **Platform** | Windows, Linux, macOS |
| **Privilege Required** | User-level (no root/admin needed) |

---

## 🗂️ Project Structure

```
Key-Logger/
│
├── main.py          # Keylogger script — listener, callback, file I/O
├── log.txt          # Generated at runtime — captured keystrokes
└── README.md        # Project documentation
```

---

## ⚙️ How It Works

```
Program Start
     │
     ▼
Import pynput.Listener
     │
     ▼
Define storeToFile(key) callback
     │
     ▼
Register OS keyboard hook  ──────────────────────────────────────┐
     │                                                           │
     ▼                                                           │
l.join()  ← blocking wait                                        │
     │                                                           │
     ▼                                                           │
Key Press Event                                                   │
     │                                                           │
     ▼                                                           │
  str(key) → strip quotes                                        │
     │                                                           │
     ├── Key.space  → ' '                                        │
     ├── Key.shift  → '' (ignored)                              │
     ├── Key.enter  → '\n'                                       │
     └── others     → raw string                                 │
     │                                                           │
     ▼                                                           │
Append to log.txt ───────────────────────────────────────────────┘
     │
  Ctrl+C
     │
     ▼
Listener exits → log.txt saved
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `pynput` library

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Lak-MedRida027/Key-Logger.git
cd Key-Logger

# 2. Install the required dependency
pip install pynput
```

### Usage

```bash
# Run the keylogger
python main.py

# The script runs silently — type anything
# All keystrokes are written to log.txt

# Stop the keylogger
# Press Ctrl+C in the terminal

# View captured keystrokes
cat log.txt        # Linux / macOS
type log.txt       # Windows
```

### Example Output (`log.txt`)

```
Hello World
This is a test sentence.
password123
```

---

## 🔍 Key Handling

| Raw Key Code | Logged As | Notes |
|---|---|---|
| `'a'`, `'1'`, `'@'` | Character itself | Quotes stripped automatically |
| `Key.space` | ` ` (space) | Preserves word boundaries |
| `Key.shift` | *(empty)* | Modifier only — ignored |
| `Key.enter` | `\n` (newline) | Represents end of a typed line |
| `Key.backspace`, `Key.f1`, etc. | `Key.<name>` | Raw string — all others logged as-is |

---

## 🛡️ Detection & Mitigation

Understanding how to **detect** this technique is the primary goal of this exercise.

**Detection Methods:**
- Monitor for unexpected Python processes with persistent runtime
- Audit repeated small file writes to `.txt` files by non-editor processes
- Flag `SetWindowsHookEx` API calls on Windows from unknown processes
- Use EDR/AV solutions that detect `pynput` and similar input-hooking libraries at install time

**Mitigation Strategies:**
- Deploy Endpoint Detection & Response (EDR) agents
- Apply application whitelisting on corporate endpoints
- Enforce the principle of least privilege for all user accounts
- Enable Multi-Factor Authentication (MFA) to limit credential-theft impact

---

## 📦 Dependencies

| Library | Version | Purpose |
|---|---|---|
| `pynput` | Latest | Cross-platform keyboard/mouse listener |

Install all dependencies:

```bash
pip install pynput
```

---

## 📄 Internship Report

A full technical report for this project was prepared as part of the Arch Technologies internship submission, covering:
- Project overview and scope
- MITRE ATT&CK mapping
- Module architecture
- Step-by-step execution flow diagram
- Full source code walkthrough
- Security analysis and detection methods

---

## 👤 Author

**Mohammed Rida Lakhdari**

- 🎓 Information Security Engineering Student — University of Batna 2
- 🏢 Cybersecurity Intern — Arch Technologies
- 💼 [LinkedIn](https://www.linkedin.com/in/mohammed-rida-lakhdari)
- 📧 lakmedrida027@gmail.com

---

## 🔗 Related Projects

- [Network Packet Sniffer](https://github.com/Lak-MedRida027/Network-Packet-Sniffer) — Month 1 internship project
- [Multi-Services Honeypot](https://github.com/Lak-MedRida027/Multi-Services-Honeypot) — University module project

---

<div align="center">

**⭐ Star this repo if you found it useful for learning!**

*Built for learning. Use responsibly.*

</div>
