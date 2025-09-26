import sqlite3 as sq

# 1 - Conectar ao BD
def connect():
    conexao = sq.connect("titulo.db")
    return conexao

def addFilme(nome, ano, nota):
    conexao = connect()
    cursor = conexao.cursor()

    cursor.execute(
        """
            INSERT INTO filmes (nome, ano, nota)
            VALUES (?, ?, ?)
        """,
        (nome, ano, nota)
    )

    conexao.commit()
    conexao.close()
    return 1

def getFilmes():
    conexao = connect()
    cursor = conexao.cursor()

    dados = cursor.execute("SELECT * FROM filmes").fetchall()
    conexao.close()

    return dados

# Apenas um teste de remoção
def delFilme(id_filme):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute(
        """
            DELETE FROM filmes
            WHERE id = ?
        """,
        (id_filme,)
    )
    conexao.commit()
    conexao.close()

    return 1

# Apenas um teste de alteração
def updFilme(id, nome, ano, nota):



    conexao = connect()
    cursor = conexao.cursor()

    if len(nome) != 0 and ano != 1926 and nota != 0:
        cursor.execute(
            """
                UPDATE filmes SET nome = ?, ano = ?, nota = ?
                WHERE id = ?
            """,
            (nome, ano, nota, id)
        )
        pass
    elif len(nome) != 0 and ano != 1926:
        cursor.execute( 
            """
                UPDATE filmes SET nome = ?, ano = ?
                WHERE id = ?
            """,
            (nome, ano, id)
        )
        pass
    elif ano != 1926 and nota != 0:
        cursor.execute( 
            """
                UPDATE filmes SET ano = ?, nota = ?
                WHERE id = ?
            """,
            (ano, nota, id)
        )
        pass
    elif len(nome) != 0 and nota != 0:
        cursor.execute( 
            """
                UPDATE filmes SET nome = ?, nota = ?
                WHERE id = ?
            """,
            (nome, nota, id)
        )
        pass
    elif len(nome) != 0:
        cursor.execute( 
            """
                UPDATE filmes SET nome = ?
                WHERE id = ?
            """,
            (nome, id)
        )
        pass
    elif ano != 1926:
        cursor.execute( 
            """
                UPDATE filmes SET ano = ?
                WHERE id = ?
            """,
            (ano, id)
        )
        pass
    elif nota != 0:
        cursor.execute( 
            """
                UPDATE filmes SET nota = ?
                WHERE id = ?
            """,
            (nota, id)
        )
        pass
    else:
        conexao.close()
        return -1
    
    conexao.commit()
    conexao.close()
    return 1