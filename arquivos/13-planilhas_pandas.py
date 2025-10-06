import pandas as pd
import numpy as np

dados_aba1 = {
    "ID": [1, 2, 3, 4, 5],
    "Nome": ["Ana", "Carlos", "Lucas", "Fernanda", "Mariana"],
    "Idade": [23, 30, 25, 28, 22],
    "Cidade":["São Paulo", "Rio de Janeiro", "Curitiba", "Porto Alegre", "Salvador"]
}

dados_aba2 = {
        "ID": [6, 7, 8, 9, 10],
    "Nome": ["Jõao", "Paula", "Pedro", "Amanda", "Rafael"],
    "Idade": [27, 35, 32, 22 ,29],
    "Cidade":["Fortaleza", "Belo Horizonte", "Recife", "Brasília", "Manaus"]
}

dados_aba3 = {
    "ID": [11, 12, 13, 14, 15],
    "Nome": ["Juliana", "Sérgio", "Gabriela", "Eduardo", "Carla"],
    "Idade": [26, 33, 28, 31, 24],
    "Cidade":["Natal", "Cuiabá", "Vitória", "Maceió", "Jõao Pessoa"]
}

dados_aba4 = {
    "ID": [16, 17, 18, 19, 20],
    "Nome": ["Ricardo", "Tânia", "Elena", "Marcos", "Beatriz"],
    "Idade": [29, 26, 34, 27, 25],
    "Cidade":["Florianópolis", "Gôiania", "Aracaju", "Campo Grande", "Belém"]
}

df_aba1 = pd.DataFrame(dados_aba1)
df_aba2 = pd.DataFrame(dados_aba2)
df_aba3 = pd.DataFrame(dados_aba3)
df_aba4 = pd.DataFrame(dados_aba4)

caminho_arquivo = "dados/clientes.xlsx"

with pd.ExcelWriter(caminho_arquivo, engine="openpyxl") as writer:
    df_aba1.to_excel(writer, sheet_name="Aba1", index=False)
    df_aba2.to_excel(writer, sheet_name="Aba2", index=False)
    df_aba3.to_excel(writer, sheet_name="Aba3", index=False)
    df_aba4.to_excel(writer, sheet_name="Aba4", index=False)

print(f"Arquivo excel com 4 abas criado em '{caminho_arquivo}'")