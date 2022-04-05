import datetime
import pprint
import string
import pymongo
from pymongo import database


def createComment(db: database.Database):
    comment = {
        "buyer": "",
        "date": datetime.date().today().isoformat(),
        "message": input("Message (string) : "),
        "notation": input("Notation (float) (1 <= x <= 5")
    }

    result = db.comments.insert_one(comment)
    print("===================")
    print("Acknowledged: " + str(result.acknowledged))
    print("_id: " + str(result.inserted_id))

    # TODO: lien commentaire <-> produit

#
#def deleteComment(db: database.Database, commentID, productID):
#    db.products.update_one({"_id" : productID},{"$pull" : {"comments.id[{commentID}]"} })
