# Lista de filmes
filmsList = ["Mario", "Inception", "The Godfather", "Titanic"]

# 1 - Iteração de itens de uma lista com while
index = 0
while index < len(filmsList):
    print(filmsList[index])
    index += 1

# 2 - BREAK com while
index = 0
while index < len(filmsList):
    
    if filmsList[index] == "The Godfather":
        break
    
    print(filmsList[index])
    index += 1

# 3 - CONTINUE com while
index = 0
while index < len(filmsList):

    if filmsList[index] == "The Godfather":
        index += 1
        continue

    print(filmsList[index])
    index += 1

# 4 - Exemplo de avaliação com while
name = input("Informe o nome do filme: ")
ammountRatings = int(input("Informe quantas notas irá dar ao filme:"))

total = 0
count = 0

while count < ammountRatings:
    rating = float(input("Informe a nota: "))
    total += rating
    count += 1

if total > 0:
    average = total / ammountRatings
    print(f"A média de avaliação do filme {name} é: {average}")
else:
    print("Filme ruim, nota 0!")
