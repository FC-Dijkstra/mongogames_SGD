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

print("lister tous les packages")
products = db.products.find()
for product in products:
    pprint.pprint(product)

print("--- Closing connexion ---")
client.close()
exit(0)