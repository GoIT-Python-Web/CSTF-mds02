import argparse
from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = f"mongodb://localhost:27017"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.mds02

parser = argparse.ArgumentParser(description="Add a new cat")
parser.add_argument("--action", help="[create, read, update, delete]")
parser.add_argument("--id", help="ID of the cat")
parser.add_argument("--name", help="Name of the cat")
parser.add_argument("--age", help="Age of the cat")
parser.add_argument("--features", help="Features of the cat", nargs="+")

args = vars(parser.parse_args())
action = args["action"]
pk = args["id"]
name = args["name"]
age = args["age"]
features = args["features"]


def read():
    cats = db.cats.find()
    return cats


def create(name, age, features):
    return db.cats.insert_one({
        "name": name,
        "age": age,
        "features": features
    })


def update(pk, name, age, features):
    return db.cats.update_one({"_id": ObjectId(pk)}, {"$set": {"name": name, "age": age, "features": features}})


def delete(pk):
    return db.cats.delete_one({"_id": ObjectId(pk)})


if __name__ == "__main__":
    match action:
        case "create":
            r = create(name, age, features)
            print(r.inserted_id)
        case "read":
            [print(cat) for cat in read()]
        case "update":
            r = update(pk, name, age, features)
            print(r.modified_count)
        case "delete":
            r = delete(pk)
            print(r.deleted_count)
        case _:
            print("Wrong action")
