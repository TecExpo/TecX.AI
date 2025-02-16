
echo this is bash shell
echo "installing package for ai-engine directory"
cd ./ai-engine
chmod +x install_packages.sh
./install_packages.sh
chmod +x train.sh
./train.sh
chmod +x infer.sh
./infer.sh
chmod +x preprocess.sh
./preprocess.sh
chmod +x Model_Exploration.sh
./Model_Exploration.sh
cd ../
cd ./tests
echo "To run all unit tests:"
pytest unit-tests/
echo "To run integration tests:"
pytest tests/integration-tests/
echo "To run load tests:"
pytest tests/load-tests/
echo "To run security tests"
pytest tests/security-tests/
cd ../
chmod +x scripts/deploy.sh
./scripts/deploy.sh
chmod +x scripts/backup/*.sh
./scripts/backup/db_backup.sh
./scripts/backup/log_backup.sh
./scripts/backup/ipfs_backup.sh

