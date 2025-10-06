name = input("Digite o nome do aluno: ")

"""
Arquivos - Modos de operação

1-> Modo W - write (escrita)(sobrescreve os dados)
2-> Modo A - append (sempre no final)
3-> Moro R - read (leitura)
"""

## Implementação 1 - sobrescreve os dados com o 'w'
# file = open("dados/names.txt", "w")
# file.write(f"{name}\n")
# file.close()

## Implementação 1
# file = open("dados/names.txt", "a", encoding="utf-8")
# file.write(f"{name}\n")
# file.close()

# Implementação 2
with open("dados/names.txt", "a", encoding="utf-8") as file:
    file.write(f"{name}\n")