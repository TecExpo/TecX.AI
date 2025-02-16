bash
echo "To run load tests:"
pytest tests/load-tests/
echo "To run security tests"
pytest tests/security-tests/

chmod +x scripts/deploy.sh
./scripts/deploy.sh
chmod +x scripts/backup/*.sh
./scripts/backup/db_backup.sh
./scripts/backup/log_backup.sh
./scripts/backup/ipfs_backup.sh

