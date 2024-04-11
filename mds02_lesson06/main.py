from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values

config = dotenv_values(".env")

uri = f"mongodb+srv://{config['USER_MDB']}:{config['PASSWORD_MDB']}@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority&appName=Krabaton"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
