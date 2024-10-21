import time

from solders.pubkey import Pubkey
from solana.rpc.api import Client
from solana.transaction import Transaction, AccountMeta, Instruction
from struct import pack
client = Client("https://api.mainnet-beta.solana.com")
# 替换为实际值
contract_address = Pubkey.from_string("pvwX4B67eRRjBGQ4jJUtiUJEFQbR4bvG6Wbe6mkCjtt")
token_program_id = Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA")
mint_address = Pubkey.from_string("")  # 替换为你的 mint 地址
destination_account = Pubkey.from_string("")  # 接收者地址

# print(client.get_balance(destination_account))
# 要铸造的数量（以最小单位表示）
transaction = Transaction()

instruction0 = Instruction(
    program_id=Pubkey.from_string("ComputeBudget111111111111111111111111111111"),
    data=bytes.fromhex('03250a2a0000000000'),
    accounts=[],
)
transaction.add(instruction0)

instruction1 = Instruction(
    program_id=Pubkey.from_string("ComputeBudget111111111111111111111111111111"),
    data=bytes.fromhex('02400d0300'),
    accounts=[],
)
transaction.add(instruction1)
# 创建自定义 Instruction 对象
instruction = Instruction(
    program_id=contract_address,
    data=bytes.fromhex('3b8418f67a2708f3'),
    accounts=[
        AccountMeta(pubkey=Pubkey.from_string("4ALKS249vAS3WSCUxXtHJVZN753kZV6ucEQC41421Rka"), is_signer=False,
                    is_writable=True),
        AccountMeta(pubkey=Pubkey.from_string("EEQGqAnxRoF7jixtxsLJk8o52JhBoDGtjmWAwvt6EJQE"), is_signer=False,
                    is_writable=True),
        AccountMeta(pubkey=Pubkey.from_string("DH7oGhZLxhmZkA1spAJEBB52MxTs4UTGuXYNYWoAUNCN"), is_signer=False,
                    is_writable=True),
        AccountMeta(pubkey=Pubkey.from_string("AmTonSS41ya3i7Cd5hgYiNJXhvrc6wP1EKngrJZ72Vvr"), is_signer=False,
                    is_writable=True),
        AccountMeta(pubkey=destination_account, is_signer=False, is_writable=True),
        AccountMeta(pubkey=Pubkey.from_string("2eAgG1UDRZrAE24rBRhTeSrk3wWYKHJSeXFHj9Skj8gV"), is_signer=False,
                    is_writable=False),
        AccountMeta(pubkey=Pubkey.from_string("Sysvar1nstructions1111111111111111111111111"), is_signer=False,
                    is_writable=False),
        AccountMeta(pubkey=Pubkey.from_string("ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"), is_signer=False,
                    is_writable=False),
        AccountMeta(pubkey=token_program_id, is_signer=False, is_writable=False),
        AccountMeta(pubkey=Pubkey.from_string("11111111111111111111111111111111"), is_signer=False,
                    is_writable=False),
        AccountMeta(pubkey=Pubkey.from_string("SysvarRent111111111111111111111111111111111"), is_signer=False,
                    is_writable=False),
    ],
)
transaction.add(instruction)
transaction.fee_payer = destination_account

for i in range(100):

    # 然后继续签名并发送交易...
    recent_blockhash_response = client.get_latest_blockhash()
    if recent_blockhash_response.value:
        transaction.recent_blockhash = recent_blockhash_response.value.blockhash
    else:
        print(f"Error fetching block hash: {recent_blockhash_response}")


    # print("Recent Blockhash:", transaction.recent_blockhash)
    # print("Fee Payer:", transaction.fee_payer)
    # print("Instructions:")
    # for instruction in transaction.instructions:
    #     print(f"  Program ID: {instruction.program_id}")
    #     print(f"  Accounts: {[str(account) for account in instruction.accounts]}")
    #     print(f"  Data: {instruction.data.hex()}")

    try:
        from solders.keypair import Keypair

        keypair = Keypair.from_base58_string("")  # 请将其替换成实际私钥

        # 签名事务，这一步很重要。
        transaction.sign(keypair)

        # 序列化已签名的交易，以便发送。
        serialized_txn = transaction.serialize()

        response_send_txn: str = client.send_transaction(serialized_txn)  # 注意这里只传递已序列化且已签名的 transaction

        print(f"Transaction Response: {response_send_txn}")
    except Exception as e:
        print(f"Error sending transaction: {str(e)}")

    time.sleep(60)
    # print(client.get_balance(destination_account))
