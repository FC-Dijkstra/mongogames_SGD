# ? Chargement fichier de configuration
import json
from datetime import datetime

import pymongo
from bson import ObjectId

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
print("--- Ajouter un produit dans une wishlist ---")

buyerID = input("ID Buyer: ")
updated_buyer = db.buyers.find_one({"_id": ObjectId(buyerID)})
added_product = input("product_ID : ")
updated_buyer["wishlist"] += [ObjectId(added_product)]

result = db.buyers.update_one({"_id": ObjectId(buyerID)}, {"$set": {"wishlist": updated_buyer["wishlist"]}})
print("[INFO] Acknowledged: " + str(result.acknowledged))
print("[INFO] modified_count: " + str(result.modified_count))

print("--- Closing connexion ---")
client.close()
exit(0)

