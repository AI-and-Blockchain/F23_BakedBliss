from web3 import Web3

ethereum_node_url = "bakedbliss.net"

w3 = Web3(Web3.HTTPProvider(ethereum_node_url))

if w3.is_connected():
    print("Connected to Ethereum node")
    print("Ethereum node version:", w3.clientVersion)
    print("Ethereum chain ID:", w3.eth.chainId)

    # Example: Check your balance
    your_address = "0xEthereumAddress"
    balance_wei = w3.eth.getBalance(your_address)
    balance_eth = w3.fromWei(balance_wei, "ether")
    print(f"Balance for {your_address}: {balance_eth} ETH")
else:
    print("Failed to connect to Ethereum node")