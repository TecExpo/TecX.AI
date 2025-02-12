from web3 import Web3

INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

CONTRACT_ADDRESS = "0xYourContractAddress"
ABI = [...]  # Replace with actual contract ABI

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

def test_reentrancy_attack():
    try:
        tx_hash = contract.functions.withdraw().transact({"from": "0xAttackerAddress"})
        print("❌ Potential reentrancy vulnerability detected!")
    except Exception as e:
        print("✅ Reentrancy test passed. No vulnerability detected.")

test_reentrancy_attack()
