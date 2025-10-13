## Conexão ao bd com psycopg
import psycopg2 as ps
from conn_post_psycopg import conn
## Exemplo de conexão com o banco
# import psycopg2 as ps
# var = ps.connect(
#     database = "DB_NAME",
#     user = "DB_USER",
#     password = "DB_PASSWORD",     
#     host = "DB_HOST",             # localhost/IP
#     port = "DB_PORT"              # 5432 (default)
# )

## 1 - Inserindo dados

games = [
    ("Valor Aleatorio", 2020, 8.0),
    ("Teste", 2016, 7.0)
]

## Cria varios cursores e os executa após sua criação
cursor = conn.cursor()
for game in games:
    cursor.execute( # %d e %f não funcionam não sei por que.... assim %s converte todos em string e o próprio 
                    # pgsql converte depois para inteiro e float...
        """
            INSERT INTO games (name, year, score)
            VALUES (%s, %s, %s) 
        """,
        game
    )
print("Dados inseridos com sucesso")
conn.commit()
