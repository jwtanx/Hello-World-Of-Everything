# List of Mongo shell notes

## Getting into Mongo Shell
`mongosh`

## Authenticating the client
```
db = db.getSiblingDB("admin") # Or you can just `use admin`
db.auth(<username>, <password>)
```
Example: `db.auth("admin", "admin")`

## ASCENDING SORTING DATE
[Reference](https://stackoverflow.com/questions/13847766/how-to-sort-a-collection-by-date-in-mongodb)
`db.getCollection('postCollection').find().sort({updatetime: 1})`

## DESCENDING SORTING
`db.getCollection('postCollection').find().sort({updatetime: -1})`

## USING A LIST OF IDS TO DO THE QUERY IN A DATABASE
[Reference](https://www.tutorialspoint.com/how-to-find-through-list-of-ids-in-mongodb)
```js
var listOfIds = ['5c8ecae42f684a30fbdfd576', '5c8ecaf82f684a30fbdfd578'];
var documentIds = listOfIds.map(function(myId) { return ObjectId(myId); });
db.getCollection('postCollection').find({_id: {$in: documentIds }})
```

## SETTING UP REPLICA SET
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