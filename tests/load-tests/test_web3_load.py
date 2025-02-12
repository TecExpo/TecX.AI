from web3 import Web3
import threading
from backend.web3.provider import get_web3_instance

w3 = get_web3_instance()
contract_address = "0xYourContractAddress"
abi = [...]  # Replace with actual contract ABI
contract = w3.eth.contract(address=contract_address, abi=abi)

def send_transaction():
    tx = contract.functions.setData("Load Test").buildTransaction({
        "from": w3.eth.accounts[0],
        "gas": 1000000,
        "gasPrice": w3.toWei("10", "gwei"),
    })
    signed_tx = w3.eth.account.signTransaction(tx, "PRIVATE_KEY")
    w3.eth.sendRawTransaction(signed_tx.rawTransaction)

def test_web3_load():
    threads = []
    for _ in range(20):  # Simulate 20 blockchain transactions
        thread = threading.Thread(target=send_transaction)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
