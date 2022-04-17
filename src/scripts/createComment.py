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
client = pymongo.MongoClient(mongostring)
db = client.SGD
print("--- Connection OK ---")
print("--- Ajouter un commentaire ---")
buyerID = input("ID de l'acheteur")
productID = input("ID du produit")

# TODO: check si a acheté produit
hasBought = db.orders.find({"buyerID": ObjectId(buyerID), "order."})
# TODO: check si pas de commentaire existant (limite 1)

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