# Tout ce qui est lié au produits
# CRUD

import datetime
import pprint
import pymongo
from pymongo import database


def createProduct(db: database.Database):
    return ""


def getProductByName(db: database.Database, name):
    product = db.products.find_one({"name": name})
    print("===================")
    pprint.pprint(product)
    return product


def getAllProducts(db: database.Database):
    products = db.products.find()
    print("===================")
    pprint.pprint(products)
    return products

def listProductsUID(db: database.Database):
    productsUIDs = list(db.products.find({},{"_id": 1}))
    print("===================")
    for (element) in productsUIDs:
        print(element)
    return productsUIDs


def linkCommentToProduct(db: database.Database, productID, commentID):
    db.products.update_one({"_id": productID}, {"$push": {"comments": commentID}})


def updateProduct():
    print("UPDATE")


def deleteProduct(db: database.Database, productID):
    db.products.delete_one({"_id": productID})
    print("DELETE")


def searchProduct():
    print("SEARCH")
