# Cisco Modeling Labs (CML) Lab Catalog

Welcome to the interactive lab repository. All published lab workbooks here are tested and built directly on your Proxmox-hosted CML instance (`cml-controller.internal`).

---

## 🚀 Published Interactive Lab Workbooks

| Lab ID & Title | Domain & Chapter | Difficulty | Est. Time | CML Lab Status |
| :--- | :--- | :--- | :--- | :--- |
| [**Lab 09: Multi-Subnet IPv4 Routing**](published/lab09-multi-subnet-routing.md) | 1.6 Addressing & 3.1 Routing | <span class="badge badge-med">Intermediate</span> | 35 Mins | <span class="badge badge-cml">Provisioned</span> |
| [**Master Lab Template**](published/template-lab-guide.md) | Standard Reference | <span class="badge badge-easy">Guide</span> | - | Reference Blueprint |

---

## 🛠️ How to Work Through a Lab Guide

1. **Review Scenario & Addressing**: Read the business requirements and fill in your subnet worksheet.
2. **Launch on CML**: Spin up the lab topology using `~/ccna-study/scripts/cml_client.py start <lab_id>`.
3. **Execute Without Spoilers**: Work through each task checklist. If you get stuck, expand the **Hint** drawers first before looking at the **Solution** drawers.
4. **Automated Verification**: Follow the verification commands to confirm routing and connectivity.
5. **Print to PDF**: Use `Ctrl+P` in your browser for a clean, pagination-ready printed lab worksheet.
