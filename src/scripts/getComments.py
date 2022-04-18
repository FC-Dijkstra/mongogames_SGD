import json
import pprint

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
print("--- Récupérer les commentaires d'un produit ---")

productID = input("ID d'un produit: ")
comments = db.products.find_one(
    {"_id": ObjectId(productID)},
    {"comments": 1}
)
pprint.pprint(comments)

print("--- Closing connexion ---")
client.close()
exit(0)