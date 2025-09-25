import sqlite3

# 1 - Conectando e criando o CURSOR
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

## 2 - Inserindo dados
nome = input("Insira o nome do Filme: ")
ano = int(input("Insira o Ano de lançamento do filme: "))
nota = float(input("Insira a nota do Filme: "))


cursor.execute(
    # """
    #     INSERT INTO filmes (nome, ano, nota)
    #     VALUES('Super Mario Bros', 2022, 9.5)
    # """
    # """
    #     INSERT INTO filmes (nome, ano, nota)
    #     VALUES ('Top Gun Maverick', 2022, 9.0)
    # """
    f"""
        INSERT INTO filmes (nome, ano, nota)
        VALUES ('{nome}', {ano}, {nota})
    """
)

print("Dados inseridos com sucesso!")
conexao.commit()
conexao.close()