# 1 - Função para imprimir um nome completo
def fullName (firstName, lastName):
    print(f"Nome: {firstName} {lastName}")

fullName("Marco", "Antonio")

# 2 - Função para somar dois numeros
def sumNumbers(a, b):
    return a + b

soma = sumNumbers(10, 20)
print(soma)

# 3 - Função com parâmetro default
def whereLive(country = "Brasil"):
    print(f"Moro no país: {country}")

whereLive()
whereLive("Argentina")

# 4 - Função para dar notas a um filme
def rate_movie(quantityOfRatings, movieName):
    total = 0
    for i in range(quantityOfRatings):
        grade = float(input("Informe a nota do filme: "))
        total += grade
    
    if total >= 0:
        average = total / quantityOfRatings
    else:
        average = 0
    
    return average,movieName

avgRate = list(rate_movie(2, "Sonic")) # Retorna em um tupla

if avgRate == 0:
    print("Filme não foi avaliado...")
else:
    print(f"A média de avaliações do filme {avgRate[1]} é: {avgRate[0]}")