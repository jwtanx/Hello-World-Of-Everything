from pymongo import MongoClient
import urllib.parse

# The url for the whole mongo connection (For localhost mongodb)
_username = urllib.parse.quote_plus(username)
_password = urllib.parse.quote_plus(password)

CLIENT_URL = f"mongodb://{_username}:{_password}@127.0.0.1"

# Specific url to access online mongo into the specific database name
DB_URL = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"

# Connecting to the client
client = MongoClient(CLIENT_URL)
# client = MongoClient("mongodb://admin:admin@localhost:27017")

# Listing all the database
dbs = list(client.list_databases())

# Access the database: Make sure you have the name is correct or a new database will be created
db = client["database_name"]

# A way to check if the database name exists
db_namelist = [db["name"] for db in dbs] # The "name" is a key here from mongodb
if "database_name" in db_namelist:
	db = client["database_name"]

# Accessing the collection
collection = db["collection_name"]

# Sorting the timestamp
collection.sort({"updatetime": 1})

# Query date
# https://stackoverflow.com/questions/26366417/how-to-make-a-query-date-in-mongodb-using-pymongo
from datetime import datetime
start = datetime.strptime("2022-04-28", "%Y-%m-%d")
end = datetime.now()

# Make sure you convert the datetime into UTC first
# https://thispointer.com/convert-local-datetime-to-utc-timezone-in-python/
import pytz
start = start.astimezone(pytz.UTC)
end = end.astimezone(pytz.UTC)

# If your mongodb datetime is in unix format, you have to change it
start = int(start.timestamp() * 1000) # make sure to check if your mongodb is in 1000 unix form
end = int(end.timestamp() * 1000)

data = list(collection.find({'updatetime': {'$lt': end, '$gte': start}}))
# gte = greater than or equals to
# lt  = lesser than

# Exporting the data to json format but the ObjectId is not serializable
# https://stackoverflow.com/questions/16586180/typeerror-objectid-is-not-json-serializable
import json
from bson import json_util
json.loads(json_util.dumps(data))