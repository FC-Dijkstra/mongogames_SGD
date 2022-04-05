# Tout ce qui est lié aux acheteurs
# CRUD

import datetime
import pprint
import pymongo
from pymongo import database


def createBuyer(db: database.Database):
    buyer = {
        "name": input("name (string): "),
        "fstName": input("first name (string): "),
        "nickname": input("nickname (string): "),
        "password": input("password (string): "),
        "wishlist": []
    }

    result = db.buyers.insert_one(buyer)
    print("=====================")
    print("Acknowledged: " + str(result.acknowledged))
    print("_id: " + str(result.inserted_id))


def deleteBuyer(db: database.Database, BuyerID):
    db.buyer.delete_one({"_id": BuyerID})
