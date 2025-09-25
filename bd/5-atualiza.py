import sqlite3

## 1 - Conectando e criando o CURSOR
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

## 2 - Atualizando Filme com id_filme 1
id_filme = 1

cursor.execute(

    """
        UPDATE filmes SET nome = ?, nota = ?, ano = ?
        WHERE id = ?
    """,
    ("Homem Aranha", 8.5, 2020, id_filme)
)

print("Sucesso ao atualizar dados")
conexao.commit()
conexao.close()

# Não é possivel verificar com esta biblioteca pois ele não retorna nada ao executar o commit() resultando em false sempre
# if conexao.commit():
#     print("Sucesso ao atualizar dados")
#     conexao.close()
# else:
#     print("Falha ao atualizar dados")
