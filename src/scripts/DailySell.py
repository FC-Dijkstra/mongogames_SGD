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
d = input("day (dd): ")
m = input("month (mm): ")
y = input("year (YYYY) : ")
choice = input("greater than -> gte,\n lesser than -> lte,\n equals -> eq :\n ")
date = datetime.now()
date = date.replace(int(y), int(m), int(d), 0, 0, 0, 0)
print(date)
choice = "$"+choice
result = None
print("date : ", choice, " : ")

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

