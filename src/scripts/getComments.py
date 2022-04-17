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
print("--- Récupérer les commentaires d'un produit ---")

productID = input("ID d'un produit: ")
product = db.products.find({"_id"})

print("--- Closing connexion ---")
client.close()
exit(0)