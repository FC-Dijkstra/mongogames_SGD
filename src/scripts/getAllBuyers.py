# ? Chargement fichier de configuration
import json
import pprint
from datetime import datetime
from bson.objectid import ObjectId
from pprint import pprint
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
print("--- find all buyers ---")
buyers = db.buyers.find()
for buyer in buyers:
        pprint(buyer)


print("--- Closing connexion ---")
client.close()
exit(0)
