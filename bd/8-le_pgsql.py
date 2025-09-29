from conn_post_psycopg import conn

cursor = conn.cursor()

cursor.execute("SELECT * FROM games")

result = cursor.fetchall()

print(result)