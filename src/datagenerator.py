from pymongo import database
import random
from datetime import *
import string
import pprint


def generateProduct(db: database.Database, quantity):
    for i in range(0, quantity):
        product = {
            "id": random.randbytes(16).hex(),
            "name": "".join(random.choice(string.ascii_letters) for i in range(30)),
            "description": "".join(random.choice(string.ascii_letters) for i in range(30)),
            "price": round(random.random() * 100, 2),
            "sales": 0,
            "notation": 0,  # 0 <= x <= 5
            "stock": random.randint(10, 500),
            "comments": [],
            "release": date.today(),
            "author": "".join(random.choice(string.ascii_letters) for i in range(30)),
            "editor": "".join(random.choice(string.ascii_letters) for i in range(30)),
            "minPlayers": random.choice([1, 2, 4]),  # au moins 1, 2 ou 4
            # >= minPlayers, 2 | 4 | 6 | 8 | 10
            "maxPlayers": random.choice([2, 4, 6, 8, 10]),
            "duration": random.randint(1, 12) * 10,  # dizaines uniquement
            "recommendedAge": random.randint(5, 18),  # 5 <= x <= 18
            "expeditionTime": random.choice([24, 48, 72]),  # 24 | 48 | 72
            "complexity": round(random.random() * 10, 1),  # 0.0 <= x <= 10.0
            # 0.0 <= x <= 10.0
            "concentration": round(random.random() * 10, 1),
            "ambience": round(random.random() * 10, 1),  # 0.0 <= x <= 0.0
        }

        pprint.pprint(product)


def generateBuyer(db: database.Database, quantity):
    quantity = int(quantity)
    for i in range(0, quantity):
        print(i)


def generateComment(db: database.Database, quantity):
    for i in range(0, quantity):
        print(i)


def generatePromotion(db: database.Database, quantity):
    for i in range(0, quantity):
        print(i)


def generatePurchase(db: database.Database, quantity):
    for i in range(0, quantity):
        print(i)


def generateData(db: database.Database):
    print("générer la totale")
