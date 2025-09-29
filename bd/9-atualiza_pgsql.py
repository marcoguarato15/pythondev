from conn_post_psycopg import conn

cursor = conn.cursor()

values = ("League of Legends", 2010, 9.9, 1)

cursor.execute(
    """
        UPDATE games SET name = %s, year = %s, score = %s
        WHERE id = %s
    """,
    values
)

## OU

sql =   """
            UPDATE games SET name = %s, year = %s, score = %s
            WHERE id = %s
        """

cursor.execute(sql, ("League of Legends", 2010, 9.9, 1))

conn.commit()
conn.close()