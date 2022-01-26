from pymongo import database
import random
import string

def generateProduct(db: database.Database, quantity):
    for i in range(1, quantity):
        id = random.randbytes(16).hex()
        name = ""
        description = "" 
        price = 0.0
        sales = 0
        notation = 0 # 0 <= x <= 5
        stock = 10 # min 10
        comments = []
        seller = ""
        release = "26/01/2022"
        author = ""
        editor = ""
        minPlayers = 1  # au moins 1, 2 ou 4
        maxPlayers = 4  # >= minPlayers, 2 | 4 | 6 | 8 | 10
        duration = 20  # dizaines uniquement
        recommendedAge = 5  # 5 <= x <= 18
        expeditionTime = random.choice([24, 48, 72])  # 24 | 48 | 72
        complexity = 0.0  # 0.0 <= x <= 10.0
        concentration = 0.0  # 0.0 <= x <= 10.0
        ambience = 0.0  # 0.0 <= x <= 0.0
