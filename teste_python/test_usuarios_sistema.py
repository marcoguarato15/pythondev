import pytest
import sqlite3
from usuarios_sistema import adicionar_usuario, buscar_usuario_email

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

@pytest.mark.parametrize(
    "id, nome, email, esperado_nome",
    [
        (1, "Alice", "alice@example.com", "Alice"),
        (2, "Bob", "bob@example.com", "Bob"),
        (3, "Charlie", "charlie@example.com", "Charlie")
    ]
)
@pytest.mark.unit
def test_adicionar_usuario(db_connection, id, nome, email, esperado_nome):
    conn, cursor = db_connection

    adicionar_usuario(cursor, id, nome, email)
    resultado = buscar_usuario_email(cursor, email)

    assert resultado is not None
    assert resultado[1] == esperado_nome
    assert resultado[2] == email


@pytest.mark.integration
def test_buscar_usuario_email_inexistente(db_connection):
    conn, cursor = db_connection
    resultado = buscar_usuario_email(cursor, "nonexistent@example.com")
    assert resultado is None

# pytest -m "integration and slow"
@pytest.mark.integration
@pytest.mark.slow
def test_insercao_busca_lenta(db_connection):
    conn, cursor = db_connection
    import time
    for i in range(100):
        adicionar_usuario(cursor, i, f"Usuario{i}", f"usuario{i}@example.com")

    time.sleep(2)

    for i in range(100):
        resultado = buscar_usuario_email(cursor, f"usuario{i}@example.com")

        assert resultado is not None
        assert resultado[1] == f"Usuario{i}"
        assert resultado[2] == f"usuario{i}@example.com"