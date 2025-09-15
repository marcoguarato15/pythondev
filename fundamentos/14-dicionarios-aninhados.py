import pprint

filmsDict = {
    "inception" : {
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-fi", "Action", "Thriller"]
    },
    "interstellar": {
        "yearRelease": 2010,
        "imdbRating": 8.6,
        "genre": ["Sci-fi", "Drama"]
    },
    "the dark knight": {
        "yearRelease": 2010,
        "imdbRating": 9.0,
        "genre": [ "Action", "Drama", "Crime"]
    }
}
# Melhor disposição de visualização de objetos(dicionários)
# Não aceita string no meio, apenas objetos -> (pp.pprint("teste", filmsDict)) não funciona
# aceita f strings mas não formata bonito pois adiciona em uma tupla
pp = pprint.PrettyPrinter(depth = 4)

# 1 - leitura de dados do dicionário
print("Dicionário completo: ")
pp.pprint(filmsDict)
print("\nGeneros:")
pp.pprint(filmsDict["inception"]["genre"])

# 2 - Adição de dados em um dicionário aninhado
filmsDict["inception"]["director"] = "Christopher Nolan"
print("\nAdição de director em inception:")
pp.pprint(filmsDict["inception"])

# 3 - remoção de dados em um dicionário
del filmsDict["the dark knight"]
print("\nRemoção do item 'the dark knight':")
pp.pprint(filmsDict)

nome1 = input("prod 1: ")
preco1 = float(input("preco 1: "))

nome2 = input("prod 2: ")
preco2 = float(input("preco 2: "))

nome3 = input("prod 3: ")
preco3 = float(input("preco 3: "))

nome1 = input("prod 1: ")
preco1 = float(input("preco 1: "))

nome2 = input("prod 2: ")
preco2 = float(input("preco 2: "))

nome3 = input("prod 3: ")
preco3 = float(input("preco 3: "))

nome1 = input("prod 1: ")
preco1 = float(input("preco 1: "))

nome2 = input("prod 2: ")
preco2 = float(input("preco 2: "))

nome3 = input("prod 3: ")
preco3 = float(input("preco 3: "))

# exercício de dicionário
dict = {
    nome1 : preco1,
    nome2 : preco2,
    nome3 : preco3
}

print(dict)
chaves = list(dict.keys())
print(chaves[0])
print( round((dict["Arroz"] + dict["Feijão"] + dict["Macarrão"]) / 3, 2))