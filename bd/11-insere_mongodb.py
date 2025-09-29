from pymongo import MongoClient

client = MongoClient()
mydb = client.dbposts
mycollection = mydb.posts

post1 = {
    "title": "FastAPI",
    "category": "Backend",
    "author": {
        "name": "Rodrigo",
        "email": "rodrigo@email.com"
    }
}

result = mycollection.insert_one(post1)
# print(result.acknowledged) # Resultado em True/False se foi inserido com sucesso
if result.acknowledged:
    print("Documento inserido com sucesso")
else:
    print("Falha ao inserir documento")

client.close()