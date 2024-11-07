from web3 import Web3
import joblib

# Load the trained model
model = joblib.load("product_authentication_model.pkl")

# Connect to the Ethereum blockchain
# Update this with your local or remote Ethereum node
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Contract address and ABI (use the contract address from your deployment and replace with the actual ABI)
contract_address = "0xYourSmartContractAddress"
contract_abi = [
    # Add your contract ABI here
]

# Load the contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Function to register product on blockchain
def register_product(product_id, product_name, manufacturer, is_genuine):
    # Convert boolean to bytes to store on blockchain
    tx = contract.functions.registerProduct(product_id, product_name, manufacturer, is_genuine).transact()
    print("Product registration transaction hash:", tx.hex())

# Use AI model to predict if the product is genuine
def authenticate_product(features):
    # Predict using AI model
    prediction = model.predict([features])[0]
    is_genuine = bool(prediction == 1)
    return is_genuine

# Example usage
product_id = 123
product_name = "Product XYZ"
manufacturer = "Company ABC"
# Sample features (these should match the model input)
product_features = [0.3, 1.5, 0.7, 0.2]  # Example feature values

# Predict authenticity and register on blockchain
is_genuine = authenticate_product(product_features)
register_product(product_id, product_name, manufacturer, is_genuine)
