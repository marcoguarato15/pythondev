cursos = []

with open("dados/cursos.csv", "r", encoding="utf=8") as file:
    for line in file:
        # linha = line.strip().split(',')
        # print(linha[0], linha[1])
        linguagem,categoria = line.strip().split(",")
        cursos.append(f"{linguagem}-{categoria}")

# Ordenar por linguagem
for curso in sorted(cursos):
    print(curso)
print()
# Ordenar por categoria
for curso in sorted(cursos, key=lambda x: x.split('-')[1]):
    print(curso)