def adicionar_usuario(cursor, id, nome, email):
    cursor.execute(
        """
        INSERT INTO users VALUES (?, ?, ?)
        """, (id, nome, email)
    )


def buscar_usuario_email(cursor, email):
    res = cursor.execute(
        """
        SELECT * FROM users WHERE email = ?
        """, (email,)
    )

    return res.fetchone()