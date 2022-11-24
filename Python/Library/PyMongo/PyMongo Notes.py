# PYMONGO NOTES

# ACCESSING TO THE MONGO DB USING URL
from pymongo import MongoClient
import urllib.parse

# The url for the whole mongo connection (For localhost mongodb)
_username = urllib.parse.quote_plus(username)
_password = urllib.parse.quote_plus(password)

CLIENT_URL = f"mongodb://{_username}:{_password}@127.0.0.1"

# SPECIFY URL TO ACCESS ONLINE MONGO DB
DB_URL = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"

# CONECTING TO THE CLIENT
client = MongoClient(CLIENT_URL)
# client = MongoClient("mongodb://admin:admin@localhost:27017")

# Listing all the database
=====
dbs = list(client.list_databases())

# Access the database: Make sure you have the name is correct or a new database will be created
=====
db = client["database_name"]

# A way to check if the database name exists
=====
db_namelist = [db["name"] for db in dbs] # The "name" is a key here from mongodb
if "database_name" in db_namelist:
	db = client["database_name"]

# Accessing the collection
=====
collection = db["collection_name"]

# Sorting the timestamp
=====
collection.sort({"updatetime": 1})

# Query date
=====
# https://stackoverflow.com/questions/26366417/how-to-make-a-query-date-in-mongodb-using-pymongo
from datetime import datetime
start = datetime.strptime("2022-04-28", "%Y-%m-%d")
end = datetime.utcnow()

# Make sure you convert the datetime into UTC first
=====
# https://thispointer.com/convert-local-datetime-to-utc-timezone-in-python/
import pytz
start = start.astimezone(pytz.UTC)

# If your mongodb datetime is in unix format, you have to change it
start = int(start.timestamp() * 1000) # make sure to check if your mongodb is in 1000 unix form
end = int(end.timestamp() * 1000)

data = list(collection.find({"updatetime": {"$lt": end, "$gte": start}}))
# gte = greater than or equals to
# lt  = lesser than

# Exporting the data to json format but the ObjectId is not serializable
# https://stackoverflow.com/questions/16586180/typeerror-objectid-is-not-json-serializable
import json
from bson import json_util
json.loads(json_util.dumps(data))

# Using a list of ids to find query the database
=====
import pandas as pd
from bson import ObjectId

ids = ["5c8ecae42f684a30fbdfd576", "5c8ecaf82f684a30fbdfd578"]
documentIds = [ObjectId(_id) for _id in ids]
data = pd.DataFrame(collection.find({"_id": {"$in": documentIds }}))

# CREATING A NEW DATABASE AND COLLECTION & INSERT DATA
# NOTE THAT YOU HAVE TO INSERT A DATA BEFORE THE DATABASE AND THE COLLECTION SHOW UP
=====
# https://www.w3schools.com/python/python_mongodb_insert.asp
from pymongo import MongoClient
client = MongoClient("mongodb://admin:admin@localhost:27017")

db = client["newDB"]
col = db["newCol"]
# col = client["newDB"]["newCol"] # shortcut

new_data = { "name": "John", "address": "Highway 37" }
x = col.insert_one(new_data)
print(x.inserted_id)

# INSERT MANY ROW OF DATA
=====
import pymongo

myclient = pymongo.MongoClient("mongodb://admin:admin@localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
print(x.inserted_ids)

# INSERT MULTIPLE DATA WITH THE SPECIFIC IDS
=====
# Cannot reinsert using the same id, the duplication key error will occur, we can only update the databsae using the id
import pymongo

myclient = pymongo.MongoClient("mongodb://admin:admin@localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

# QUERY AND UPDATE DATA
=====
# https://www.w3schools.com/python/python_mongodb_update.asp
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  	print(x)

# QUERY WITH REGEX AND UPDATE MANY
=====
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

# ADDING THE DATA TO THE LIST IF IT DOES NOT EXIST ($addToSet)
=====
# https://stackoverflow.com/questions/38970835/mongodb-add-element-to-array-if-not-exists
client["db"]["col"].update_one(
    { "name": "sport" },
    { "$addToSet": { "videoIDs": "34f54e34d" } }, upsert=True
) # Set the upsert to True so you don't need to insert before hand

# ADDING EACH OF THE ELEMENT IN THE LIST INTO A LIST IN THE DATABSE IF IT DOES NOT EXIST
=====
# https://kb.objectrocket.com/mongo-db/how-to-add-elements-into-an-array-in-mongodb-1195
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://admin:admin@localhost:27017")
client["db"]["col"].update_one(
    { "_id": ObjectId("633111ad220ab45401f6c6c3") },
    { "$addToSet": { "videoIDs": {"$each" : ["asdf", "sdfg"] } } }, upsert=True
) # Set the upsert to True so you don't need to insert before hand

# UPDATE MULTIPLE LIST INTO MULTIPLE LIST
=====
client = MongoClient("mongodb://admin:admin@localhost:27017")
client["db"]["col"].update_one(
    { "_id": ObjectId("633111ad220ab45401f6c6c3") },
    { "$addToSet": { "postIds": {"$each" : ["abc", "erg"] }, "projIds": {"$each": ["aaa", "ghj"]} } }, upsert=True
)

# DROPPING DATABASE
=====
# https://stackoverflow.com/questions/35463526/how-do-i-drop-a-mongodb-database-using-pymongo
from pymongo import MongoClient
client = MongoClient("mongodb://admin:admin@localhost:27017")
client.drop_database("database_name")

# DROPPING COLLECTION
=====
# https://www.w3schools.com/python/python_mongodb_drop_collection.asp
import pymongo

myclient = pymongo.MongoClient("mongodb://admin:admin@localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mycol.drop()

# SET THE VALUE ON INSERT (FOR INSERT_DATE AND UPDATE FOR THE UPDATED_DATE)
=====
# https://stackoverflow.com/questions/2801008/mongodb-insert-if-not-exists/17533368#17533368
now = datetime.utcnow()
for document in update:
    collection.update_one(
        filter={
            '_id': document['_id'],
        },
        update={
            '$setOnInsert': {
                'insertion_date': now,
            },
            '$set': {
                'last_update_date': now,
            },
        },
        upsert=True,
    )

# EXPORTING THE DATA TO JSON
=====
import json
from bson import json_util
from PyMongo import MongoClient

client = MongoClient(url="mongodb://admin:admin@localhost:27017")
collection = client["dbname"]["dbcol"]

# To include the emojis, you have to make sure the encoding is utf8 and the ensure_ascii == False
# To unseen the emoji, just alter the ensure_ascii to True
with open("collection.json", "w", encoding="utf8") as file:
    json.dump(json.loads(json_util.dumps(collection.find())), file, indent=2, ensure_ascii=False)

# LOADING THE JSON FILE DATA
=====
import json
from PyMongo import MongoClient

with open("collection", "r", encoding="utf8") as f:
    dat = json.load(f)

# INSERT MANY DATA
=====
import json
from PyMongo import MongoClient

with open("data.json", "r", encoding="utf8") as f:
    data = json.load(f) # LIST

client["db"]["col"].insert_many(data)