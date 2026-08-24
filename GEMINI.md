# Tyler's CCNA Study & Lab Hub (Local-First Architecture)

## Student Profile & Roadmap
- **Target Exam**: Cisco CCNA (200-301 v1.1)
- **Primary Literature**: Wendell Odom's Cisco Press Official Cert Guides (Volume 1 & Volume 2)
- **Active Focus**: **Volume 1, Chapter 9: Subnet Design & IPv4 Routing Configuration**
- **Lab Infrastructure**: Cisco Modeling Labs (CML 2.10) on Proxmox VE (`cml-controller.internal`)
- **Dashboard**: `~/ccna-study/index.html` (Local-First, standalone HTML)
- **Lab Workbooks**: `~/ccna-study/labs/*.html` (Interactive, collapsible solutions, SVG topologies)

---

## Daily Study Protocol
1. **Diagnostic Warmup**: Run a 4-question pre-chapter DIKTA quiz when requested.
2. **Concept Explanations**: Explain networking with first principles, packet walks, and binary breakdown.
3. **CML Lab Automation**: Generate CML topologies via `cml_client.py` or MCP tools.
4. **Interactive HTML Lab Generation**: Output new lab guides as standalone, interactive HTML workbooks in `labs/` with spoiler-free `<details>` accordions and progress trackers.
5. **Knowledge Log**: Capture gotchas, CLI quirks, and insights in `notes/lessons-learned.md`.
