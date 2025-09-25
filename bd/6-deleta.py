import sqlite3

## 1 - Conectando e criando o CURSOR
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

## 2 - Deletando Filme com id 1 e 2
id = (1, 2)
cursor.execute(
    """
        DELETE FROM filmes
        WHERE ID in (?, ?)
    """,
    id
    )

conexao.commit()
conexao.close()

print("Dados excluídos com sucesso")