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
print("--- Modification du produit ---")
productID = input("ID du produit: ")
product = db.products.find_one({"_id": ObjectId(productID)})
pprint.pprint(product)

print("Laisser vide pour conserver la valeur précédente")

name = input("Nom: ") or product["name"]
description = input("Description: ") or product["description"]
price = input("Prix: ") or product["price"]
stock = input("Stock: ") or product["stock"]
author = input("Auteur: ") or product["author"]
editor = input("Editeur: ") or product["editor"]
minPlayers = input("Nombre min. de joueurs: ") or product["minPlayers"]
maxPlayers = input("Nombre max. de joueurs: ") or product["maxPlayers"]
duration = input("Durée: ") or product["duration"]
recommendedAge = input("Age recommandé: ") or product["recommendedAge"]
expeditionTime = input("Délai d'envoi: ") or product["expeditionTime"]
complexity = input("Complexité: ") or product["complexity"]
concentration = input("Concentration: ") or product["concentration"]
ambience = input("Ambiance: ") or product["ambience"]

modifications = {
    "name": name,
    "description": description,
    "price": price,
    "stock": stock,
    "author": author,
    "editor": editor,
    "minPlayers": minPlayers,
    "maxPlayers": maxPlayers,
    "duration": duration,
    "recommendedAge": recommendedAge,
    "expeditionTime": expeditionTime,
    "complexity": complexity,
    "concentration": concentration,
    "ambience": ambience
}

result = db.products.update_one({"_id": ObjectId(productID)}, {"$set": modifications})
print("[INFO] Acknowledged: " + str(result.acknowledged))
print("[INFO] modifiedCount: " + str(result.modified_count))


print("--- Closing connexion ---")
client.close()
exit(0)