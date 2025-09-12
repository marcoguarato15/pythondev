# CONJUNTO MATEMÁTICO (possibilita a utilização de funções matemáticas, como joint, intersection, union... )
# remoção com pop(último) e remove(valor)
# NÃO POSSÚI ORDEM
# NÃO ACEITA DOIS VALORES IGUAIS

# Aceita apenas um 'Inception'
filmsSet1 = {1000 ,"Inception", "Inception", "The Shawshank Redemption", "The Dark Knight",
          "Pulp Fiction", "Interstellar"}

filmsSet2 = {"Interstellar"}

filmsSet3 = {"Madagasgar"}

print(type(filmsSet1))
print("Set: ", filmsSet1)

# 1 - Não permite marcações como strings e listas
# print("Marcações de inicio:fim:passo (filmsSet1[::-1]) -> inverso",filmsSet1[::-1])

# 2 - Remoção por valor passado
filmsSet1.remove("The Shawshank Redemption")
print("Remoção de um valor por parametro (filmsSet1.remove('The Shawshank Redemption')): ", filmsSet1)


# 3 - Inserção de valores (não adiciona se igual a valor interno)
filmsSet1.add("Top Gun")
print("Adição de valores com a função add() (filmsSet1.add('Top Gun')): ", filmsSet1)

# 4 - Funções matemáticas de conjunto
print("filmsSet1: ", filmsSet1)
print("filmsSet2: ", filmsSet2)
print("filmsSet3: ", filmsSet3)
print("isSubset filmsSet2.issubset(filmsSet1):", filmsSet2.issubset(filmsSet1))
print("Union (filmsSet1.union(filmsSet3)): ", filmsSet1.union(filmsSet3))
print("Difference (filmsSet1.difference(filmsSet2)): ", filmsSet1.difference(filmsSet2))

# 5 - Remoção de um valor aleatório(arbitrário) (como não possui indexação...)
popped = filmsSet1.pop() 
print("Remoção de um valor aleatório pela função pop() (filmsSet1.pop()): ",filmsSet1, popped)