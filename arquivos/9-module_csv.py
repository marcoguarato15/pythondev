import csv

cursos = []

with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for linha in reader:
        # print(linha)
        cursos.append(
            {"Linguagem":linha['language'], "Categoria":linha["category"]}
        )
    # Não é necessário colocar cursos.pop(0) pois o csv já descarta a linha de título

print(cursos)