#!/bin/bash

# Exit on error
set -e

# Database credentials
DB_USER="root"
DB_PASS="your_password"
DB_NAME="ai_web3_db"
BACKUP_DIR="backup/db"

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Generate timestamp
TIMESTAMP=$(date +"%F-%H-%M-%S")

# Perform MySQL dump
echo "💾 Backing up MySQL database..."
mysqldump -u $DB_USER -p$DB_PASS $DB_NAME > $BACKUP_DIR/db_backup_$TIMESTAMP.sql

echo "✅ Database backup completed: $BACKUP_DIR/db_backup_$TIMESTAMP.sql"
