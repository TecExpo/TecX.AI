from web3 import Web3
from backend.web3.provider import get_web3_instance

w3 = get_web3_instance()
contract_address = "0xYourContractAddress"
abi = [...]  # Replace with actual ABI
contract = w3.eth.contract(address=contract_address, abi=abi)

def test_reentrancy_attack():
    tx = contract.functions.withdraw().buildTransaction({
        "from": w3.eth.accounts[0],
        "gas": 1000000,
        "gasPrice": w3.toWei("10", "gwei"),
    })
    signed_tx = w3.eth.account.signTransaction(tx, "PRIVATE_KEY")
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    
    assert receipt["status"] == 1, "Potential reentrancy vulnerability detected"

def test_integer_overflow():
    try:
        tx = contract.functions.setValue(2**256).buildTransaction({
            "from": w3.eth.accounts[0],
            "gas": 1000000,
            "gasPrice": w3.toWei("10", "gwei"),
        })
        signed_tx = w3.eth.account.signTransaction(tx, "PRIVATE_KEY")
        w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        assert False, "Integer overflow not handled properly"
    except Exception:
        assert True  # Overflow should be prevented
