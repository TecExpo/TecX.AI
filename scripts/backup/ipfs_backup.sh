#!/bin/bash

# Exit on error
set -e

IPFS_DIR="$HOME/.ipfs"
BACKUP_DIR="backup/ipfs"

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Generate timestamp
TIMESTAMP=$(date +"%F-%H-%M-%S")

# Backup IPFS data
echo "🌐 Backing up IPFS data..."
tar -czvf $BACKUP_DIR/ipfs_backup_$TIMESTAMP.tar.gz $IPFS_DIR

echo "✅ IPFS backup completed: $BACKUP_DIR/ipfs_backup_$TIMESTAMP.tar.gz"
