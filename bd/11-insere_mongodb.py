from pymongo import MongoClient
from pymongo import ASCENDING

client = MongoClient()
mydb = client.dbposts
mycollection = mydb.posts

mycollection.create_index([('author.email', ASCENDING)], unique=True) # Criando um índice único para email neste documento
mycollection.create_index([('author.name', ASCENDING)], unique=True)  # índice errado
print(mycollection.index_information())                               # mostrar indices /para acesso o 
                                                                      # nome do índice fica como author.name_1 ("author.name", 1)

# exclusão do indice unico errado:
mycollection.drop_index("author.name_1")

post1 = {
    "title": "FastAPI",
    "category": "Backend",
    "author": {
        "name": "Rodrigo",
        "email": "rodrigo@email.com"
    }
}

result = mycollection.insert_one(post1)
print(result.acknowledged) # Resultado em True/False se foi inserido com sucesso
if result.acknowledged:
    print("Documento inserido com sucesso")
else:
    print("Falha ao inserir documento")

client.close()