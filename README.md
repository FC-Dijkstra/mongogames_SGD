# mongogames_SGD
Projet de SGD (M1S2)

**A RENDRE: 19 MAI**

doit contenir:
- scripts mongoDB
- scripts py exécutabbles
- rapport

## Contexte

Base de données mongoDB pour un site de vente de jeux.

doit gérer:
- jeux (nom, description, prix, categorie, auteur)
- categories de jeux
- auteurs 
- avis
- ...

fonctionnalités:
- catalogue
- avis
- jeux bien notés
- jeux beaucoup commentés
- /jeu ou /categorie

## 1ere partie: conception

Modèle UML et fichiers JSON d'exemple.

Justifier le schéma par rapport au notions de polymorphisme, imbrication et référence. 

## 2e partie: requêtes
Langage: **Python**
Driver: **PyMongo**

Proposer toutes les requêtes possibles (CRUD + extras)

Instructions *find*, *agregate* et une requête expliquée en *MapReduce*

## 3e partie: Python et pyMongo

requêtes complémentaires plus complexes sur les jeux et les commentaires à des fins d'analyse décisionnelle.

## Pour lancer le projet

La version de python nécessaire est la version 3.9
Il doit y avoir les bibliothèques suivantes d'installées:

* matplotlib
* pymongo\[srv\]
* tkinter (normalement fourni avec python)
