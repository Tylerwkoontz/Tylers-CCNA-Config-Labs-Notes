#!/usr/bin/env python3
"""
CML API Client & Automation Utility for CCNA Lab Orchestration.
"""
import urllib.request
import json
import ssl
import sys
import os

CML_URL = os.getenv("CML_URL", "https://cml-controller.internal")
CML_USER = os.getenv("CML_USERNAME", "admin")
CML_PASS = os.getenv("CML_PASSWORD", "Ruger10/22!")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_token():
    auth_url = f"{CML_URL}/api/v0/authenticate"
    payload = {"username": CML_USER, "password": CML_PASS}
    req = urllib.request.Request(
        auth_url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, context=ctx) as res:
        return json.loads(res.read().decode())

def api_request(endpoint, method="GET", data=None, content_type="application/json"):
    token = get_token()
    url = f"{CML_URL}/api/v0/{endpoint.lstrip('/')}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": content_type}
    if data is not None:
        body = data.encode() if isinstance(data, str) else json.dumps(data).encode()
    else:
        body = None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, context=ctx) as res:
        content = res.read().decode()
        return json.loads(content) if content else None

def list_labs():
    labs = api_request("labs")
    print(f"\n📡 Labs on CML Controller ({CML_URL}):")
    print(f"{'ID':<38} {'STATE':<18} {'NODES':<6} {'TITLE'}")
    print("-" * 85)
    for lab_id in labs:
        details = api_request(f"labs/{lab_id}")
        title = details.get("lab_title", "Untitled")
        state = details.get("state", "UNKNOWN")
        node_count = details.get("node_count", 0)
        print(f"{lab_id:<38} {state:<18} {node_count:<6} {title}")

def sync_breakout():
    """Trigger background breakout service restart to auto-bind new lab ports."""
    try:
        import subprocess
        subprocess.run(["systemctl", "--user", "restart", "cml-breakout.service"], capture_output=True)
        print("🔄 Breakout console ports automatically synchronized.")
    except Exception:
        pass

def start_lab(lab_id):
    print(f"🚀 Starting lab {lab_id}...")
    api_request(f"labs/{lab_id}/start", method="PUT")
    print("✅ Lab start requested.")
    sync_breakout()

def stop_lab(lab_id):
    print(f"🛑 Stopping lab {lab_id}...")
    api_request(f"labs/{lab_id}/stop", method="PUT")
    print("✅ Lab stop requested.")
    sync_breakout()

def wipe_lab(lab_id):
    print(f"🧹 Wiping lab {lab_id}...")
    api_request(f"labs/{lab_id}/wipe", method="PUT")
    print("✅ Lab wiped.")
    sync_breakout()


def import_lab(yaml_path):
    if not os.path.exists(yaml_path):
        print(f"❌ File not found: {yaml_path}")
        return
    print(f"📦 Importing {yaml_path} to CML...")
    with open(yaml_path, "r") as f:
        yaml_content = f.read()
    res = api_request("import", method="POST", data=yaml_content, content_type="text/plain")
    lab_id = res.get("id") if isinstance(res, dict) else res
    print(f"✅ Lab successfully imported! CML Lab ID: {lab_id}")
    return lab_id

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "list":
        list_labs()
    elif sys.argv[1] == "start" and len(sys.argv) > 2:
        start_lab(sys.argv[2])
    elif sys.argv[1] == "stop" and len(sys.argv) > 2:
        stop_lab(sys.argv[2])
    elif sys.argv[1] == "wipe" and len(sys.argv) > 2:
        wipe_lab(sys.argv[2])
    elif sys.argv[1] == "import" and len(sys.argv) > 2:
        import_lab(sys.argv[2])
    else:
        print("Usage: cml_client.py [list|start <id>|stop <id>|wipe <id>|import <yaml_file>]")
