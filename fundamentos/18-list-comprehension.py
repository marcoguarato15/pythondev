# Lista com 10 numeros que sejam menores que 6
numList = [num for num in range(10) if num < 6]
print(numList)

# Lista de filmes
filmsList = ["Mario", "Mario Cart", "Inception", "The Godfather", "Gran Turism", "Titanic"]

# filmes com a letra 'g' no Título
moviesWithG = [movie for movie in filmsList if 'g' in movie.lower()]
print("Filmes com a letra 'g' no título",moviesWithG)

# filmes que assisti
moviesWatched = [movie for movie in filmsList if movie not in ["Gran Turism", "Titanic", "Mario"]]
print(f"Assisti ao(s) filme(s): {moviesWatched}")


while True:

    movieName = input("Digite o nome do filme ou 'sair' para encerrar: ")
    if movieName == "sair":
        break
    else:
        foundMovies = [movie for movie in filmsList if movieName.lower() in movie.lower()]
        if foundMovies:
            print(f"Filmes que assisti: {foundMovies}")
        else:
            print("Nenhum filme encontrado procure novamente!")