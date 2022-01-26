import os
import json
from sshtunnel import BaseSSHTunnelForwarderError
from sshtunnel import SSHTunnelForwarder
import pymongo
import pprint

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

# ! insérer code sur les tables ici.
db = client[config["mongo_db"]]
pprint.pprint(db.list_collection_names())
pprint.pprint(next(db['etudiants'].find()))

# ? fermeture de la connexion
print("--- Closing connexion ---")
sshServer.stop()
exit(0)
