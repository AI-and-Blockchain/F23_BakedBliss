import ipfshttpclient

# Connect to an IPFS node (replace 'localhost' and '5001' with your IPFS node's address)
client = ipfshttpclient.connect('/ip4/localhost/tcp/5001/http')

# Define the CID of the content you want to retrieve
cid = "QmYourCIDHere"

# Retrieve the content associated with the CID
try:
    content = client.cat(cid)
    print(f"Content for CID {cid}:")
    print(content.decode('utf-8'))  # Assuming it's text content
except ipfshttpclient.exceptions.StatusError as e:
    print(f"Error: {e}")
finally:
    client.close()