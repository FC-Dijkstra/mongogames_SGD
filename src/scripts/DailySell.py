# ? Chargement fichier de configuration
import json
from datetime import datetime, date
from pprint import pprint
import pymongo
from bson import ObjectId

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

result = db.orders.aggregate([{"$unwind" : "$order"},{"$group": {"_id" : "$order.idProduct","total" : {"$sum" : "$order.quantity"}}},{"$sort" : {"date" : -1}}])
for r in result:
    pprint(r)
print("--- Closing connexion ---")
client.close()
exit(0)

