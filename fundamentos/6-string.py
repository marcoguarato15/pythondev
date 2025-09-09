movieName1 = "Top Gun"
movieName2 = "top Gun"

print(movieName1 == movieName2) # Case Sensitive (False)

#strings multi linhas (Não são formatadas, pegam os enters e tabs e também os armazenam)
movieDescription = """    Top Gun é um filme de aviação e aventura
muito consagrado na indústria!
"""

print(movieName1)
# 1- Multiplicação de strings
line = "="
print(line *50)
print(movieDescription)

# 2- Procurar uma palavra dentro de uma string

print("top" in movieName2)
print("ação" in movieName2)