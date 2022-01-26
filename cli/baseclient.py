import os
import json
from sshtunnel import BaseSSHTunnelForwarderError
from sshtunnel import SSHTunnelForwarder
import pymongo
import pprint
import cmd

# * Classe pour la CLI

class CLI(cmd.Cmd):
    intro = "CLI pour gérer mongogames (help pour de l'aide"
    prompt = "~> "

    def do_quit(self, line):
        """Quitter la CLI"""
        print("--- Closing conneion ---")
        client.close()
        sshServer.stop()
        exit(0)

    def do_test(self, text):
        """Tester l'accès à la base mongoDB"""
        db = client[config["mongo_db"]]
        pprint.pprint(db.list_collection_names())


# ? nettoyage de l'interface
os.system("clear")

# ? Chargement fichier de configuration
configfile = open("./config.json")
config = json.load(configfile)
configfile.close()
# pprint.pprint(config)
print("--- Loaded config ---")

# ? configuration et connexion ssh
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
mongostring = f"mongodb://{config['mongo_user']}:{config['mongo_pass']}@{config['remote_host']}/{config['mongo_db']}?authSource={config['mongo_db']}"

client = pymongo.MongoClient(mongostring, sshServer.local_bind_port)
print("--- Connection OK ---")

cli = CLI()
cli.cmdloop()
