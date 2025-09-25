import sqlite3

## 1 - Conectando e criando o CURSOR
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

## 2 - Fazendo a leitura de dados no DB # NESTE CASO retorna a instância do objeto e não os valores diretamente)
                                        # Necessita executar o fetchall() após o execute()
dados = cursor.execute("SELECT * FROM filmes")

# 3 - Mostrando os valores
print(f"Sem fetchall(): {dados}")
print(f"Com fetchall(): {dados.fetchall()}")

# NESTE CASO retorna os dados diretamente
dados1 = cursor.execute("SELECT * FROM filmes").fetchall()
print(f"Com fetchall já integrado: {dados1}")

conexao.close()
