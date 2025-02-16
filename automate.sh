
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
pytest integration-tests/
echo "To run load tests:"
pytest load-tests/
echo "To run security tests"
pytest security-tests/
cd ../
cd ./scripts
chmod +x deploy.sh
./deploy.sh
chmod +x backup/*.sh
./backup/db_backup.sh
./backup/log_backup.sh
./backup/ipfs_backup.sh
cd ../
