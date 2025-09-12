filmsList = ["Inception", "The Shawshank Redemption", "The Dark Knight",
          "Pulp Fiction", "Interstellar"]

print("Lista de filmes:", filmsList)

# 1 - tamanho da lista
print("Tamanho com a função len():", len(filmsList))

# 2 - Recuperar o indice do item pelo valor do item
print("Índice do item 'Interstellar' (pela função index()):",filmsList.index("Interstellar"))

# 3 - Adicionar item a lista (no final)
filmsList.append("The Lord of the Rings")
print("Adicionando um item na lista com a função append()", filmsList)

# 4 - Ordenar a lista
filmsList.sort()
print("Lista ordenada pela função sort():", filmsList)

# 5 - Copiar os itens de uma lista para outra
filmsCopy = filmsList[1:4].copy()
print("Copia da lista com a função copy() (filmsList[1:4].copy())", filmsCopy)

# 6 - Remoção de todos itens da lista
filmsCopy.clear()
print("Remoção de todos itens com a função clear():", filmsCopy)

# 7 - Remoção de itens pelo nome (Aceita apenas um valor)
filmsList.remove("Interstellar")
print("Remoção de itens pelo nome com a função remove() (filmsList.remove('Interstellar'))", filmsList)