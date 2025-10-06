import csv

linguagem = input("Informe a linguagem de programação: ")
categoria = input("Informe a categoria da linguagem de programação: ")

with open("dados/cursos.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow([linguagem,categoria])

cursos = []

with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    cursos_reader = csv.DictReader(file)
    for linha in cursos_reader:
        cursos.append([{"Linguagem":linha["language"], "Categoria":linha["category"]}])
print(cursos)