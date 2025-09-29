from pymongo import MongoClient

client = MongoClient()
mydb = client.dbposts
mycollections = mydb["posts"]

myquery = {"category": "Backend"}

x = mycollections.delete_one(myquery)
print(f"Informações do delete: {x}")
# Irá deletar apenas o primeiro objeto encontrado como é delete_one...
# mesmo sem objetos ele retorna 'acknowledged=True' pois é bem sucedida mas sem valores excluídos...
print(f"Número de exclusões: {x.deleted_count}")

client.close()