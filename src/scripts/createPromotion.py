import datetime
import json

import pymongo

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

productIDs = []
stop = False
while not stop:
    productID = input("ID du produit: ")

    if productID == "":
        stop = True
    else:
        productIDs.append(productID)

promotion = {
    "type": input("Type: (FLAT | PERCENT)"),
    "value": input("Valeur: "),
    "startDate": input("Date de début"),
    "endDate": input("Date de fin")
}

print("--- Closing connexion ---")
client.close()
exit(0)