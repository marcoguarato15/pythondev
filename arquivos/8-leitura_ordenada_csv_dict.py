cursos = []

with open("dados/cursos.csv", "r", encoding="utf=8") as file:
    for line in file:
        # linha = line.strip().split(',')
        # print(linha[0], linha[1])
        linguagem,categoria = line.strip().split(",")
        curso = {}
        cursos += [{"Linguagem":linguagem,"Categoria":categoria}]
    cursos.pop(0)

## Ordenação por operações lambda
# for curso in sorted(cursos, key= lambda x: x["Linguagem"]):
#     print(curso)

# for curso in sorted(cursos, key= lambda x: x["Categoria"]):
#     print(curso)

## Ordenação por operações de funções
def get_language(courses):
    return courses["Linguagem"]

def get_category(courses):
    return courses["Categoria"]

for curso in sorted(cursos, key= get_language):
    print(curso)
print()
for curso in sorted(cursos, key= get_category):
    print(curso)