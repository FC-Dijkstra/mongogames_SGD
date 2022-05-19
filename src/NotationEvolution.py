import json
import pprint
from bson import ObjectId
import numpy as np
import matplotlib.pyplot as plt

import pymongo

configfile = open("../config.json")
config = json.load(configfile)
configfile.close()
print("--- Loaded config ---")

# ? configuration et connexion mongoDB
# mongodb://user:pwd@host/db?authSource=db
mongostring = f"mongodb+srv://{config['user']}:{config['password']}@{config['host']}/"
client = pymongo.MongoClient(mongostring)
db = client.SGD
print("--- Connection OK ---")

# INSERER CODE ICI

pipeline = [
    {"$match": {"_id": ObjectId("625c23fc781677e6f2531ce5")}},
    {"$unwind": "$comments"},
    {"$replaceRoot": {"newRoot": "$comments"}},
    {"$project": {
        "month": {"$month": {"$dateFromString": {"dateString": "$date"}}},
        "day": {"$dayOfMonth": {"$dateFromString": {"dateString": "$date"}}},
        "notation": 1
    }},
]

#Pour chaque jour du mois, on note l'évolution des notes des avis (moyenné) et le nombre de nouveaux avis.
comments = db.products.aggregate(pipeline)
comments = list(comments)

notes = [0] * 31
nbCommentaires = [0] * 31
for comment in comments:
    notes[comment["day"]] += comment["notation"]
    nbCommentaires[comment["day"]] += 1

#moyennage des jours
for i in range(0, 31):
    if nbCommentaires[i] != 0:
        notes[i] = (notes[i] / nbCommentaires[i])

#https://matplotlib.org/3.5.0/gallery/subplots_axes_and_figures/two_scales.html

plt.bar(range(0, 31), notes, color="r", label="note moyenne")
plt.plot(nbCommentaires, color="g", label="Nombre de commentaires")
plt.ylabel("Notation")
plt.xlabel("Jour")
plt.legend()
plt.show()

print("--- Closing connexion ---")
client.close()
exit(0)