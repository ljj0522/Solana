from solana.rpc.api import Client
from solders.pubkey import Pubkey

def get_solana_balance(address: str) -> float:
    # 创建Solana客户端，连接到主网或测试网
    client = Client("https://api.mainnet-beta.solana.com")

    pubkey = Pubkey.from_string(address)

    # 获取账户信息
    response = client.get_balance(pubkey)
    if response.value is not None:
        balance_lamports = response.value  # 从响应中获取lamports值
        # 将lamports转换为SOL（1 SOL = 1e9 lamports）
        balance_sol = balance_lamports / 1_000_000_000.0
        return balance_sol
    else:
        raise Exception(f"Error fetching balance: {response}")


if __name__ == "__main__":
    address_to_check = "your SOLANA address"

    try:
        balance = get_solana_balance(address_to_check)
        print(f"The balance of the account {address_to_check} is: {balance} SOL")
    except Exception as e:
        print(e)
