"""
Arquivos - Modos de operação

1-> Modo W - write (escrita)(sobrescreve os dados)
2-> Modo A - append (sempre no final)
3-> Moro R - read (leitura)
"""

with open("dados/names.txt", "r", encoding="utf-8") as file:
    # print(file.read())
    for line in file:
        # print(f"Olá, {line}") # A quebra de linha continua sendo lida
        # print(f"Olá, {line.rstrip()}") # Remove apenas os espaços em branco (quebra de linha inclusa) à direita
        print(f"Olá, {line.strip()}") # Remove todos espaços em branco a direita e a esquerda removendo a quebra de linha
        