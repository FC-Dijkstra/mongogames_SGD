import datetime
from datetime import datetime
import json
import uuid

import pymongo
from bson.binary import UuidRepresentation
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
print("--- Créer une promotion ---")

promotion = {
    "uuid": ObjectId(),
    "type": input("Type: (FLAT | PERCENT): "),
    "value": input("Valeur: "),
    "startDate": datetime.strptime(input("Date de début (dd/mm/YYYY): "), "%d/%m/%Y"),
    "endDate": datetime.strptime(input("Date de fin (dd/mm/YYYY): "), "%d/%m/%Y")
}

productIDs = []
stop = False
while not stop:
    productID = input("ID du produit (vide pour arréter) : ")

    if productID == "":
        stop = True
    else:
        result = db.products.update_one(
            {"_id": ObjectId(productID)},
            {"$push": { "promotions": promotion}}
        )

        print("[INFO] Acknowledged: " + str(result.acknowledged))
        print("[INFO] modifiedCount: " + str(result.modified_count))

print("--- Closing connexion ---")
client.close()
exit(0)