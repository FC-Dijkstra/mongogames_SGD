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
print("--- Mettre a jour un commentaire ---")

productID = input("ID du produit: ")
buyerID = input("ID de l'acheteur: ")

comment = db.products.find_one(
    {"_id": ObjectId(productID)},
    {"comments": {
        "$elemMatch": {
            "buyerID": ObjectId(buyerID)
        }
    }}
)

if comment is None:
    print("Erreur, aucun commentaire trouvé.")
    exit(1)

message = input("Message: ") or comment["message"]
notation = int(input("Note: ")) or comment["notation"]

result = db.products.update_one(
    {
        "_id": ObjectId(productID),
        "comments.buyerID": ObjectId(buyerID)
    },
    {
        "$set": {
            "comments.$.message": message,
            "comments.$.notation": notation
        }
    }
)

print("[INFO] Acknowledged: " + str(result.acknowledged))
print("[INFO] modifiedCount: " + str(result.modified_count))

print("--- Closing connexion ---")
client.close()
exit(0)