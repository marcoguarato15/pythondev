from pymongo import MongoClient

client = MongoClient()
mydb = client.dbposts
mycollections = mydb["posts"]

# filter
old_value = {"level" : "Intermediario"}
# update
new_value = {"$set": {"level":"Iniciante"}}

# acha o primeiro e o altera (filter, update)
mycollections.update_one(old_value, new_value)

result = mycollections.find()

for p in result:
    print(p)