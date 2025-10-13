import pytest
import sqlite3

@pytest.fixture
def db_connection():

    ## SETUP
    """
    Fixtre que configura uma conexão com um banco de dados SQLite em memória
    temporário e garante a limpeza dos recursos após o teste
    """
    conn = sqlite3.connect(":memory:") # diz que o banco de dados fica na memória
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE users(
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """
    )
    conn.commit()
    yield conn, cursor

    ## TEARDOWN
    conn.close()

def test_database_insert(db_connection):
    """
    Testa a inserção de um usuário na tabela users do BD SQLite
    """
    conn, cursor = db_connection
    cursor.execute(
        """
        INSERT INTO users (nome, email)
        VALUES (?, ?)
        """, ("John Doe", "john.doe@example.com")
    )
    conn.commit()

    # Verificação da inserção
    cursor.execute(
        """
        SELECT * FROM users WHERE email = ?
        """, ("john.doe@example.com",)
    )
    user = cursor.fetchone()
    assert user is not None
    assert user[1] == "John Doe"
    assert user[2] == "john.doe@example.com"


def test_duplicate_email_entry(db_connection):
    conn, cursor = db_connection
    cursor.execute(
        """
        INSERT INTO users (nome, email)
        VALUES (?, ?)
        """, ("John Doe", "john.doe@example.com")
    )
    conn.commit()

    # Realiza o teste de inserção com email duplicado, se der erro ele passa pelo teste
    # Se alterarmos o email ele falha -> FAILED test_database.py::test_duplicate_email_entry - Failed: DID NOT RAISE <class 'sqlite3.IntegrityError'>
    with pytest.raises(sqlite3.IntegrityError):
        conn, cursor = db_connection
        cursor.execute(
            """
            INSERT INTO users (nome, email)
            VALUES (?, ?)
            """, ("John Doe", "john.doe@example.com")
        )
        conn.commit()