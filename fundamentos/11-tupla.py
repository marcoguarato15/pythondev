# ! Tuplas são objetos imutáveis !
# NÃO É POSSIVEL REMOVER ITENS DE TUPLAS
filmsTuple = ("Inception", "The Shawshank Redemption", "The Dark Knight",
          "Pulp Fiction", "Interstellar")

print(type(filmsTuple))

## Também funcionam como strings e listas no quesito de marcação [::]

# Mostrar o último valor da tupla
print(filmsTuple[-1])

# Mostrar a quantidade de itens da tupla
print(len(filmsTuple))

# É possivel fazer um casting de tupla para listas

filmsList = list(filmsTuple)
print(type(filmsList), '\n' ,filmsList)

# Ele recria a tupla com esses novos valores, não remove o ultimo filme
filmsTuple = ("Inception", "The Shawshank Redemption", "The Dark Knight",
          "Pulp Fiction")
print(filmsTuple)