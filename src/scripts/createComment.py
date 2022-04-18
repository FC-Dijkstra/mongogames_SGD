import json
import pprint
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
client = pymongo.MongoClient(mongostring)
db = client.SGD
print("--- Connection OK ---")
print("--- Ajouter un commentaire ---")
buyerID = input("ID de l'acheteur: ")
productID = input("ID du produit: ")

# 625c18d40ad854de821d0401
# 625c23fc781677e6f2531ce5

# Check si l'utilisateur a acheté le produit
hasBought = db.orders.find_one(
    {"buyerID": ObjectId(buyerID)},
    {"order": {
        "$elemMatch": {
            "idProduct": ObjectId(productID)
        }
    }}
)
if hasBought is None:
    print("Erreur, l'utilisateur n'a pas acheté le produit")
    exit(1)

# Check si l'utilisateur a déjà commenté le produit
hasCommented = db.products.find_one(
    {
        "_id": ObjectId(productID),
        "comments.buyerID": ObjectId(buyerID)
    },
    {"comments": 1}
)

if hasCommented is not None and hasCommented.matched_count > 0:
    print("Erreur, l'utilisateur a déjà commenté sur le produit")
    exit(1)

comment = {
    "buyerID": ObjectId(buyerID),
    "date": datetime.now().isoformat(),
    "message": input("Message: "),
    "notation": input("Note (sur 5): ")
}

result = db.products.update_one({"_id": ObjectId(productID)}, {"$set": {"comments": [comment]}})
print("[INFO] Acknowledged: " + str(result.acknowledged))
print("[INFO] modifiedCount: " + str(result.modified_count))

print("--- Closing connexion ---")
client.close()
exit(0)