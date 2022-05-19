# ? Chargement fichier de configuration
import json
from datetime import datetime
from datetime import date
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
print("--- Créer un order ---")

item_ordered = []
iteration = "null"
totalamount = 0
while iteration != "end" :
        find = input("id_product (string): ").strip()
        try :
                product = db.products.find_one({"_id": ObjectId(find)})
                if product != None:
                        quantity = int(input("quantity (int) : "))
                        try :
                                if int(product["stock"]) >= quantity :
                                        price = float(product["price"])
                                        stock = int(product["stock"]) - quantity
                                        totalamount += price*quantity
                                        db.products.update_one({"_id": ObjectId(find)},
                                                           {
                                                                   "$set": {"stock": stock}
                                                           })
                                        item_ordered += [{
                                                "idProduct": ObjectId(find),
                                                "quantity": quantity,
                                                "sous-total": price*quantity
                                        }]
                                else :
                                        print("we don't have enough stock")
                        except Exception as e:
                                print("Stock or Quantity incorrect / error : ",e)
        except Exception :
                print("product not found")
        iteration = input(" it's finish ? tap end, if not just enter : ")


order = {
        "order": item_ordered,
        "buyerID": ObjectId(input("ID (string): ")),
        "date": datetime.now(),
        "totalAmount": float(totalamount),
    }

result = db.orders.insert_one(order)
print("[INFO] Acknowledged: " + str(result.acknowledged))
print("[INFO] _id: " + str(result.inserted_id))

print("--- Closing connexion ---")
client.close()
exit(0)
