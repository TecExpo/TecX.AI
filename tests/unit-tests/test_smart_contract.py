from web3 import Web3
import json

INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
CONTRACT_ADDRESS = "0xYourContractAddress"
ABI_FILE = "abi.json"

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

with open(ABI_FILE) as f:
    contract_abi = json.load(f)

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

def test_contract_name():
    name = contract.functions.name().call()
    assert name == "MyToken"

def test_total_supply():
    total_supply = contract.functions.totalSupply().call()
    assert total_supply > 0

if __name__ == "__main__":
    test_contract_name()
    test_total_supply()
    print("✅ Smart contract tests passed.")
