#REGEX
import re

text = "Udemy - uma plataforma com muitos cursos"

## 1 - indice inicial e final de palavras
# O 'r' significa uma raw string (string bruta)
match = re.search(r'muitos cursos', text)
print(f"Match é: {match}")
print(f"Indice inicial: {match.start()}")
print(f"Indice final: {match.end()}")

## 2 - Encontrar um índice específico em uma string
site = "https://udemy.com"
match = re.search(r'\.', site)
print("Obj regex(re)", match)

## 3 - Encontrar uma lista de caracteres dado um padrão
pattern = '[a-m]' # a até m
result = re.findall(pattern, text)
print(f"Dado o padrão [a-m] no texto: '{text}', o resultado do re.findall() é: {result}")

## 4 - Verificando se a string começa com a regra dada
rule = r'^A' # regra = começa com 'A' maiúsculo
phrases1 = ['A casa está limpa', 'O dia está lindo', 'Vamos passear', 'A casa está organizada']
for f in phrases1:
    print(10 * '-')
    print(re.match(rule, f))
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")
    print(10 * '-')

## 5 - Verificando se a string termina com um valor (regra)
rule2 = r'.*!$' # regra = termina com ponto de exclamação
phrases2 = ["O dia está lindo!", "Você está bem?", "Continue com a massagem por favor!"]
for p in phrases2:
    print(10 * '-')
    print(re.match(rule2, p))
    if re.match(rule2, p):
        print(f"Combina: {p}")
    else:
        print(f"não combina: {p}")
    print(10 * '-')

re.match