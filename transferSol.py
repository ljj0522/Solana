from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair

client = Client("https://api.mainnet-beta.solana.com")

sender = Keypair.from_private_key("")
receiver = PublicKey("")
sol_amount = 0.5
instruction = transfer(
        from_public_key=sender.public_key,
        to_public_key=receiver,
        lamports=int(sol_amount*(10**9))
    )

transaction = Transaction(instructions=[instruction], signers=[sender])
result = client.send_transaction(transaction)
print("Transaction response: ", result)
