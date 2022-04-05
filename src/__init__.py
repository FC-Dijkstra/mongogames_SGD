import os
import json
import pprint
import pymongo
import cmd

from pymongo import database

import datagenerator
import products

# * variables globales
client: pymongo.MongoClient
db: database.Database
currentUID: str = ""
currentType: str = ""


# * Classe pour la CLI

class CLI(cmd.Cmd):
    intro = "MongoGames Shell  || (help pour plus d'informations)"
    prompt = f"[{currentUID}][{currentType}] > "

    def do_quit(self, line):
        """Quitter la CLI"""
        print("--- Closing connexion ---")
        client.close()
        exit(0)

    def do_generate(self, text):
        """generate <product|buyer|comment|promotion|purchase|data> <quantity>"""
        """Génère des données aléatoires"""
        if text:
            text = text.split()
            db = client[config["mongo_db"]]
            if text[0] == "product":
                datagenerator.generateProduct(db, text[1])
            elif text[0] == "buyer":
                datagenerator.generateBuyer(db, text[1])
            elif text[0] == "comment":
                datagenerator.generateComment(db, text[1])
            elif text[0] == "promotion":
                datagenerator.generatePromotion(db, text[1])
            elif text[0] == "purchase":
                datagenerator.generatePurchase(db, text[1])
            elif text[0] == "data":
                datagenerator.generateData(db, text[1])
            else:
                print("Argument invalide")
        else:
            print("Vous devez préciser deux arguments")

    def do_create(self, arg):
        """create <product|comment|buyer|promotion|purchase>"""
        """Crée un objet du type spécifié et l'insère dans la table"""
        if arg:
            if arg == "product":
                products.createProduct(db)
            elif arg == "comment":
                print("create comment")
            elif arg == "buyer":
                print("buyer")
            elif arg == "promotion":
                print("create promotion")
            elif arg == "purchase":
                print("purchase")
        else:
            print("Vous devez préciser le type d'objet a créer")

    def do_list(self, arg):
        if arg:
            if arg == "product":
                products.listProductsUID(db)


# ? Chargement fichier de configuration
configfile = open("../config.json")
config = json.load(configfile)
configfile.close()
pprint.pprint(config)
print("--- Loaded config ---")

# ? configuration et connexion mongoDB
# mongodb://user:pwd@host/db?authSource=db
mongostring = f"mongodb+srv://{config['user']}:{config['password']}@{config['host']}/myFirstDatabase?retryWrites=true&w=majority"
print(mongostring)


client = pymongo.MongoClient(mongostring)
db = client.test
print("--- Connection OK ---")
cli = CLI()
cli.cmdloop()

