from tkinter import *

import json
from datetime import datetime
from tkinter.messagebox import showinfo

import pymongo

configfile = open("../config.json")
config = json.load(configfile)
configfile.close()
print("--- Loaded config ---")

# ? configuration et connexion mongoDB
# mongodb://user:pwd@host/db?authSource=db
mongostring = f"mongodb+srv://{config['user']}:{config['password']}@{config['host']}/"
print(mongostring)

client = pymongo.MongoClient(mongostring)
db = client.SGD
print("--- Connection OK ---")
print("--- Créer un acheteur ---")

def process () :
    buyer = {
        "name": name.get(),
        "fstName": fstname.get(),
        "nickname": nickname.get(),
        "password": password.get(),
        "wishlist": []
    }
    result = db.buyers.insert_one(buyer)
    print("[INFO] Acknowledged: " + str(result.acknowledged))
    print("[INFO] _id: " + str(result.inserted_id))
    showinfo("Réponse de la DB", "Acknowledged: " + str(result.acknowledged))



window = Tk()
window.title("Créer un compte")
window.geometry("300x100")

name = StringVar()
name.set("nom")
textinput1 = Entry(window, textvariable=name, width=50)
textinput1.pack()

fstname = StringVar()
fstname.set("prénom")
textinput2 = Entry(window, textvariable=fstname, width=50)
textinput2.pack()

nickname = StringVar()
nickname.set("pseudo")
textinput3 = Entry(window, textvariable=nickname, width=50)
textinput3.pack()

password = StringVar()
password.set("mot de passe")
textinput4 = Entry(window, textvariable=password, width=50)
textinput4.pack()


validate = Button(window, text="Ajouter à la base", command=process)
validate.pack()

window.mainloop()