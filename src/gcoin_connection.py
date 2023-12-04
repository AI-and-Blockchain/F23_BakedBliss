from web3 import Web3
import gcoin_data

def reward_user(address):

    ethereum_node_url = "%%%encoded%%%"

    w3 = Web3(Web3.HTTPProvider(ethereum_node_url))

    if w3.is_connected():
        print("Connected to Ethereum node")

        
        contract_address = gcoin_data.gcoin_address
        

        # Create a Contract object
        contract = w3.eth.contract(address=contract_address, abi=gcoin_data.gcoin_abi)

        # Call function on the smart contract
        value = contract.functions.mint(address, 10000000)
        print(f"Current value in the smart contract: {value}")

    else:
        print("Failed to connect to Ethereum node")