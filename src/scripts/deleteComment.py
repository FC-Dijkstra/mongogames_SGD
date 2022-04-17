import json

import pymongo
from bson import ObjectId

configfile = open("../../config.json")
config = json.load(configfile)
configfile.close()
print("--- Loaded config ---")

# ? configuration et connexion mongoDB
# mongodb://user:pwd@host/db?authSource=db
mongostring = f"mongodb+srv://{config['user']}:{config['password']}@{config['host']}/"
client = pymongo.MongoClient(mongostring)
db = client.SGD
print("--- Connection OK ---")
print("--- Supprimer un commentaire ---")

productID = input("ID du produit: ")
buyerID = input("ID de l'acheteur: ")

result = db.products.update_one(
    {"_id": ObjectId(productID)},
    {"$pull": {"comments": {"buyerID": ObjectId(buyerID)}}},
)
print("[INFO] Acknowledged: " + str(result.acknowledged))
print("[INFO] modifiedCount: " + str(result.modified_count))

print("--- Closing connexion ---")
client.close()
exit(0)