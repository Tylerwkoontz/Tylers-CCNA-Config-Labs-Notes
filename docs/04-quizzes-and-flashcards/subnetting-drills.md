# Subnetting Speed Drills

Use these practice drills to build instant mental math for IPv4 subnetting.

---

## ⚡ Drill 1: Subnet ID & Broadcast Calculation

| Given IP Address & Mask | Subnet ID | First Usable Host | Last Usable Host | Broadcast Address |
| :--- | :--- | :--- | :--- | :--- |
| `10.50.20.100 /20` | `10.50.16.0` | `10.50.16.1` | `10.50.31.254` | `10.50.31.255` |
| `172.16.88.200 /22` | `172.16.88.0` | `172.16.88.1` | `172.16.91.254` | `172.16.91.255` |
| `192.168.1.142 /27` | `192.168.1.128` | `192.168.1.129` | `192.168.1.158` | `192.168.1.159` |
| `10.100.5.50 /29` | `10.100.5.48` | `10.100.5.49` | `10.100.5.54` | `10.100.5.55` |

---

## 🧠 Magic Number Quick Reference

| Prefix | Mask Octet | Magic Number (Increment) | Number of Hosts ($2^h - 2$) |
| :--- | :--- | :--- | :--- |
| `/25` or `/17` or `/9` | `.128` | **128** | 126 |
| `/26` or `/18` or `/10` | `.192` | **64** | 62 |
| `/27` or `/19` or `/11` | `.224` | **32** | 30 |
| `/28` or `/20` or `/12` | `.240` | **16** | 14 |
| `/29` or `/21` or `/13` | `.248` | **8** | 6 |
| `/30` or `/22` or `/14` | `.252` | **4** | 2 |
| `/31` (RFC 3021 P2P) | `.254` | **2** | 2 (no broadcast/subnet ID reserved) |
| `/32` (Host Route) | `.255` | **1** | 1 |
