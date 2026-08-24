# Lab Template: [Lab Title Here]

<span class="badge badge-ccna">CCNA 200-301</span>
<span class="badge badge-time">Est. Time: 45 Mins</span>
<span class="badge badge-med">Difficulty: Intermediate</span>
<span class="badge badge-cml">CML Ready</span>

<div class="lab-header-card">
  <strong>Lab Overview & Objectives:</strong>
  <div class="lab-header-grid">
    <div><strong>Primary Topic:</strong> [e.g., OSPFv2 Single-Area]</div>
    <div><strong>Odom Reading:</strong> [Volume 1, Chapter X]</div>
    <div><strong>Nodes:</strong> 2x IOSv, 2x Switch, 2x PC</div>
    <div><strong>CML Lab ID:</strong> <code>[UUID Here]</code></div>
  </div>
</div>

---

## 🗺️ Topology Diagram

```mermaid
flowchart LR
    PC1["PC 1"] --- SW1["Switch 1"]
    SW1 --- R1["Router 1"]
    R1 <-->|WAN Link| R2["Router 2"]
    R2 --- SW2["Switch 2"]
    SW2 --- PC2["PC 2"]
```

---

## 📋 Addressing & Subnetting Table

| Device | Interface | IPv4 Address | Subnet Mask | Default Gateway | Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **R1** | `Gi0/0` | `10.0.12.1` | `255.255.255.252` | N/A | WAN to R2 |
| **R1** | `Gi0/1` | `192.168.10.1` | `255.255.255.0` | N/A | LAN Gateway |
| **R2** | `Gi0/0` | `10.0.12.2` | `255.255.255.252` | N/A | WAN to R1 |
| **R2** | `Gi0/1` | `192.168.20.1` | `255.255.255.0` | N/A | LAN Gateway |

---

## 📝 Tasks & Step-by-Step Instructions

### Task 1: [Task Description]
- [ ] Configure hostname and interface IP on Router 1.
- [ ] Add interface description and issue `no shutdown`.

??? tip "💡 Hint: Interface Configuration Syntax"
    Remember to navigate to interface configuration mode before assigning the IP address:
    ```cisco
    Router(config)# interface GigabitEthernet0/0
    Router(config-if)# ip address <ip> <mask>
    Router(config-if)# no shutdown
    ```

??? success "🔍 Solution: Router 1 Configuration"
    ```cisco
    enable
    configure terminal
    hostname R1
    !
    interface GigabitEthernet0/0
     description WAN link to R2
     ip address 10.0.12.1 255.255.255.252
     no shutdown
    !
    interface GigabitEthernet0/1
     description LAN A Gateway
     ip address 192.168.10.1 255.255.255.0
     no shutdown
    !
    end
    write memory
    ```

---

## 🔍 Verification & Testing

=== "1. Interface Status"
    Verify that all interfaces are in the `up/up` state:
    ```cisco
    R1# show ip interface brief
    ```

=== "2. Routing Table"
    Verify that connected and local routes appear:
    ```cisco
    R1# show ip route
    ```

=== "3. End-to-End Ping"
    Test reachability between endpoints:
    ```cisco
    PC1# ping 192.168.20.10
    ```

---

## ⚡ Break-Fix Challenge (Troubleshooting)

??? warning "⚠️ Inject Fault: Break-Fix Challenge"
    **Symptom**: PC1 cannot ping PC2. 
    **Challenge**: Use verification commands to identify the fault without looking at the running configuration directly.

??? success "🛠️ Solution & Fault Explanation"
    **Root Cause**: [Explain the fault, e.g., subnet mask mismatch or shutdown interface].
    **Resolution**: [Provide the command to fix the issue].
