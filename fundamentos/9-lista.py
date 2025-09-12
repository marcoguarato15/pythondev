filmMatrix = ["Matrix", 1999, 8.8, True]
print(type(filmMatrix))
print(filmMatrix)

filmsList = ["Inception", "The Shawshank Redemption", "The Dark Knight",
          "Pulp Fiction", "Interstellar"]

print("Lista de filmes: ",filmsList)

# 1 - Buscar os dois primeiros itens da lista
print("2 primeiros [:2]",filmsList[: 2])

# 2 - Buscar o último item da lista (retorna do tipo da variável quando é apenas um item e não uma lista)
print("Ultimo item: ", type(filmsList[-1]))

# 3 - Buscar filmes até uma determinada posição
print("Até uma posição, EX três primeiros([:3] -> 0, 1, 2)", filmsList[:3])

# 4 - Buscar filmes de uma posição específica
print("Filmes de uma posição específica, Ex 1 ao 3[1:4]", filmsList[1:4])