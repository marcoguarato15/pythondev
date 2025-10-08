import json

dados = {
    "clientes":[
        {"id":1, "nome": "Ana", "idade": 25, "cidade": "São Paulo"},
        {"id":2, "nome": "Carlos", "idade": 30, "cidade": "Rio de Janeiro"},
        {"id":3, "nome": "Fernanda", "idade": 22, "cidade": "Curitiba"},
        {"id":4, "nome": "Jõao", "idade": 35, "cidade": "Belo Horizonte"}
    ]
}

caminho_arquivo = 'dados/clientes.json'

# 1 - Escrevendo dados em um arquivo JSON
with open(caminho_arquivo, "w", encoding="utf-8") as file:
    json.dump(dados, file, indent=4)

# 2 - Lendo dados de um arquivo JSON
with open(caminho_arquivo, "r", encoding="utf-8") as file:
    dados_lidos = json.load(file)
    print(dados_lidos)
    print(type(dados_lidos))

# 3 - Alterando dados dentro de um dicionário
for cliente in dados_lidos["clientes"]:
    if cliente["nome"] == "Carlos":
        cliente["idade"] = 20

# 4 - Criando um novo cliente para adicionar ao documento
novo_cliente = {"id":5, "nome": "Marco", "idade": 24, "cidade": "Uberaba"}

# 5 - Adicionando o novo cliente ao dicionário que será salvo no documento
dados_lidos["clientes"].append(novo_cliente)

# 6 - Salvando os novos dados sobrescrevendo os que estavam no arquivo JSON (utilizando "w")
with open(caminho_arquivo, "w", encoding="utf-8") as file:
    json.dump(dados_lidos, file, indent=4)
