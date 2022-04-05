import datetime
import pprint
import pymongo
from pymongo import database


def createPurchase(db: database.Database):
    # choisir un acheteur
    # choisir un(plusieurs) produit
    print("TODO")

def deletePurchase(db: database.Database, purchaseID):
    db.purchase.delete_one({"_id": purchaseID})
