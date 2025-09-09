num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

## Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
#resto da divisão
mod = num1 % num2
#exponenciação
exp = num1 ** num2

print("Exponenciação: ",exp)
print(f"Resto da divisão de {num1} por {num2} é: {mod}")

## Comparação (retorna bool True/False)

bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
biggerEqual = num1 >= num2
smallerEqual = num1 <= num2

print(f"O numero {num1} é menor ou igual ao {num2}?: {smallerEqual}")
print(f"O numero {num1} é maior ou igual ao {num2}?: {biggerEqual}")
print(f"O numero {num1} é igual ao {num2}?: {equal}")

## Atribuição

# num1 = num1 + 2
num1 += 2
#num1 = num1 - 2 
num1 -= 2
#num1 = num1 * 2
num1 *= 2
#num1 = num1 / 2
num1 /= 2
#num1 = num 1 ** 2
num1 **= 2
print(f'Exponenciação atribuindo o valor ao num1 (num1 **= 2) e alterando seu valor interno, mostrando num1: {num1}')
#num1 = num1 %= 2
num1 %= 2
print(f'Modulação atribuindo o valor ao num1 (num1 %= 2) e alterando seu valor interno, mostrando num1: {num1}')