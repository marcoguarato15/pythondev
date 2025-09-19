import pprint

pp = pprint.PrettyPrinter(depth = 4)
# 1 - função para mostrar uma mensagem
def welcome():
    print("Olá! Bem vindo ao sistema de filmes!")

welcome()

# for i in range(10):
#     welcome()

# 2 - função para calcular uma media de notas
def calculateAverage():
    quantity = int(input("Informe quantas notas dará ao filme: "))
    total = 0
    for i in range(quantity):
        nota = float(input("Informe a nota: "))
        total += nota

    if quantity != 0:
        average = total / quantity
    else:
        print("Erro: divisão por zero")
        average = 0
        
    return average

print(f"A média de notas é: {calculateAverage():.2f}")

# 3 - função para cadastrar um filme
movieDict = {
    "Movie1" : {"id" : 0,
        "name" : "Mario",
        "releaseYear" : 2023,
        "imdbRating" : 8.0,
        "price" : 70.0}
}

def register():
    name = input("Nome do filme: ")
    releaseYear = int(input("Ano de lançamento: "))
    imdbRating = float(input("Nota do filme: "))
    price = float(input("Preço do filme: "))

    print(f"O filme {name} de {releaseYear} é R${price:.2f} e tem a nota de {imdbRating:.2f} ")
    index = len(movieDict)
    movieDict.update({
        "Movie2" : {"id" : index,
        "name" : name,
        "releaseYear" : releaseYear,
        "imdbRating" : imdbRating,
        "price" : price}
        })


register()


pp.pprint(movieDict)