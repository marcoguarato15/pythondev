import pandas as pd
import os
from pathlib import Path

# 1 - Importando dados de todas as Sheets
tb_clientes_dict = pd.read_excel("dados/clientes.xlsx", sheet_name=None)
print(tb_clientes_dict)
print(type(tb_clientes_dict))

# 2 - Criando a pasta 'planilhas_separadas' se não existis
pasta_saida = 'dados/planilhas_separadas'
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)
    print("Pasta planilhas_separadas criada com sucesso!")

# 3 - Separando as planilhas em diferentes arquivos
for nome_aba, tabela in tb_clientes_dict.items():
    caminho_arquivo = os.path.join(pasta_saida, f"{nome_aba}.xlsx")
    tabela.to_excel(caminho_arquivo, index=False)
print("Arquivos criados com sucesso")

# 4 - Criando a pasta 'planilhas_consolidadas' se não existis
pasta_consolidada = 'dados/planilhas_consolidadas'
if not os.path.exists(pasta_consolidada):
    os.makedirs(pasta_consolidada)
    print("Pasta planilhas_consolidadas criada com sucesso!")

# 5 - Caminho para arquivo
caminho_arquivo_consolidado = os.path.join(pasta_consolidada, "clientes.xlsx")

# 6 - Consolidar (juntas as planilhas sem juntar as abas)
with pd.ExcelWriter(caminho_arquivo_consolidado) as consolidada:
    for arquivo in Path(pasta_saida).glob("*.xlsx"):
        tabela = pd.read_excel(arquivo)
        # sheet_name=arquivo.stem(dá o próprio nome do arquivo lido 'Aba1, Aba2'...)
        tabela.to_excel(consolidada, sheet_name=arquivo.stem, index=False)