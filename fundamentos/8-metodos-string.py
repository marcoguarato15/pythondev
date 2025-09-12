movieName = "top Gun"

movieDescription = """    Top Gun, é um filme de aviação e aventura,
muito consagrado na indústria!
"""

print(movieName.upper()) # retona a string toda maiúscula
print(movieName.lower()) # retorna a string toda minúscula
print(movieName.capitalize()) # retorna a string com a primeira letra maiúscula, e deixa o resto em minúsculas
print(movieName.title()) # retorna a string com a primeira letra maiúscula
print(movieName.find("u")) # retorna o indice do caractere fornecido
print(movieDescription.count("t")) # se mais de um, retorna a quantidade de caracteres nessa string
print(movieName.replace("op", "teste")) # troca os caracteres fornecidos pelos informados em seguida
print(movieDescription.split(',')) # separa em um vetor as frases quebrando pelo valor fornecido removendo-o