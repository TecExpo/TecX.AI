from web3 import Web3
import pytest
from backend.web3.provider import get_web3_instance

w3 = get_web3_instance()

def test_web3_contract_interaction():
    contract_address = "0xYourContractAddress"
    abi = [...]  # Replace with actual contract ABI
    contract = w3.eth.contract(address=contract_address, abi=abi)

    owner = contract.functions.owner().call()
    assert Web3.isAddress(owner)  # Check if owner is a valid Ethereum address
