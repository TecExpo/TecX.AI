bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
chmod +x scripts/backup/*.sh
./scripts/backup/db_backup.sh
./scripts/backup/log_backup.sh
./scripts/backup/ipfs_backup.sh

