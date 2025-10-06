names = []

with open("dados/names.txt", "r", encoding="utf-8") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names): # Parametro 'reverse=True' coloca como ordem decrescente do último ao primeiro
    print(f"Olá, {name}")
    