with open("dados/cursos.csv", "r", encoding="utf=8") as file:
    for line in file:
        # linha = line.strip().split(',')
        # print(linha[0], linha[1])
        linguagem,categoria = line.strip().split(",")
        print(f"Linguagem: {linguagem}, Categoria: {categoria}")