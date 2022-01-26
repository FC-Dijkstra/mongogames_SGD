mongod --dbpath ./db
mongo --host localhost --port 27017

# use admin
# db.createUser({user: "ian", pwd: "aaa", roles: ["root"]})
# show users
# db.shutdownServer()

#mongodb://ian:aaa@localhost/admin