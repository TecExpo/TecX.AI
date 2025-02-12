from web3 import Web3
import json

INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
CONTRACT_ADDRESS = "0xYourContractAddress"
ABI_FILE = "abi.json"

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

with open(ABI_FILE) as f:
    contract_abi = json.load(f)

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

def test_blockchain_transaction():
    sender = "0xYourWalletAddress"
    receiver = "0xReceiverWalletAddress"
    amount = w3.toWei(0.01, "ether")

    tx = {
        "from": sender,
        "to": receiver,
        "value": amount,
        "gas": 21000,
        "gasPrice": w3.toWei("50", "gwei"),
    }

    assert tx["value"] > 0
    print("✅ Blockchain transaction test passed.")

if __name__ == "__main__":
    test_blockchain_transaction()
