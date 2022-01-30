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
    input("Appuyez sur une touche pour continuer")

    # pprint.pprint(product)


def getProduct():
    print("GET")


def getAllProducts():
    print("GET ALL")


def updateProduct():
    print("UPDATE")


def deleteProduct():
    print("DELETE")


def searchProduct():
    print("SEARCH")
