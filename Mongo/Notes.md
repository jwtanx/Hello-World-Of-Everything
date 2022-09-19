# List of Mongo shell notes

## Getting into Mongo Shell
`mongosh`

## Authenticating the client
```
db = db.getSiblingDB("admin")
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