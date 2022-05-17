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
print("--- Voir le prix actuel d'un élément (promotions appliquées) ---")

productID = input("ID du produit: ")
product = db.products.find_one({"_id": ObjectId(productID)})
# on considère qu'il ne reste que les promotions actives (CF cleanPromotions.py)

price = float(product["price"])
for promotion in product["promotions"]:
    if promotion["type"] == "FLAT":
        price = price - int(promotion["value"])
    elif promotion["type"] == "PERCENT":
        price = price - (price * (int(promotion["value"]) / 100))

print("Prix réel (avec promotions): " + str(price))

print("--- Closing connexion ---")
client.close()
exit(0)