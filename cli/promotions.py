import datetime
import pprint
import pymongo
from pymongo import database


def createPromotion(db: database.Database):
    promotion = {
        "type": input("Type (FLAT | PERCENT): "),
        "value": input("Value (float): "),
        "expirationDate": input("ExpirationDate (date) (DD/MM/YYYY): "),
        "releaseDate": input("ReleaseDate (date) (DD/MM/YYYY): ")
    }

    result = db.promotions.insert_one(promotion)
    print("===================")
    print("Acknowledged: " + str(result.acknowledged))
    print("_id: " + str(result.inserted_id))
