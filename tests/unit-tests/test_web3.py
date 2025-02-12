from web3 import Web3
import pytest
from backend.web3.provider import get_web3_instance

w3 = get_web3_instance()

def test_web3_connection():
    assert w3.isConnected() == True  # Ensure connection to the Ethereum node

def test_smart_contract_interaction():
    contract_address = "0xYourContractAddress"
    abi = [...]  # Replace with actual contract ABI
    contract = w3.eth.contract(address=contract_address, abi=abi)

    owner = contract.functions.owner().call()
    assert owner is not None  # Check if owner is a valid address
