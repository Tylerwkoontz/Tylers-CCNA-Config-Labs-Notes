# Tyler's CCNA Study & Lab Hub (Local-First Edition)

A high-efficiency, private study and lab environment for the **Cisco Certified Network Associate (CCNA 200-301 v1.1)**.

---

## 🚀 Quick Start & Daily Usage

### 1. Open the Visual Dashboard in Your Browser
```bash
~/ccna-study/open-dashboard.sh
```
*(Or double-click `index.html` in your file manager).*

### 2. Launching and Stopping Labs on CML (Proxmox)
```bash
# List all labs on your CML server
python3 ~/ccna-study/scripts/cml_client.py list

# Start Lab 09 (Multi-Subnet IPv4 Routing)
python3 ~/ccna-study/scripts/cml_client.py start 86e5272c-f7a7-40b3-84ab-47ff9f969786

# Stop Lab 09
python3 ~/ccna-study/scripts/cml_client.py stop 86e5272c-f7a7-40b3-84ab-47ff9f969786
```

### 3. Studying with Antigravity (`agy`) in Terminal
```bash
cd ~/ccna-study
agy
```

---

## 📁 Workspace Layout
* `index.html` — Master Visual Dashboard, Study Workflow, and Subnetting Math Trainer.
* `labs/` — Standalone, interactive HTML lab workbooks with collapsible spoiler-free solutions.
* `notes/` — Chapter summaries, subnet cheat sheets, and lessons learned.
* `scripts/` — CML REST API automation tools (`cml_client.py`).
