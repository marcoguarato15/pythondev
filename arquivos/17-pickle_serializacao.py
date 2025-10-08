import pickle

class Cliente:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def __str__(self):
        return f"{self.nome} - {self.idade} anos - {self.cidade}"
    
clientes = [
    Cliente("Ana", 25, "São Paulo"),
    Cliente("Carlos", 30, "Rio de Janeiro"),
    Cliente("Fernanda", 22, "Curitiba"),
]

## 1 - Salvar(serializar) lista de clientes em arquivo pickle
# wb - write binary
with open("dados/clientes.pkl", "wb") as file:
    pickle.dump(clientes, file)

# 2 - Lendo os dados(desseliazando) os dados pickle
with open("dados/clientes.pkl", "rb") as file:
    clientes_carregados = pickle.load(file)

# print(clientes_carregados) # trás a lista de objetos e não seu método str, necessário iterar
for cliente in clientes_carregados: 
    print(cliente) # aqui já trás o método __str__ de cada objeto

# 3 - Adicionando um novo cliente
novo_cliente = Cliente("Marcos", 28, "Uberaba")
clientes_carregados.append(novo_cliente)

with open("dados/clientes.pkl", "wb") as file:
    pickle.dump(clientes_carregados, file)

    
