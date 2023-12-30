# Cheat Sheet

## INSTALLATION
[Reference](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#std-label-install-mdb-community-ubuntu)
To enable automated startup of mongodb
```sh
sudo systemctl enable mongod
```

## AFTER REBOOT
> You might face mongod cannot be started due to permission: [Reference](https://askubuntu.com/a/1103513)
```sh
sudo chown mongodb:mongodb /tmp/mongodb-27017.sock
sudo service mongod restart
```

## Getting into Mongo Shell
`mongosh`

## QUICK START
```s
# Checking version
db.version()

# Get all the help
db.help()

# Get the list of database
show dbs

# Switching to another database by `use <DATABASE_NAME>`
use local

# Getting collections
show collections

# Getting the stats
db.stats()
```

## LEARN
### AUTHENTICATION
```js
db = db.getSiblingDB("admin") # Or you can just `use admin`
db.auth(<username>, <password>)
```
Example: `db.auth("admin", "admin")`

### CREATE & DELETE DATABASE
> NOTE: Database `forum` is not created yet until it has the data in it
```sh
# Create database
# use <NEW_DATABASE_NAME>
use forum

# Delete database
db.dropDatabase();
# { ok: 1, dropped: 'forum' }
```
There is no way to rename the database but we can move the data into the new database
```sh
# Dump the database
mongodump --db oldDatabaseName --out /path/to/output/directory

# Restore it with a new name
mongorestore --db newDatabaseName /path/to/output/directory/oldDatabaseName

# Delete the old database
# First, start the mongo shell and switch to the old database
mongo
use oldDatabaseName
db.dropDatabase();
```

### CREATE & DELETE & RENAME COLLECTION
```sh
# Create collection
db.createCollection("clothes");

# Rename collection
db.clothes.renameCollection("posts")

# Delete collection
# db.<COLLECTION_NAME>.drop()
db.posts.drop();

```

### INSERT ONE RECORD
> Take in one object and insert into the collection
```sh
# insertOne( {...} )
db.posts.insertOne({
  title: "What is the best way to learn JavaScript from the ground up?",
  postId: NumberInt(3511),
  comments: 10,
  shared: true,
  tags: [
    "JavaScript",
    "programming"
  ],
  author: {
    name: "Mike Forester",
    nickname: "mikef"
  }
})
```

### INSERT MANY RECORDS
> Take in an array of objects and insert into the collection
```sh
# insertMany( [{...}, {...}, {...}] )
var docs = [
  {
    title: "My thoughts about 12-factor App Methodology",
    postId: NumberInt(2618),
    comments: 0,
    shared: false,
    tags: [],
    author: {
      name: "Emily Watson",
      nickname: "emily23"
    }
  },
  {
    title: "Who can suggest best computer coding book for beginners?",
    postId: NumberInt(8451),
    comments: 2,
    shared: false,
    tags: [
      "programming",
      "coding"
    ],
    author: {
      name: "Emily Watson",
      nickname: "emily23"
    }
  },
  {
    title: "I want to start my own business. What I need to do first?",
    postId: NumberInt(3015),
    comments: 25,
    shared: true,
    tags: [
      "business",
      "money"
    ],
    author: {
      name: "Bob Hutchinson",
      nickname: "bob1995"
    }
  },
  {
    title: "What is the average salary of the junior frontend developer?",
    postId: NumberInt(1151),
    comments: 0,
    shared: false,
    author: {
      name: "Mike Forester",
      nickname: "mikef"
    }
  }
];

db.posts.insertMany(docs);
```

### DELETE ONE RECORD
```js
// deleteOne({query})
db.posts.deleteOne({postId: 3015})
```

### DELETE MANY RECORDS
```js
// deleteMany({query})
db.posts.deleteMany({shared: false})

// Delete all records
db.posts.deleteMany({title: null})
```

### UPDATE RECORDS
> Parameters: (query, update, options)
Update Operators

| Operator       | Description                                                                             | Example                                                                          |
| -------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `$set`         | Sets the value of a field in a document.                                                | `db.posts.updateOne({ postId: 3015 }, { $set: { shared: true } })`               |
| `$unset`       | Removes the specified field from a document.                                            | `db.posts.updateOne({ postId: 3015 }, { $unset: { shared: "" } })`               |
| `$inc`         | Increments the value of the field by the specified amount.                              | `db.posts.updateOne({ postId: 3015 }, { $inc: { comments: 1 } })`                |
| `$rename`      | Renames a field.                                                                        | `db.posts.updateOne({ postId: 3015 }, { $rename: { "comments": "feedback" } })`  |
| `$currentDate` | Sets the value of a field to current date, either as a Date or a Timestamp.             | `db.posts.updateOne({ postId: 3015 }, { $currentDate: { lastModified: true } })` |
| `$addToSet`    | Adds a value to an array unless the value is already present.                           | `db.posts.updateOne({ postId: 3015 }, { $addToSet: { tags: "unique tag" } })`    |
| `$mul`         | Multiplies the value of the field by the specified amount.                              | `db.posts.updateOne({ postId: 3015 }, { $mul: { comments: 2 } })`                |
| `$min`         | Only updates the field if the specified value is less than the existing field value.    | `db.posts.updateOne({ postId: 3015 }, { $min: { comments: 10 } })`               |
| `$max`         | Only updates the field if the specified value is greater than the existing field value. | `db.posts.updateOne({ postId: 3015 }, { $max: { comments: 20 } })`               |
| `$push`        | Appends a specified value to an array.                                                  | `db.posts.updateOne({ postId: 3015 }, { $push: { tags: "new tag" } })`           |
| `$pop`         | Removes the first or last item of an array.                                             | `db.posts.updateOne({ postId: 3015 }, { $pop: { tags: 1 } })`                    |
| `$addToSet`    | Adds a value to an array unless the value is already present.                           | `db.posts.updateOne({ postId: 3015 }, { $addToSet: { tags: "unique tag" } })`    |


#### UPDATE ONE RECORD
```js
// updateOne({query}, <update>, <options>)
db.posts.updateOne({postId: 2618}, {$set: {shared: true}})
db.posts.updateOne({postId: 1151}, {$set: {title: "What is the average salary of the senior frontend developer?"}})
```

#### UPDATE MANY RECORDS
```js
// updateMany({query}, <update>, <options>)
db.posts.updateMany({tags: []}, {$unset: {tags: 1}})
// The `1` here is just a placeholder, you can put any number, the output will still be the same

// Increasing & decreasing the value
db.posts.updateMany({shared: true}, {$inc: {comments: 2}})
db.posts.updateMany({shared: true}, {$inc: {comments: -2}})
```

### FIND RECORDS
```js
// db.yourCollectionName.find({query})
db.posts.find({shared: 3015})

// db.getCollection("yourCollectionName").find({query})
// Find matching query using nested object
db.getCollection("posts").find({"author.nickname": {$eq: "emily23"}})
db.posts.find({"author.nickname": "emily23"})
```

### FIND ONE RECORD
```js
// db.yourCollectionName.findOne({query})
db.posts.findOne({postId: 8451})

// db.getCollection("yourCollectionName").findOne({query})
db.getCollection("posts").findOne({"tags": {$in: ["programming"]}})

```

### QUERY OPERATOR

| Query    | Description                                                    | Example                                                                         |
| -------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `$lt`    | Checks if the field value is less than                         | `db.posts.find({comments: {$lt: 5}})`                                           |
| `$gt`    | Checks if the field value is greater than                      | `db.posts.find({comments: {$gt: 0}})`                                           |
| `$in`    | Checks if an element in the field                              | `db.posts.find({tags: {$in: ["programming", "coding"]}})`                       |
| `$nin`   | Checks if an element not in the field                          | `db.posts.find({tags: {$nin: ["money"]}})`                                      |
| `$eq`    | Chceks if the field is equal to something                      | `db.posts.find({shared: {$eq: true}})`                                          |
| `$ne`    | Checks if the field is not equal to something                  | `db.posts.find({shared: {$ne: false}})`                                         |
| `$or`    | Checks and return records if matches any one of the conditions | `db.posts.find({$or: [{shared: {$eq: true}}, {tags: {$in: ["programming"]}}]})` |
| `$and`   | Checks and return records if matches all the conditions        | `db.posts.find({$and: [{comments: {$gt: 0}}, {comments: {$lt: 5}}]})`           |
| `$regex` | Regular expression                                             | `db.posts.find({"author.name": {$regex: /^Emily/ }})`                           |
| `$exist` | Checks if a field exists                                       | `db.posts.find({title: {$exists: false}})`                                      |

#### EQUAL - $eq
```js
db.getCollection("posts").find({"author.nickname": {$eq: "emily23"}})

// Shortcut
db.posts.find({"author.nickname": "emily23"})

```

#### IS IN - $in
```js
db.getCollection("posts").find({"tags": {$in: ["programming"]}})

// Shortcut
db.posts.find({"tags": "programming"})

// Finding multiple elements (if OR and AND condition met)
db.posts.find({"tags": {$in: ["programming", "coding"]}})

```

#### CHECK EXIST - $exist
```js
db.posts.find({title: {$exist: false}})

// Shortcut
db.posts.find({title: null})

```

#### REGULAR EXPRESSION - $regex
| Pattern  | Description                                                          |
| -------- | -------------------------------------------------------------------- |
| `^`      | Matches the start of the string.                                     |
| `$`      | Matches the end of the string.                                       |
| `.`      | Matches any single character except newline characters.              |
| `*`      | Matches zero or more occurrences of the previous character or group. |
| `+`      | Matches one or more occurrences of the previous character or group.  |
| `?`      | Makes the previous character or group optional.                      |
| `\d`     | Matches any digit (equivalent to `[0-9]`).                           |
| `\D`     | Matches any non-digit character (equivalent to `[^0-9]`).            |
| `\w`     | Matches any word character (equivalent to `[a-zA-Z0-9_]`).           |
| `\W`     | Matches any non-word character (equivalent to `[^a-zA-Z0-9_]`).      |
| `\s`     | Matches any whitespace character (spaces, tabs, line breaks).        |
| `\S`     | Matches any non-whitespace character.                                |
| `[abc]`  | Matches any of the characters inside the square brackets.            |
| `[^abc]` | Matches any character that is not inside the square brackets.        |
| `(abc)`  | Matches the group "abc".                                             |
| `a{3}`   | Matches exactly three 'a' characters.                                |
| `a{3,}`  | Matches three or more 'a' characters.                                |
| `a{3,6}` | Matches between three and six 'a' characters.                        |

### HELPER FUNCTIONS
| Function           | Description                                                                                                                        | Example                                     |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| `sort()`           | Sorts the documents in an array in ascending or descending order based on the specified expression. (1: ascending, -1: descending) | `db.posts.find().sort({ title: -1 })`       |
| `limit()`          | Limits the number of documents in the result set.                                                                                  | `db.posts.find().limit(5)`                  |
| `skip()`           | Skips over the specified number of documents from the query results.                                                               | `db.posts.find().skip(2)`                   |
| `distinct()`       | Returns a list of distinct values for the given key across a collection.                                                           | `db.posts.distinct("author.name")`          |
| `countDocuments()` | Returns the count of documents that would match a find() query. (NOTE: count() is deprecated)                                      | `db.posts.countDocuments({ shared: true })` |

#### SORT
> By default, `db.posts.find({})` returns sorted records by `_id`
```js
// Simplest sorting ascending
db.posts.find().sort("title")
```

#### COMBINATION OF HELPER FUNCTIONS
```js
// Skip and sort
db.posts.find().skip(2).sort({shared: 1})
```

### AGGREGATION FRAMEWORK
```js
// Simple example
db.posts.aggregate([{$group: {_id: "$author.nickname"}}])
// Make sure you have this ---------^
// [ { _id: 'mikef' }, { _id: 'emily23' }, { _id: 'bob1995' } ]
```

#### AGGREGATION OPERATOR
| Operator   | Description                                                                                                                                                                            | Example                                                           |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `$match`   | Filters the documents to pass only documents that match the specified condition(s) to the next pipeline stage.                                                                         | `db.posts.aggregate([{$match: {shared: true}}])`                  |
| `$group`   | Groups input documents by the specified `_id` expression and for each distinct grouping, outputs a document.                                                                           | `db.posts.aggregate([{$group: {_id: "$author.nickname"}}])`       |
| `$sort`    | Reorders the document stream by a specified sort key. Only the order changes; the documents remain unmodified.                                                                         | `db.posts.aggregate([{$sort: {comments: -1}}])`                   |
| `$limit`   | Passes the first "n" documents unmodified to the pipeline where "n" is the specified limit. For each input document, outputs either one document (unchanged) or zero documents.        | `db.posts.aggregate([{$limit: 5}])`                               |
| `$skip`    | Skips the first "n" documents where "n" is the specified skip number and passes the remaining documents unmodified to the pipeline.                                                    | `db.posts.aggregate([{$skip: 5}])`                                |
| `$unwind`  | Deconstructs an array field from the input documents to output a document for each element. Each output document replaces the array with an element value.                             | `db.posts.aggregate([{$unwind: "$tags"}])`                        |
| `$project` | Passes along the documents with the requested fields to the next stage in the pipeline. The specified fields can be existing fields from the input documents or newly computed fields. | `db.posts.aggregate([{$project: {_id: 0, title: 1, author: 1}}])` |

##### UNWIND
> Desconstruct array into a single value
```js
db.posts.aggregate({$unwind: "$tags"})
```
> Output
```json
{
  tags: ["abc", "def"]
}
// To
{
  tags: "abc"
}
```

##### UNDO UNWIND
> Not technically undo but this reconstruct the data back into the array
```js
db.posts.aggregate([
  { $unwind: "$tags" },
  { $group: { _id: "$_id", tags: { $push: "$tags" } } }
])
```

### USING A LIST OF IDS TO DO THE QUERY IN A DATABASE
[Reference](https://www.tutorialspoint.com/how-to-find-through-list-of-ids-in-mongodb)
```js
var listOfIds = ['5c8ecae42f684a30fbdfd576', '5c8ecaf82f684a30fbdfd578'];
var documentIds = listOfIds.map(function(myId) { return ObjectId(myId); });
db.getCollection('postCollection').find({_id: {$in: documentIds }})
```

## MONGO UTILITIES
### EXPORT DATA
```js
// Export all databases
mongodump

// Export certain database
mongodump --db forum --collection posts

// A folder named dump will be created along with their bson
// To view the bson content:
hexdump ./dump/forum/posts.bson
hexdump -C ./dump/forum/posts.bson

// Export certain data
mongoexport -d forum -c posts -o posts.txt

```

### IMPORT DATA
```js
// Import database
mongorestore ./dump

// Import certain data
mongoimport --db forum --collection posts --file posts.txt

```

## REPLICA SET
A MongoDB Replica Set is a group of MongoDB servers that maintain the same data set. It provides redundancy and high availability, and is the basis for all production deployments. Here's a simplified explanation:
- Multiple Servers: A production database isn't just one server. It's a group of servers, and this group is called a Replica Set.
- Primary and Secondary Servers: In a Replica Set, there's one primary server and the rest are secondary servers. You can only make changes (write operations) on the primary server.
- Data Replication: When you update a document on the primary server, this update is automatically copied (or "replicated") to all the secondary servers. This ensures all servers have the same data.
- Failover: If the primary server fails, the secondary servers choose a new primary server among themselves. This process is automatic.
- Read Operations: You can read data from any server, whether it's primary or secondary. This can help balance the load of read operations across multiple servers.
- Example with MongoDB Atlas: In a MongoDB Atlas cluster, you might see tags like "Primary" and "Secondary". This shows which server is the primary and which ones are secondaries in the Replica Set. If the primary server fails, one of the secondary servers will automatically become the new primary. All write operations happen on the primary server and are replicated to the secondary servers.

### SETTING UP REPLICA SET
[Reference](https://www.sohamkamani.com/docker/mongo-replica-set/)
```bash
##### Step 1: Creating a keyfile using openssl #####
openssl rand -base64 756 > <path-to-keyfile>

##### Step 2: Change the permission to the keyfile to be specified to 400 #####
chmod 400 <path-to-keyfile>
# NOTE: Some error might happen here where the permission is not updated if you are using Windows + WSL2
# To fix this problem, you have to crete a new configuration file using WSL
cd /etc
nano wsl.conf

# Paste the code below into the file and save it then restart your machine to apply th configuration completely
[automount]
options = "metadata"

# Save the key file into the ./script/mongodb.key
# Create a new file called script.sh into the ./script folder too
# The content of the script.sh:

#!/bin/bash
# `host.docker.internal` is only when you are initiating using Windows, and you are running from local machine to import the data
# use the hostname as stated in the docker compose file to replace the host.docker.internal
# docker exec m1 /scripts/setup.sh

mongosh <<EOF
    var cfg = {
        "_id": "rs0",
        "version": 1,
        "members": [
            {
                "_id": 0,
                "host": "host.docker.internal:27017"
            },
            {
                "_id": 1,
                "host": "host.docker.internal:27018"
            },
            {
                "_id": 2,
                "host": "host.docker.internal:27019"
            }
        ]
    };
    rs.initiate(cfg, { force: true });
    //rs.reconfig(cfg, { force: true });
    rs.status();
EOF
sleep 10

mongosh <<EOF
    db = db.getSiblingDB("admin");
    db.createUser(
    {
        user: "admin",
        pwd: "admin",
        roles: [ { role: "root", db: "admin" } ]
    });
    db.getSiblingDB("admin").auth("admin", "admin");
    db.createUser({
        user: "reader",
        pwd: "reader",
        roles: [ "readAnyDatabase" ]
    });
    rs.status();
EOF

##### Step 3: Create the docker compose yaml file #####
# https://prashix.medium.com/setup-mongodb-replicaset-with-authentication-enabled-using-docker-compose-5edd2ad46a90

version: "3.7"

# networks:
#   mongo-net:
#     name: mongo-net

services:
  m3:
    # hostname: m3
    container_name: m3
    image: mongo:5.0.9
    entrypoint: [ "mongod", "--keyFile", "/data/mongodb.key", "--replSet", "rs0", "--journal", "--bind_ip_all" ]
    ports:
    - "27019:27017"
    restart: unless-stopped
    # networks:
    #   - mongo-net
    volumes:
    - "./scripts/mongodb.key:/data/mongodb.key"

  m2:
    # hostname: m2
    container_name: m2
    image: mongo:5.0.9
    entrypoint: [ "mongod", "--keyFile", "/data/mongodb.key", "--replSet", "rs0", "--journal", "--bind_ip_all" ]
    ports:
    - "27018:27017"
    restart: unless-stopped
    # networks:
    #   - mongo-net
    volumes:
    - "./scripts/mongodb.key:/data/mongodb.key"

  m1:
    # hostname: m1
    container_name: m1
    image: mongo:5.0.9
    command: bash -c "mongod --keyFile /data/mongodb.key --replSet rs0 --journal --bind_ip_all"
    ports:
    - "27017:27017"
    # links:
    # - m3:m3
    # - m2:m2
    restart: unless-stopped
    # networks:
    #   - mongo-net
    volumes:
    - "./scripts/setup.sh:/scripts/setup.sh"
    - "./scripts/mongodb.key:/data/mongodb.key"
    depends_on:
    - m3
    - m2

##### Step 4: Run #####
# To run, cd to the current directory and type
docker compose up -d

##### Step 5: Open a new terminal and run the script file internally #####
docker exec m1 /scripts/setup.sh

```