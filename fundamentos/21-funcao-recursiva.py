## Recursividade

# 1 - Fatorial de um número

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

number = int(input("Informe o número para o fatorial: "))
print(f"O fatorial de {number} é {factorial(number)}")

# 2 - soma total de um número
def totalSum(num):
    if num == 1:
        return 1
    else:
        return num + totalSum(num - 1)
    
number = int(input("Informe o número para a soma total: "))
print(f"O fatorial de {number} é {totalSum(number)}")
