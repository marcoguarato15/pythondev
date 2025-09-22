import math

## 1 - Pegar o número de PI
print(math.pi)
print(f"{math.pi:.2f}")

## 2 - Pegar o número de Euler
print(math.e)
print(f"{math.e:.2f}")

## 3 - Arredondar o número para cima ou para baixo
num1 = 10.5
print(f"{math.ceil(num1)}") # Para cima
print(f"{math.floor(num1)}")# Para baixo

## 4 - Fatorial de um número
num2 = int(input("Informe um número para descobrir seu fatorial: "))
print(f"{math.factorial(num2)}")

## 5 - Potência de números
num3 = int(input("Informe um número para elevar: "))
num4 = int(input("Informe sua elevação: "))
print(f"{math.pow(num3, num4)}")

## 6 - Raiz quadrada de um número
num5 = int(input("Informe o número que quer descobrir a raiz quadrada: "))
print(f"Raiz quadrada de {num5}: {math.sqrt(num5):.2f}")

## 7 - MDC (maior divisor comum)
# gdc greater common divisor
print(math.gcd(20,100))
## Não é possivel passar uma lista/objeto é necessário passar individualmente os números separados por virgula
# quantidade = int(input("Informe a quantidade de números para o MDC: "))
# num6 = []
# for i in range(quantidade):
#     numero = int(input("Informe os números: "))
#     num6.append(numero)
# print(f"O MDC de {num6} é: {math.gcd(num6)}")

## 8 - Logarítmos
print(math.log(10)) # Base default é o número de euler -> log(x,base)