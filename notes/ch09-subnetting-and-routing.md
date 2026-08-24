# Chapter 09: Subnet Design & IPv4 Routing Configuration

## 📖 Chapter Summary
Chapter 9 of Wendell Odom's Official Cert Guide covers the principles of designing IPv4 subnetting schemes, choosing the right subnet mask based on host and subnet requirements, and applying IP addressing configurations to Cisco router interfaces.

---

## 🔑 Key Concepts & Definitions

### 1. Subnet Sizing Formulas
* **Number of Subnets created from borrowed bits ($s$):**
  $$\text{Subnets} = 2^s$$
* **Number of Usable Hosts per Subnet ($h$ remaining host bits):**
  $$\text{Usable Hosts} = 2^h - 2$$
  *(Minus 2 accounts for the reserved Subnet ID and Broadcast Address)*.

### 2. Magic Number Method
* **Magic Number** = $256 - \text{Interesting Octet Subnet Mask Value}$.
* The Magic Number is the exact step/increment between consecutive Subnet IDs in that octet.
* **Example:** Subnet mask `255.255.255.224` (/27)
  * Interesting Octet = 4th octet (`224`)
  * Magic Number = $256 - 224 = 32$
  * Subnets: `.0`, `.32`, `.64`, `.96`, `.128`, `.160`, `.192`, `.224`.

---

## 🛠️ Cisco IOS Configuration Reference

### Interface IP Configuration
```cisco
Router(config)# interface GigabitEthernet0/0/0
Router(config-if)# ip address 192.168.10.1 255.255.255.0
Router(config-if)# description LAN connection to Switch1
Router(config-if)# no shutdown
```

### Static Route Configuration
```cisco
! ip route <destination-network> <subnet-mask> <next-hop-ip | exit-interface>
Router(config)# ip route 10.1.2.0 255.255.255.0 10.1.12.2

! Default Static Route (Gateway of Last Resort)
Router(config)# ip route 0.0.0.0 0.0.0.0 198.51.100.1
```

---

## 🔍 Essential Verification Commands
| Command | Purpose |
| :--- | :--- |
| `show ip interface brief` | View summary status (`Status: up`, `Protocol: up/down`) and assigned IPs. |
| `show ip route` | Inspect the IPv4 routing table. Look for codes: `C` (Connected), `L` (Local host /32), `S` (Static). |
| `show interfaces <name>` | Check speed, duplex, MTU, packet counters, collisions, and errors. |
| `ping <destination-ip>` | Verify Layer 3 end-to-end IP reachability. |

---

## ⚠️ Common Traps & Gotchas
1. **Local (`L`) routes in IOS 15+**: Cisco routers automatically create `/32` host routes for every configured and active interface IP. Do not confuse `C` (the subnet) with `L` (the exact interface IP).
2. **Interface state down/down**: If an interface is `administratively down`, run `no shutdown`. If `up/down`, check physical cabling, speed/duplex mismatch, or keepalive issues.
