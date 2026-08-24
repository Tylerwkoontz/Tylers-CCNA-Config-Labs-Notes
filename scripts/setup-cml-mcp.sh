#!/usr/bin/env bash
set -e

# Prompt for CML credentials if not set
read -rp "Enter your CML Username [admin]: " CML_USER
CML_USER=${CML_USER:-admin}

read -rsp "Enter your CML Password: " CML_PASS
echo ""

# Ensure uv is in PATH
export PATH="$HOME/.local/bin:$PATH"

echo "Registering CML MCP server with agy..."
agy mcp add \
  --env CML_URL=https://cml-controller.internal \
  --env CML_USERNAME="$CML_USER" \
  --env CML_PASSWORD="$CML_PASS" \
  --env CML_VERIFY_SSL=false \
  cml uvx -- "cml-mcp[pyats]"

echo "CML MCP Server registered successfully! Listing MCP servers:"
agy mcp list
