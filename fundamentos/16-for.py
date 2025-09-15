# Lista de filmes
filmsList = ["Mario", "Inception", "The Godfather", "Titanic"]

# 1 - Iterando valores de uma lista
for film in filmsList:
    print(film)

# 2 - parando a função caso a condição seja atendida
print("\n# Parando a função caso a condição seja atendida (if film == 'The Godfather'):")
for film in filmsList:
    if (film == "The Godfather"):
        break
    print(film)

# 3 - Pulando a iteração caso a condição seja atendida
print("\n# Pulando a iteração caso a condição seja atendida (if film == 'The Godfather'):")
for film in filmsList:
    if (film == "The Godfather"):
        continue
    print(film)

name = input("Informe o nome do filme: ")
ammountRatings = int(input("Informe quantas notas irá dar ao filme:"))

total = 0
for i in range(ammountRatings):
    rating = float(input("Informe a nota: "))
    total += rating

if total > 0:
    average = total / ammountRatings
    print(f"A média de avaliação do filme {name} é: {average}")
else:
    print("Filme ruim, nota 0!")
