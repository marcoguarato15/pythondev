from conn_post_psycopg import conn

cursor = conn.cursor()

sql =   """
            DELETE FROM games 
            WHERE id = %s
        """

cursor.execute(sql, (2,))

conn.commit()
conn.close()