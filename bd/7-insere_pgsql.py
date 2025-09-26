## Conexão ao bd com psycopg
import psycopg2 as ps
from conn_post_psycopg import conn
## Exemplo de conexão com o banco
# var = ps.connect(
#     database = "DB_NAME",
#     user = "DB_USER",
#     password = "DB_PASSWORD",     
#     host = "DB_HOST",             # localhost/IP
#     port = "DB_PORT"              # 5432 (default)
# )

## 1 - Inserindo dados

games = [
    ("Star Wars Survivor", 2023, 9.0),
    ("Luigis Mission 3", 2019, 9.0)
]

## Cria varios cursores e os executa após sua criação
cursor = conn.cursor()
for game in games:
    cursor.execute(
        """
            INSERT INTO games (name, year, score)
            VALUES (%s, %s, %s)
        """,
        game
    )
print("Dados inseridos com sucesso")
conn.commit()
