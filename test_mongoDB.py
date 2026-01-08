
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

# Encode only username and password
username = quote_plus("arya22310290")
password = quote_plus("Arya@7806")

# Build URI exactly like your original code
uri = f"mongodb+srv://{username}:{password}@cluster0.la9i3ml.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)