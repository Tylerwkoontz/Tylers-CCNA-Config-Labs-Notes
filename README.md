# 🚀 Tyler's CCNA Lab Hub & Interactive Study Suite

[![CCNA 200-301 v1.1](https://img.shields.io/badge/Exam-CCNA%20200--301%20v1.1-0284c7.svg?style=for-the-badge&logo=cisco)](https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html)
[![Pure HTML Architecture](https://img.shields.io/badge/Architecture-100%25%20Pure%20HTML%2FCSS%2FJS-10b981.svg?style=for-the-badge&logo=html5)](https://html.spec.whatwg.org/)
[![CML 2.10 Ready](https://img.shields.io/badge/Lab%20Infra-CML%202.10%20Automation-581c87.svg?style=for-the-badge&logo=cisco)](https://developer.cisco.com/modeling-labs/)
[![GitHub Pages Ready](https://img.shields.io/badge/Deployment-GitHub%20Pages-f59e0b.svg?style=for-the-badge&logo=github)](https://pages.github.com/)

A modern, standalone interactive web suite and automated Cisco Modeling Labs (CML 2.10) environment designed for mastering the **Cisco CCNA 200-301 (v1.1)** certification.

Built with a **zero-dependency pure HTML architecture**, this repository features 11 comprehensive, spoiler-free performance-based lab workbooks, responsive multi-tier SVG topologies, mental subnetting drills, and automated CML REST API provisioning scripts.

---

## 🌐 Live Interactive Dashboard (GitHub Pages)

You can host and access the entire interactive suite directly in any web browser via **GitHub Pages**:

👉 **Live URL**: `https://tylerwkoontz.github.io/Tylers-CCNA-Config-Labs-Notes/`

---

## 🧪 Interactive Lab Catalog & Blueprint Mapping

Each lab is structured as an authentic **CCNA Performance-Based Question (Simlet)** with business scenarios, specification tables, pre-solution verification steps, and spoiler-free collapsible solution drawers.

| Lab # | Lab Title | CCNA 200-301 Domain | Primary Blueprint Focus | CML YAML Template |
| :--- | :--- | :--- | :--- | :--- |
| **Lab 01** | **[TCP/IP Encapsulation & Headers](labs/lab01-tcp-ip-encapsulation.html)** | `1.1`, `1.4`, `1.5` | 5-Layer Encapsulation, TCP 3-Way Handshake & Frame Deconstruction | [`cml-templates/lab01...yaml`](cml-templates/lab01-tcp-ip-encapsulation.yaml) |
| **Lab 03** | **[Packet Delivery & ARP Resolution](labs/lab03-packet-delivery-arp.html)** | `1.1`, `1.3`, `3.1` | Local vs Remote Subnet ARP Resolution & Router MAC Rewrites | [`cml-templates/lab03...yaml`](cml-templates/lab03-packet-delivery-arp.yaml) |
| **Lab 03B**| **[Multi-Hop Routed WAN & Framing](labs/lab03b-routed-wan-headers.html)** | `1.1`, `1.2`, `3.1` | Point-to-Point WAN Framing, Static Routing & TTL Hop Analysis | [`cml-templates/lab03b...yaml`](cml-templates/lab03b-routed-wan-headers.yaml) |
| **Lab 04** | **[Cisco IOS CLI & Memory Architecture](labs/lab04-cli-navigation-memory.html)** | `2.8`, `5.5` | EXEC Modes, Submodes, History Buffers & RAM/NVRAM Persistence | [`cml-templates/lab04...yaml`](cml-templates/lab04-cli-navigation-memory.yaml) |
| **Lab 06** | **[Switch Management & Hardened SSH](labs/lab06-switch-management-ssh.html)** | `1.1`, `2.1`, `5.5` | SVI VLAN 1 IP, Default Gateway, RSA Key Gen & SSH v2 Enforcement | [`cml-templates/lab06...yaml`](cml-templates/lab06-switch-management-ssh.yaml) |
| **Lab 06B**| **[Cross-Subnet Switch Management](labs/lab06b-cross-subnet-management.html)** | `1.1`, `2.8`, `3.1` | `ip default-gateway` Fault Isolation & Remote NOC Administration | [`cml-templates/lab06b...yaml`](cml-templates/lab06b-cross-subnet-management.yaml) |
| **Lab 07** | **[Switch Interfaces & MAC Table](labs/lab07-switch-interfaces-mac-table.html)** | `1.13`, `2.1`, `2.4` | Port Speed/Duplex Locking, Dynamic MAC Learning & Static Mapping | [`cml-templates/lab07...yaml`](cml-templates/lab07-switch-interfaces-mac-table.yaml) |
| **Lab 07B**| **[Interface Diagnostics & Duplex](labs/lab07b-interface-diagnostics-duplex.html)** | `1.4`, `2.4` | Parallel Detection Mismatches, Late Collisions vs CRC Isolation | [`cml-templates/lab07b...yaml`](cml-templates/lab07b-interface-diagnostics-duplex.html) |
| **Lab 09** | **[STP Root Election & Path Cost](labs/lab09-stp-root-election-path-cost.html)** | `2.5` | 802.1D Bridge ID Hierarchy, Deterministic Root Election & Cost Tuning | [`cml-templates/lab09...yaml`](cml-templates/lab09-stp-root-election-path-cost.yaml) |
| **Lab 09B**| **[STP Parallel Links & Timers](labs/lab09b-stp-port-priority-timers.html)** | `2.5` | Parallel Link Tiebreakers, Sender Port Priority & Timer Tuning | [`cml-templates/lab09b...yaml`](cml-templates/lab09b-stp-port-priority-timers.yaml) |
| **Lab 17** | **[Multi-Subnet IPv4 Routing](labs/lab17-multi-subnet-routing.html)** | `1.6`, `3.1`, `3.3` | VLSM Subnet Calculations (/26, /27, /30) & Static Route Verification | [`cml-templates/lab17...yaml`](cml-templates/lab17-multi-subnet-routing.yaml) |

---

## ✨ Architectural Features & Design Highlights

### 1. Pure HTML / Zero-Build Architecture
* **Single-File Standalone Workbooks**: Every lab workbook in `labs/` runs completely offline with zero external NPM packages, node servers, or heavy frameworks.
* **100% Mobile & Print Friendly**: Embedded `@media print` stylesheets allow instant 1-click **Print to PDF** for offline binder study.

### 2. Standard Cisco Hierarchical Topology Diagrams
* All network topology diagrams are embedded as vector SVGs following standard **Cisco Multi-Tier Enterprise Design**:
  * 🏢 **Distribution & Gateway Tier (Top)**: Default gateway routers and SVIs.
  * 🔀 **Access Switching Tier (Middle)**: Layer 2 Catalyst switches.
  * 💻 **Host & Endpoint Tier (Bottom)**: Endpoints, clients, servers, and console management stations.

### 3. Exam Simulation Standard (Zero Spoilers)
* Tasks are written strictly as **specification-driven requirements** requiring you to recall and enter Cisco IOS commands from memory.
* Verified solution configurations and 1-click **Copy Config** buttons are safely locked inside collapsible `<details class="card solution-drawer">` elements.
* Every solution includes an **Engineering Deep-Dive & Exam Pitfalls** section analyzing common exam traps, enterprise security standards, and packet flow mechanics.

### 4. Interactive Mental Subnetting Speed Trainer
* Built right into the master dashboard (`index.html`):
  * **Class C Mode**: `/24` through `/30` (Magic numbers 4, 8, 16, 32, 64, 128).
  * **Class B Mode**: `/16` through `/23`.
  * **Class A Mode**: `/8` through `/15`.
  * Real-time score and streak counter to develop instantaneous mental subnet calculations.

---

## ⚡ Cisco Modeling Labs (CML 2.10) & Ubuntu Workflow Reference

This repository is optimized for a **zero-touch background workflow** on Ubuntu. You never have to manually manage proxies or remember port mappings.

---

### 🚀 1. The Daily Command Cheat Sheet (`~/.zshrc`)

| Command | Action | Description |
| :--- | :--- | :--- |
| **`cml-con`** | Interactive Menu | Shows active labs; select a lab to open its side-by-side **Split Grid** |
| **`cml-con 09b`** | Lab Split Grid | **Launches all 4 devices for Lab 09B side-by-side in a 2x2 grid** |
| **`cml-con SW1`** | Direct Connect | Instantly connects straight to `SW1` console in your current shell |
| **`cml-con all`** | Full Grid | Launches a multi-pane split grid across all running lab nodes |
| **`cml-labs`** | List Topologies | Queries `cml-controller.internal` for active and stopped lab IDs |
| **`cml-ui`** | Breakout Dashboard | Opens Web UI at `http://127.0.0.1:8080` for **1-click live Wireshark captures** |
| **`cml-dash`** | HTML Study Hub | Launches your master interactive CCNA workbook dashboard |



---

### 🔌 2. Zero-Touch Background Service (`systemd`)

The CML Breakout Tool runs as an automated background user daemon (`cml-breakout.service`) on your workstation:
* **Starts on Boot**: The proxy is always running quietly in the background on ports `9000+`.
* **Zero Manual Steps**: You never have to keep a dedicated terminal tab open for `./start-breakout.sh`.
* **Service Controls** (if ever needed):
  ```bash
  systemctl --user status cml-breakout   # Check proxy status
  systemctl --user restart cml-breakout  # Force re-sync with CML
  systemctl --user stop cml-breakout     # Stop background proxy
  ```

---

### 🧪 3. Lab Lifecycle & Switching Labs

When you switch between different CCNA chapters (e.g. from Lab 09 STP to Lab 06 SSH):
```bash
# 1. Stop old lab & start new lab (auto-syncs breakout ports in the background)
python3 scripts/cml_client.py stop <old-uuid>
python3 scripts/cml_client.py start <new-uuid>

# 2. Connect immediately to new devices!
cml-con          # Menu will now list the newly started lab nodes
cml-con all      # Opens all new lab nodes in tabs
```
* Existing terminal sessions will cleanly show `Connection closed by foreign host`.
* The background service automatically detects the new lab nodes and maps fresh ports.

---

### 🚪 4. Terminal Escape / Disconnect Shortcut

To cleanly exit any Cisco console session without closing your terminal window:
1. Press **`Ctrl + ]`** (Hold `Ctrl` and tap `]`).
2. Type **`quit`** (or `q`) and press `Enter`.
3. *(Alternative)* Press **`Ctrl + Shift + W`** to close the active tab.

---

### 🦈 5. Live Wireshark Packet Sniffing

To capture live traffic (STP BPDUs, ARP resolution, TCP 3-way handshakes) directly in native Ubuntu Wireshark:
1. Run `cml-ui` and open `http://127.0.0.1:8080`.
2. Click the **Wireshark** icon next to any interface or link.
3. Native Wireshark launches immediately on your desktop streaming the live wire traffic.



---

## 🚀 How to Enable GitHub Pages

You can host this entire interactive study portal for yourself and peers for free using GitHub Pages:

1. Push this repository to your GitHub account.
2. In your GitHub repository, navigate to **Settings** &rarr; **Pages** (under Code and automation).
3. Under **Build and deployment**:
   * **Source**: Select `Deploy from a branch`.
   * **Branch**: Select `main` / `root` (`/`).
4. Click **Save**.
5. Within 60 seconds, GitHub will publish your site at `https://<your-username>.github.io/<repo-name>/`.

---

## ⚖️ Legal, Copyright & Open-Source Compliance

### Is it legal and appropriate to host this repository publicly?
**Yes, 100%.** Here is why:

1. **Original Educational Work & Public Standards**:
   * All explanations, SVG network diagrams, problem scenarios, and engineering deep-dive debriefs in this repository are **original educational works**.
   * Network protocols (IPv4, TCP, UDP, Ethernet, ARP, SSH) and Cisco IOS command-line structures are **public industry standards and facts**, which are not subject to copyright restrictions.
2. **No Proprietary Cisco Software Binaries**:
   * This repository contains **only open text files** (HTML, CSS, JS, Python, and YAML topology definitions).
   * It does **NOT** contain or distribute Cisco proprietary operating system image binaries (`.qcow2`, `.bin`, `.vmdk`, or IOL/IOSv images). Users run topologies inside their own legally licensed CML environments.
3. **No Exam Non-Disclosure Agreement (NDA) Violations**:
   * This repository contains **no braindumps or actual exam test questions**.
   * All scenarios are practice engineering exercises designed in accordance with the publicly available Cisco CCNA 200-301 v1.1 Exam Blueprint.

### Trademark Disclaimer
> Cisco, Cisco Systems, CCNA, and Cisco IOS are registered trademarks or trademarks of Cisco Systems, Inc. and/or its affiliates in the United States and certain other countries. This repository is an independent, non-commercial open-source educational study resource and is not affiliated with, sponsored by, or endorsed by Cisco Systems, Inc.
