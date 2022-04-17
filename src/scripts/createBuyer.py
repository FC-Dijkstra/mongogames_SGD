# ? Chargement fichier de configuration
import json
from datetime import datetime

import pymongo

configfile = open("../../config.json")
config = json.load(configfile)
configfile.close()
print("--- Loaded config ---")

# ? configuration et connexion mongoDB
# mongodb://user:pwd@host/db?authSource=db
mongostring = f"mongodb+srv://{config['user']}:{config['password']}@{config['host']}/"
print(mongostring)

client = pymongo.MongoClient(mongostring)
db = client.SGD
print("--- Connection OK ---")

buyer = {
        "name": input("name (string): "),
        "fstName": input("first name (string): "),
        "nickname": input("nickname (string): "),
        "password": input("password (string): "),
        "wishlist": []
    }

result = db.buyers.insert_one(buyer)
print("[INFO] Acknowledged: " + str(result.acknowledged))
print("[INFO] _id: " + str(result.inserted_id))

print("--- Closing connexion ---")
client.close()
exit(0)
