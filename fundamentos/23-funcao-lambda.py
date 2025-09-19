# 1 - Função que da a potência ao quadrado de um número
power = lambda num: num ** 2

print(power(5)) # -> 25

# 2 - Função que verifica se um número é par
isEven = lambda x: x % 2 == 0

if isEven(25):
    print("Numero é par")
else:
    print("Número é impar")

# 3 - Função que divide um número por outro
division = lambda x, y: x / y

print(division(25, 5))

# 4 - Função que inverte uma string
reverseString = lambda s: s[::-1]

print(reverseString("Python"))
print(reverseString("Javascript"))

moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "The Matrix"]
ratings = {
    "Titanic" : [8.5, 9.0, 7.5],
    "The Godfather" : [9.5, 9.8, 8.0],
    "Inception" : [8.0, 7.0, 8.5],
    "Jurassic Park" : [7.5, 7.0, 8.0],
    "The Matrix" : [8.8, 9.2, 8.0]
}

# 5 - Função para calcular a média de avaliações
average_rating = lambda movieName: sum(ratings[movieName]) / len(ratings[movieName])

print(f"A média do filme Titanic é {average_rating("Titanic"):.2f}")

# 6 - Função que verifica se um filme está na lista
checkMovie = lambda movieName: movieName in moviesList

print(f"O filme 'Inception' está na lista? {checkMovie("Inception")}")

# 7 - Função que retorna uma string recomendando o filme passado como parâmetro
recommendMovie = lambda movieName: f"Recomendo o filme {movieName} com a média de {average_rating(movieName):.2f}"

print(f"{recommendMovie("The Matrix")}")