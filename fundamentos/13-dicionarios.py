filmInception = {
    "title": "Inception",
    "yearRelease": 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-fi", "Action", "Thriller"]
}

print(filmInception)
print(len(filmInception))
print(type(filmInception))

# 1 - Recuperação de dados em um dicionário
print(filmInception["title"])
print(filmInception.get("title"))

# 2 - Buscar apenas as chaves do dicionário
print(filmInception.keys())

# 3 - Buscar apenas os valores do dicionário
print(filmInception.values())

# 4 - Buscar as chaves e valores com retorno em tupla
print(filmInception.items())

# 5 - Adicionar/Atualizar itens no dicinário
filmInception.update({"director" : "Christopher Nolan"})
filmInception["director"] = "Christopher Nollan"
print(filmInception)

# 6 - Atualizar valores no dicionário
filmInception.update({"imdbRating" : 8.7})

# 7 - Remover itens do dicionario
filmInception.pop("director")
print(filmInception)