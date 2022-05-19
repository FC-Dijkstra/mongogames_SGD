# ? Chargement fichier de configuration
import json
from datetime import datetime

import pymongo

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
print("--- Créer un produit ---")
product = {
    "name": input("Nom (string):"),
    "description": input("Description (string): "),
    "price": float(input("Prix (float): ")),
    "sales": 0,
    "notation": 0,
    "stock": int(input("Stock (int): ")),
    "comments": [],
    "promotions": [],
    "release": datetime.now().isoformat(),
    "author": input("Auteur (string): "),
    "editor": input("Editeur (string): "),
    "minPlayers": int(input("Nombre minimum de joueurs (int): ")),
    "maxPlayers": int(input("Nombre maximum de joueurs (int): ")),
    "duration": int(input("Durée (int): ")),
    "recommendedAge": int(input("Age recommandé (int): ")),
    "expeditionTime": int(input("Délai d'envoi (int): ")),
    "complexity": float(input("Complexité (float) [0;10]: ")),
    "concentration": float(input("Concentration (float) [0; 10]: ")),
    "ambience": float(input("Ambience (float) [0; 10]: "))
}

result = db.products.insert_one(product)
print("[INFO] Acknowledged: " + str(result.acknowledged))
print("[INFO] _id: " + str(result.inserted_id))

print("--- Closing connexion ---")
client.close()
exit(0)