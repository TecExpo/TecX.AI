from web3 import Web3
import threading

INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

SENDER_WALLET = "0xYourWalletAddress"
RECEIVER_WALLET = "0xReceiverWalletAddress"
NUM_TRANSACTIONS = 50  # Simulating 50 transactions

def send_transaction(tx_id):
    amount = w3.toWei(0.01, "ether")
    tx = {
        "from": SENDER_WALLET,
        "to": RECEIVER_WALLET,
        "value": amount,
        "gas": 21000,
        "gasPrice": w3.toWei("50", "gwei"),
    }
    
    print(f"✅ Transaction {tx_id} prepared")
    # Simulating transaction broadcast (Not actually signing/sending for security reasons)

threads = []
for i in range(NUM_TRANSACTIONS):
    thread = threading.Thread(target=send_transaction, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("✅ Load test for Web3 transactions completed.")
