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
d = input("day (dd): ")
m = input("month (mm): ")
y = input("year (YYYY) : ")
choice = input("greater than -> gte,\n lesser than -> lte,\n equals -> eq :\n ")
date = d+"/"+m+"/"+y
choice = "$"+choice

print("date : ", choice, " : ", date)

try:
    result = db.orders.aggregate([{"$match": {"date" : {choice: date}}},{"$unwind" : "$order"},{"$group": {"_id" : {"idProduct": "$order.idProduct"},
                                                                            "total": {"$sum": "$order.quantity"}}},
                              {"$project": {"_id": 1, "total" : 1, "date": 1}}, {"$sort" : {"date" : -1}}])
except Exception as e :
    print("Error !! : ", e)

for r in result:
    pprint(r)
print("--- Closing connexion ---")
client.close()
exit(0)

