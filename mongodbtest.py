import pymongo
# create a connection between python and mongodb
client = pymongo.MongoClient("mongodb+srv://FSDS_mongodb:Fsds@mongodb@cluster0.cfqrz9t.mongodb.net/?retryWrites=true&w=majority")
# calling the connection
db = client.test
# print the connection
print (db)