# Utilizando o input (retorna apenas str)

name = input("Informe o nome do filme: ")

# casting para integer
releaseYear = int(input("Informe o ano de lançamento: ")) 

#casting para float
movieRating = float(input("Informe a nota do filme: "))

aprovedMovie = bool(input("Informe se o filme foi aprovado: "))

tipoName =  str(type(name)) 
tipoReleaseYear = str(type(releaseYear))
tipoMovieRating = str(type(movieRating))
tipoAprovedMovie = str(type(aprovedMovie))

print(tipoName)
print(tipoReleaseYear)
print(tipoMovieRating)
print(tipoAprovedMovie)

# soma de strings (concatenação errada não aceita outros tipos sem ser string)
print("\nNome do filme: " + name + " / tipo: " + tipoName + "\nData de lançamento: " + \
        str(releaseYear)  +  " / tipo: " + tipoReleaseYear + "\nNota: " + str(movieRating) + \
        " / tipo: " + tipoMovieRating + "\nAprovado: " + str(aprovedMovie) + " / tipo: " + tipoAprovedMovie)

# concatenação básica
print("\n\nNome do Filme: ", name, "\nAno de Lançamento: ", releaseYear, "\nNota do Filme: ", movieRating, \
      "\nFilme aprovado: ", aprovedMovie)

# f string
print(f"\n\nNome do Filme: {name}\nAno de lançamento: {releaseYear}\nNota do filme: {movieRating}\n"
      f"Filme aprovado: {aprovedMovie}")