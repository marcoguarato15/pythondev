"""
    *args - Utilizamos o *args quando não sabemos quantos parâmetros queremos ter em uma função
    - Os argumentos são passados como uma tupla
"""

# 1 - Soma de números
def sumNumbers(*args):
    sumTotal = 0
    for n in args:
        sumTotal += n
    print(f"A soma total é {sumTotal}")

sumNumbers()
sumNumbers(11)
sumNumbers(1,5,4,10,3,7,2,1)

"""
    **kwargs - Além dos valores podemos passar também as respectivas chaves para cada argumento
    - Os argumentos são passados como um dicionário
"""

# 2 - Apresentação de cursos
def presentation(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} - {value}")

print("Lista de Cursos:")
print("------------------------------")
presentation(name="Python", category="backend", level="Inicianete")
presentation(name="C#", category="full-stack", level="Intermediário")
presentation(name="Javascript", category="front-end", level="Inicianete")
