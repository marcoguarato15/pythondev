cursos = []

with open("dados/cursos.csv", "r", encoding="utf=8") as file:
    for line in file:
        # linha = line.strip().split(',')
        # print(linha[0], linha[1])
        linguagem,categoria = line.strip().split(",")
        curso = {}
        cursos += [{"Linguagem":linguagem,"Categoria":categoria}]
    cursos.pop(0)

print(cursos)