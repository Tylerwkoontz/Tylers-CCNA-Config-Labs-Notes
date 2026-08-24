#!/usr/bin/env bash
set -e

REMOTE_HOST="mkdocs.internal"
REMOTE_PATH="/root/mkdocs"

echo "🔄 Syncing documentation to Proxmox MkDocs container ($REMOTE_HOST)..."
rsync -avz --delete "$HOME/ccna-study/docs/" "root@$REMOTE_HOST:$REMOTE_PATH/docs/"
rsync -avz "$HOME/ccna-study/mkdocs.yml" "root@$REMOTE_HOST:$REMOTE_PATH/mkdocs.yml"

echo "✅ Sync complete! Live docs updated at: http://192.168.1.120:8000 (or http://mkdocs.internal:8000)"
