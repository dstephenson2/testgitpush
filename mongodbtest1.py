import pymongo
# create a connection between python and mongodb
client = pymongo.MongoClient("mongodb+srv://FSDS_mongodb:Fsds_mongodb@cluster0.cfqrz9t.mongodb.net/?retryWrites=true&w=majority")
# calling the connection
db = client.test
# print the connection
print (db)

# mongodb is a nosql database
# dump some sort of a record, create a dictionary
d = {
    "name":"daniel",
    "email_id":"sdaniel.stephenson@gmail.com",
    "surname":"stephen"
}

db1 = client['mongodbtest1']
coll = db1['test']
coll.insert_one(d )