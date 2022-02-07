import os
import json
from sshtunnel import BaseSSHTunnelForwarderError
from sshtunnel import SSHTunnelForwarder
import pymongo
import pprint
import cmd
import subprocess
import psutil


import datagenerator
import products

LOCAL = True

# * variables globales
client: pymongo.MongoClient
db: pymongo.database.Database


# * Classe pour la CLI

class CLI(cmd.Cmd):
    intro = "MongoGames Shell  || (help pour plus d'informations)"
    prompt = "~> "

    def do_quit(self, line):
        """Quitter la CLI"""
        print("--- Closing connexion ---")
        client.close()
        sshServer.stop()
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


# ? nettoyage de l'interface
def clearScreen():
    os.system("clear")


clearScreen()

# ? Chargement fichier de configuration
if (LOCAL == True):
    configfile = open("./config_LOCAL.json")
elif (LOCAL == False):
    configfile = open("./config_FAC.json")
config = json.load(configfile)
configfile.close()
# pprint.pprint(config)
print("--- Loaded config ---")

# ? configuration et connexion ssh
if (LOCAL == False):
    sshServer = SSHTunnelForwarder(
        config["mongo_host"],
        ssh_username=config["ssh_username"],
        ssh_password=config["ssh_password"],
        remote_bind_address=(config["remote_host"], config["remote_port"])
    )

    try:
        sshServer.start()
    except BaseSSHTunnelForwarderError:
        print("Erreur de connexion SSH. Le VPN est-il actif ?")
        exit(1)



# ? configuration et connexion mongoDB
# mongodb://user:pwd@host/db?authSource=db
if (LOCAL == False):
    mongostring = f"mongodb://{config['mongo_user']}:{config['mongo_pass']}@{config['remote_host']}/{config['mongo_db']}?authSource={config['mongo_db']}"
elif (LOCAL == True):
    mongostring = f"mongodb://ian:aaa@localhost/admin"


try:
    if (LOCAL == True):
        client = pymongo.MongoClient(mongostring, serverSelectionTimeoutMS=1000)
    elif (LOCAL == False):
        client = pymongo.MongoClient(mongostring, sshServer.local_bind_port, serverSelectionTimeoutMS=1000)
    client.server_info()
    db = client[config["mongo_db"]]
    print("--- Connection OK ---")
    cli = CLI()
    cli.cmdloop()
except:
    print("Invalid connexion, aborting.")
    exit(1)