import json
import pprint

import pymongo
from bson import ObjectId

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
print("--- Mettre a jour une promotion ---")

promotionID = input("ID de la promotion: ")
pipeline = [
    {"$unwind": "$promotions"},
    {"$match": {"promotions.uuid": ObjectId(promotionID)}},
    {"$limit": 1},
    {"$replaceRoot": { # permet de retourner le sous-document
        "newRoot": "$promotions"
    }}
]
promotion = list(db.products.aggregate(pipeline))[0]

type = input("Type: ") or promotion.type
value = input("Valeur: ") or promotion.valeur
startDate = input("Date de debut: ") or promotion.startDate
endDate = input("Date de fin: ") or promotion.endDate

result = db.products.update_many(
    {"promotions.uuid": ObjectId(promotionID)},
    {"$set": {
        "promotions.$.type": type,
        "promotions.$.value": value,
        "promotions.$.startDate": startDate,
        "promotions.$.endDate": endDate
    }}
)

print("[INFO] Acknowledged: " + str(result.acknowledged))
print("[INFO] modifiedCount: " + str(result.modified_count))

print("--- Closing connexion ---")
client.close()
exit(0)