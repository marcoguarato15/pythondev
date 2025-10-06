import glob, os, zipfile

# 1 - Pegando o diretorio atual
print(os.getcwd())

# 2 - Listar todos os arquivos txt
for file in glob.glob("dados/*.txt"):
    print(file)

# 3 - listar todos arquivos csv
for file in glob.glob("dados/*.csv"):
    print(file)

# 4 - Compactar arquivos .txt
with zipfile.ZipFile("dados/names.zip", "w") as zip:
    for file in glob.glob("dados/*.txt"):
        zip.write(file)

# 4 - Compactar todos arquivos
with zipfile.ZipFile("dados/code.zip", "w") as zip:
    for file in glob.glob("*", recursive=True):
        zip.write(file)
