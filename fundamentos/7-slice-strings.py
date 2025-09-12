movieName = "Top Gun"

## string[inicio:fim] - índice começa na posição 0 / índice final -1

# 1 - Buscar toda string a partir da primeira posição
print(movieName[0:])

# 2 - Buscar toda string até a última posição
print(movieName[:6])    # total de 7 caracteres, colocando 6  (0 até 6 = 7) ele corta o último
print(movieName[:-1])   # corta o último caractere
print(f'Correto: {movieName[:7]}')

# 3 - Buscar toda string a partir do 3 caractere
print(movieName[2:])

"""
    Com incremento
    string[inicio:fim:passo]
    passo - determina o incremento. Por padrão é 1
"""
# 4 - Buscar toda string de 2 em 2 caracteres
print(movieName[::2])

# 5 - Buscando toda string mas os indices impares
print(movieName[1::2])

# 6 - Iverter a string
print(movieName[::-1])