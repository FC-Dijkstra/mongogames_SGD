import json
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
print("--- Supprimer un acheteur ---")

buyerID = input("ID buyer: ")
result = db.buyers.delete_one({"_id": ObjectId(buyerID)})
print("[INFO] Acknowledged: " + str(result.acknowledged))
print("[INFO] deleted: " + str(result.deleted_count))

print("--- Closing connexion ---")
client.close()
exit(0)