from pymongo import MongoClient

client = MongoClient()
mydb = client.dbposts
mycollection = mydb.posts

result = mycollection.find({})

# print(result)       # Trás a instância do fetch como Objeto
# print(vars(result)) # NÃO trás os dados do objeto, trás essas informações: {'_collection': Collection(Database(MongoClient(host=['localhost:27017'],  
#                       document_class=dict.... 
#                     # São úteis para verificação de atributos da consulta

## Necessário iterar para recuperar os valores, não possui um fetchAll() da vida
for item in result:
    print(item)
client.close()

