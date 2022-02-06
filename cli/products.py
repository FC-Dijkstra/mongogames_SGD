# Tout ce qui est lié au produits
# CRUD

import datetime
import pprint
import pymongo
from pymongo import database


def createProduct(db: database.Database):
    product = {
        "name": input("Nom (string):"),
        "description": input("Description (string): "),
        "price": input("Prix (float): "),
        "sales": 0,
        "notation": 0,
        "stock": input("Stock (int): "),
        "comments": [],
        "release": datetime.datetime.now().isoformat(),
        "author": input("Auteur (string): "),
        "editor": input("Editeur (string): "),
        "minPlayers": input("Nombre minimum de joueurs (int): "),
        "maxPlayers": input("Nombre maximum de joueurs (int): "),
        "duration": input("Durée (int): "),
        "recommendedAge": input("Age recommandé (int): "),
        "expeditionTime": input("Délai d'envoi (int): "),
        "complexity": input("Complexité (float) (0 <= x <= 10): "),
        "concentration": input("Concentration (float) (0 <= x <= 10): "),
        "ambience": input("Ambience (float) (0 <= x <= 5)")
    }

    result = db.products.insert_one(product)
    print("===================")
    print("Acknowledged: " + str(result.acknowledged))
    print("_id: " + str(result.inserted_id))

    # pprint.pprint(product)


def getProductByName(db: database.Database, name):
    product = db.products.find_one({"name": name})
    print("===================")
    pprint.pprint(product)


def getAllProducts(db: database.Database):
    products = db.products.find()
    print("===================")
    pprint.pprint(products)

def listProductsUID(db: database.Database):
    productsUIDs = db.products.find({},{"_id": 1})
    print("===================")
    pprint.pprint(productsUIDs)


def linkCommentToProduct(db: database.Database, productID, commentID):
    db.products.update_one({"_id": productID}, {"$push": {"comments": commentID}})


def updateProduct():
    print("UPDATE")


def deleteProduct():
    print("DELETE")


def searchProduct():
    print("SEARCH")
