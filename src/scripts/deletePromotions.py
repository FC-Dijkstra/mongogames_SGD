import datetime
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
print("--- Supprimer les promotions invalides ---")

currentdate = datetime.datetime.now()
result = db.products.update_many(
    {},
    {"$pull": {
        "promotions": {"endDate": {"$lt": currentdate}}
    }}
)

print("[INFO] Acknowledged: " + str(result.acknowledged))
print("[INFO] modifiedCount: " + str(result.modified_count))

print("--- Closing connexion ---")
client.close()
exit(0)