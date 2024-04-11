from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = f"mongodb://localhost:27017"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.mds02

try:
    # print(db.list_collection_names())
    db.cats.insert_many([
        {
            "name": 'Lama',
            "age": 2,
            "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
        },
        {
            "name": 'Liza',
            "age": 4,
            "features": ['ходить в лоток', 'дає себе гладити', 'білий'],
        },
    ])

except Exception as e:
    print(e)
