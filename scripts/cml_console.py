#!/usr/bin/env python3
"""
Interactive CML Console Selector and Connector.
Reads breakout-tool/labs.yaml and lets you connect to any active node with 1 click/keystroke.
"""
import os
import sys
import subprocess
import yaml

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABS_YAML = os.path.join(WORKSPACE, "breakout-tool", "labs.yaml")

def load_labs():
    if not os.path.exists(LABS_YAML):
        print(f"❌ '{LABS_YAML}' not found. Run 'systemctl --user restart cml-breakout' first.")
        sys.exit(1)
    
    with open(LABS_YAML, "r") as f:
        data = yaml.safe_load(f) or {}

    labs = {}
    for lab_id, lab in data.items():
        lab_title = lab.get("lab_title", "Untitled Lab")
        nodes = []
        for node_id, node in lab.get("nodes", {}).items():
            label = node.get("label", "Unknown")
            for dev in node.get("devices", []):
                if dev.get("name") == "serial0" and dev.get("enabled"):
                    nodes.append({
                        "label": label,
                        "port": dev.get("listen_port"),
                        "lab_id": lab_id,
                        "lab_title": lab_title
                    })
        if nodes:
            labs[lab_id] = {
                "title": lab_title,
                "nodes": sorted(nodes, key=lambda x: x["label"])
            }
    return labs

def get_short_title(title):
    """Extract short title e.g. 'Lab 09B' from 'CCNA Lab 09B: STP Parallel Links'"""
    if "Lab " in title:
        parts = title.split(":")[0].replace("CCNA ", "").strip()
        return parts
    return title[:12]

def open_split_grid(nodes, lab_title=None):
    """Launches all nodes for the lab in a tiled side-by-side grid inside a new terminal window."""
    import shutil
    import re

    short_lab = get_short_title(lab_title) if lab_title else "All Labs"
    slug = re.sub(r'[^a-zA-Z0-9_-]', '_', short_lab).lower()
    session = f"cml_{slug}"

    print(f"\n🚀 Launching Split Grid ({len(nodes)} devices) in a new window for '{short_lab}'...")

    # Kill old session if exists
    subprocess.run(["tmux", "kill-session", "-t", session], capture_output=True)

    # 1. Start session with first node
    first = nodes[0]
    cmd0 = f"telnet 127.0.0.1 {first['port']}"
    subprocess.run(["tmux", "new-session", "-d", "-s", session, "-n", short_lab, cmd0])
    subprocess.run(["tmux", "select-pane", "-t", f"{session}:0.0", "-T", f"[{short_lab}] {first['label']} ({first['port']})"])

    # 2. Split for remaining nodes
    for idx, node in enumerate(nodes[1:], 1):
        cmd = f"telnet 127.0.0.1 {node['port']}"
        subprocess.run(["tmux", "split-window", "-t", session, cmd])
        subprocess.run(["tmux", "select-pane", "-t", f"{session}:0.{idx}", "-T", f"[{short_lab}] {node['label']} ({node['port']})"])

    # 3. Tiled layout (2x2, 1x2, etc.)
    subprocess.run(["tmux", "select-layout", "-t", session, "tiled"])

    # 4. Enable mouse mode and colored pane titles
    subprocess.run(["tmux", "set-option", "-t", session, "mouse", "on"])
    subprocess.run(["tmux", "set-option", "-t", session, "pane-border-status", "top"])
    subprocess.run(["tmux", "set-option", "-t", session, "pane-border-format", " #[bold,fg=colour39] #{pane_title} #[default]"])

    # 5. Launch in a dedicated new Ptyxis window
    if shutil.which("ptyxis"):
        subprocess.Popen(["ptyxis", "--new-window", "-T", f"CML Grid: {short_lab}", "--", "tmux", "attach-session", "-t", session])
    elif shutil.which("gnome-terminal"):
        subprocess.Popen(["gnome-terminal", "--title", f"CML Grid: {short_lab}", "--", "tmux", "attach-session", "-t", session])
    else:
        subprocess.Popen(["x-terminal-emulator", "-T", f"CML Grid: {short_lab}", "-e", f"tmux attach-session -t {session}"])

    print(f"✅ Split Grid opened in a new window!")
    print("   💡 Tip: Click any box to type. Drag borders to resize. Press 'Ctrl+B' then 'Z' to zoom a switch full-screen.")

def connect(node):
    short_lab = get_short_title(node.get("lab_title", ""))
    print(f"\n🔌 Connecting to [{short_lab}] {node['label']} on 127.0.0.1:{node['port']}...")
    print("📌 TO DISCONNECT: Press 'Ctrl + ]', type 'quit', and press Enter.\n")
    try:
        subprocess.run(["telnet", "127.0.0.1", str(node["port"])])
    except KeyboardInterrupt:
        pass

def main():
    labs = load_labs()
    if not labs:
        print("⚠️ No active labs/nodes found in labs.yaml.")
        print("Ensure your CML lab is started and run 'systemctl --user restart cml-breakout'.")
        sys.exit(1)

    lab_list = list(labs.values())
    all_nodes = [n for l in lab_list for n in l["nodes"]]

    # Command line argument handling
    if len(sys.argv) > 1:
        arg = sys.argv[1].strip().lower()

        # Handle 'all'
        if arg in ("all", "-a", "--all", "grid"):
            if len(lab_list) == 1:
                open_split_grid(lab_list[0]["nodes"], lab_list[0]["title"])
            else:
                open_split_grid(all_nodes, "All Active Labs")
            return

        # Direct Lab match (e.g. 'cml-con 09b' or 'cml-con 9' or 'cml-con ssh')
        matched_lab = next((l for l in lab_list if arg in l["title"].lower()), None)
        if matched_lab:
            open_split_grid(matched_lab["nodes"], matched_lab["title"])
            return

        # Direct Node match (e.g. 'cml-con sw1')
        matched_node = next((n for n in all_nodes if n["label"].lower() == arg), None)
        if matched_node:
            connect(matched_node)
            return

    # Interactive Menu
    print("\n🔬 Active Labs on CML:")
    print("=" * 65)
    for idx, lab in enumerate(lab_list, 1):
        node_summary = ", ".join([f"{n['label']}:{n['port']}" for n in lab["nodes"]])
        print(f"  [{idx}] {lab['title']}")
        print(f"      ↳ Nodes ({len(lab['nodes'])}): {node_summary}\n")
    
    if len(lab_list) > 1:
        print(f"  [A] Open ALL {len(all_nodes)} nodes across all labs in a Split Grid")
    print("=" * 65)
    print("  💡 Tip: To disconnect from any console, press 'Ctrl + ]', then 'quit'\n")

    try:
        prompt = f"👉 Select Lab [1-{len(lab_list)}] for Split Grid, device name (e.g. SW1), or 'q' to cancel: "
        choice = input(prompt).strip()
        if not choice or choice.lower() in ('q', 'quit', 'exit'):
            return

        if choice.lower() in ('a', 'all'):
            open_split_grid(all_nodes, "All Active Labs")
            return

        if choice.isdigit() and 1 <= int(choice) <= len(lab_list):
            selected_lab = lab_list[int(choice) - 1]
            open_split_grid(selected_lab["nodes"], selected_lab["title"])
            return

        # Check if they typed a node label directly
        matched_node = next((n for n in all_nodes if n["label"].lower() == choice.lower()), None)
        if matched_node:
            connect(matched_node)
            return

        # Check if they typed a lab search query
        matched_lab = next((l for l in lab_list if choice.lower() in l["title"].lower()), None)
        if matched_lab:
            open_split_grid(matched_lab["nodes"], matched_lab["title"])
            return

        print(f"❌ Invalid selection: '{choice}'")
    except (KeyboardInterrupt, EOFError):
        print("\nSession canceled.")

if __name__ == "__main__":
    main()



