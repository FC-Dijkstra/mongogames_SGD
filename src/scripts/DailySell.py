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
print("--- Statistiques de vente ---")

# ? configuration et connexion mongoDB
# mongodb://user:pwd@host/db?authSource=db
mongostring = f"mongodb+srv://{config['user']}:{config['password']}@{config['host']}/"
print(mongostring)

client = pymongo.MongoClient(mongostring)
db = client.SGD
print("--- Connection OK ---")
d = input("jour (dd): ")
m = input("mois (mm): ")
y = input("année (YYYY) : ")
choice = input("après -> gte,\n avant -> lte,\n jour même -> eq :\n ")
date = datetime.now()
date = date.replace(int(y), int(m), int(d), 0, 0, 0, 0)
print(date)
choice = "$"+choice
result = None
print("date : ", choice, " : ")

#si on veut une date avant / après
if choice != "$eq" :
    result = db.orders.aggregate([
        {"$match": {"date": {choice: date}}},
        {"$unwind" : "$order"},
        {"$group": {
            "_id" :"$order.idProduct",
            "total": {
                "$sum": "$order.quantity"}
        }},
        {"$project": {
            "_id": 1,
            "total": 1,
            "date": 1}
        },
        {"$sort" : {"date" : -1}}])
#si on veut une date le jour même
else :
    date = date.replace(date.year,date.month,date.day,0,0,0,0)
    datef = date.replace(date.year,date.month,date.day+1,0,0,0,0)
    result = db.orders.aggregate([
        {"$match": {"date" : {"$gte": date, "$lt": datef}}},
        {"$unwind" : "$order"},
        {"$group": {
            "_id" :"$order.idProduct",
            "total": {
                "$sum": "$order.quantity"
            }
        }},
        {"$project": {"_id": 1, "total" : 1, "date": 1}},
        {"$sort" : {"date" : -1}}])

for r in result:
    product = db.products.find_one({"_id": r["_id"]})
    print("product name : ",product["name"],"\nauthor : ", product["author"],"\ntotal price : ", float(product["price"])*int(r["total"]),"\n")
    pprint(r)

print("--- Closing connexion ---")
client.close()
exit(0)

