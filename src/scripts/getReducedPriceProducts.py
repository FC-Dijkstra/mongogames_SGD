import json
import pprint

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
print("--- Récupérer les produits en promotion ---")

products = db.products.find(
    {"promotions": {"$exists": True, "$not": {"$size": 0}}}
)

for product in products:
    pprint.pprint(product)

print("--- Closing connexion ---")
client.close()
exit(0)