bash

chmod +x ai-engine/train.sh
./ai-engine/train.sh
chmod +x ai-engine/infer.sh
./ai-engine/infer.sh
chmod +x ai-engine/preprocess.sh
./ai-engine/preprocess.sh
chmod +x ai-engine/Model_Exploration.sh
./ai-engine/Model_Exploration.sh
chmod +x ai-engine/install_packages.sh
./ai-engine/install_packages.sh
echo "To run all unit tests:"
pytest tests/unit-tests/
echo "To run integration tests:"
pytest tests/integration-tests/
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

