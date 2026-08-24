# Tyler's CCNA Study & Lab Hub (Pure HTML Architecture)

## Student Profile & Roadmap
- **Target Exam**: Cisco CCNA (200-301 v1.1)
- **Primary Literature**: Wendell Odom's Cisco Press Official Cert Guides (Volume 1 & Volume 2)
- **Active Focus**: **Volume 1, Chapter 9: Subnet Design & IPv4 Routing Configuration**
- **Lab Infrastructure**: Cisco Modeling Labs (CML 2.10) on Proxmox VE (`cml-controller.internal`)
- **Dashboard**: `~/ccna-study/index.html` (Master Interactive Dashboard)
- **Lab Format**: `~/ccna-study/labs/*.html` (100% Rich Standalone Interactive HTML Workbooks)

---

## Agent Operational Rules (Zero Fluff)
1. **NO Markdown Fluff**: Do NOT generate separate text `.md` summary files or duplicate textbook content.
2. **HTML-Only Lab Workbooks**: Whenever creating new chapter lab guides (e.g. Lab 10, Lab 11), generate them directly as single-file, responsive, self-contained `.html` workbooks in `labs/` with:
   - Spoiler-free collapsible `<details>` drawers for solutions and hints.
   - Interactive task checklists (`updateProgress()`).
   - 1-click "Copy Config" buttons for Cisco IOS syntax.
   - Embedded SVG network topology maps.
   - Print-to-PDF styles (`@media print`).
3. **CML Automation**: Manage CML topologies programmatically using `scripts/cml_client.py`.
4. **Diagnostic & Quizzing**: Quiz the student interactively in terminal chat with Socratic questions, CLI output analysis, and packet flow tracing.
