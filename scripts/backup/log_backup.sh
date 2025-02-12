#!/bin/bash

# Exit on error
set -e

LOG_DIR="/var/log/ai-web3"
BACKUP_DIR="backup/logs"

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Generate timestamp
TIMESTAMP=$(date +"%F-%H-%M-%S")

# Archive logs
echo "📂 Archiving logs..."
tar -czvf $BACKUP_DIR/log_backup_$TIMESTAMP.tar.gz $LOG_DIR

echo "✅ Logs backup completed: $BACKUP_DIR/log_backup_$TIMESTAMP.tar.gz"
