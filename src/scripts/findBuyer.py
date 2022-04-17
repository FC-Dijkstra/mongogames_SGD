# ? Chargement fichier de configuration
import json
import pprint
from datetime import datetime
from bson.objectid import ObjectId
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
updated_buyer = db.buyers.find()
for buyer in updated_buyer:
        print("{")
        for item in buyer:
                print(item," : ", buyer[item])
        print("}")


print("--- Closing connexion ---")
client.close()
exit(0)
