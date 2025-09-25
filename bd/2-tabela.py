import sqlite3

# 1 - Conectando no banco de dados
conexao = sqlite3.connect('titulo.db')

# 2 - Criando a variável CURSOR (necessária para realizar operações no banco)
cursor = conexao.cursor()

# 3 - Criando a Tabela 'filmes' utilizando o cursor
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """
)

print("Tabela Criada")