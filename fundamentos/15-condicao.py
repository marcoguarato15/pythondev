# name = input("Digite o nome do filme:")

# yearRelease = int(input("Digite o ano de lançamento:"))

# rating = float(input("Digite a nota de avaliação do filme:"))

# # Verifica se o filme é recomendável

# if (rating > 8.0):
#     if yearRelease > 2015:    
#         print(f"Recomendo o filme {name}. Ele é muito bom")
#     else:
#         print("O filme ainda não é recomendável pois é muito antigo...")
# else:
#     print("O filme ainda não atingiu uma nota boa...")

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

operacao = input("Informe a operação (+ - * /):")

if (operacao == "+"):
    result = num1 + num2
elif (operacao == "-"):
    result = num1 - num2
elif (operacao == "*"):
    result = num1 - num2
elif (operacao == "/"):
    if (num2 != 0):
        result = num1 - num2
    else:
        print("Erro: divisão por 0!")
        result = "Erro"
else:
    print("Operação inválida!")
    result = "Erro"

if(type(result) == float):
    print(f"Resultado: {result:.2f}")
else:
        print(f"Resultado: {result}")