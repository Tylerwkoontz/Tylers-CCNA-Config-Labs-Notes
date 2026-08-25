#!/usr/bin/env bash
#
# Cisco CML Breakout Tool Helper Script
#

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd "$DIR" || exit 1

export BREAKOUT_PASSWORD="${BREAKOUT_PASSWORD:-Ruger10/22!}"
export BREAKOUT_USERNAME="${BREAKOUT_USERNAME:-admin}"
export BREAKOUT_CONTROLLER="${BREAKOUT_CONTROLLER:-https://cml-controller.internal}"

case "$1" in
  ui)
    echo "🌐 Launching CML Breakout Tool Web UI..."
    echo "👉 Open your browser to: http://127.0.0.1:8080"
    ./breakout-linux-amd64 ui
    ;;
  init)
    echo "🔄 Fetching active CML labs and generating port assignments..."
    ./breakout-linux-amd64 init --enable-all
    ;;
  run|"")
    echo "🔄 Refreshing lab topology..."
    ./breakout-linux-amd64 init --enable-all > /dev/null 2>&1
    echo "🚀 Starting CML Breakout console proxy..."
    ./breakout-linux-amd64 run
    ;;
  *)
    echo "Usage: ./start-breakout.sh [run|ui|init]"
    echo ""
    echo "  run   (default) Refresh running labs and start local serial console listeners"
    echo "  ui              Launch the local Web UI on http://127.0.0.1:8080"
    echo "  init            Refresh labs.yaml configuration without starting listeners"
    exit 1
    ;;
esac
