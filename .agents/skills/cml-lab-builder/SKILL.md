---
name: cml-lab-builder
description: Guide for creating, provisioning, and verifying Cisco Modeling Labs (CML) topologies on cml-controller.internal using cml-mcp or REST API.
---

# CML Lab Builder & Automation Skill

This skill guides the agent in orchestrating network labs on the user's Proxmox-hosted CML instance (`cml-controller.internal`).

## Lab Design Principles for CCNA
1. **Topology Simplicity**: Keep lab topologies minimal and laser-focused on the chapter topic (typically 2-4 routers/switches and 2 lightweight hosts/Alpine nodes).
2. **Standard Addressing Conventions**:
   - Point-to-point links: `10.0.xy.x/30` or `10.0.xy.y/30` (where `x` and `y` are device numbers).
   - LAN subnets: `192.168.x.0/24` or `10.x.0.0/24`.
   - Loopback management: `10.255.255.x/32` (matches router number `Rx`).
3. **Structured Lab Lifecycle**:
   - Step 1: Generate or load CML topology definition.
   - Step 2: Push base configurations (hostname, interface IP, `no shutdown`, console logging synchronous).
   - Step 3: Present lab objective instructions to the user.
   - Step 4: Verify student completion via pyATS / CLI `show` commands.

## Troubleshooting Drills (Break-Fix)
To create a break-fix drill:
1. Inject a subtle issue into a working topology (e.g. passive interface on OSPF link, incorrect subnet mask, access VLAN mismatch, shut interface, duplex/speed mismatch).
2. Challenge the student: *"Host A cannot reach Host B. Use your verification commands to isolate the fault and fix it."*
