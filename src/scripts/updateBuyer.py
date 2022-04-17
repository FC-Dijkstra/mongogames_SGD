# ? Chargement fichier de configuration
import json
from datetime import datetime
from bson.objectid import ObjectId
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
print("---update buyer---")

buyerID = input("ID Buyer: ")
updated_buyer = db.buyers.find_one({"_id": ObjectId(buyerID)})
buyer = {
        "name": input("name (string): ") or updated_buyer["name"],
        "fstName": input("first name (string): ") or updated_buyer["fstName"],
        "nickname": input("nickname (string): ") or updated_buyer["nickname"],
        "password": input("password (string): ") or updated_buyer["password"],
        "wishlist": []
    }


result = db.buyers.update_one({"_id": ObjectId(buyerID)}, {"$set": buyer})
print("[INFO] Acknowledged: " + str(result.acknowledged))
print("[INFO] modified_count: " + str(result.modified_count))

print("--- Closing connexion ---")
client.close()
exit(0)
