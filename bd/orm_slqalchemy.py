from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# string que armazena a conexão com o banco
engine =  create_engine("sqlite:///banco.db", echo=True)
# string que armazena uma classe base para ser herdada em classes do projeto
Base = declarative_base()

class Filme(Base):
    # Linha obrigatória
    __tablename__ = "filmes"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

Base.metadata.create_all(engine)

# 1 - Adicionar filmes
def addFilme(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = (Filme(nome= nome, ano= ano, nota= nota))
    session.add(filme)

    session.commit()
    session.close()

addFilme("Homem Aranha", 2016, 9.8)
addFilme("Sonic", 2020, 8.5)


# 2 - Atualizar um filme
def updateFilme(id, nome=None, ano=None, nota=None):
    Session = sessionmaker(bind=engine)
    session = Session()

    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        if nome != None:
            filme.nome = nome
        if ano != None:
            filme.ano = ano
        if nota != None:
            filme.nota = nota
        session.commit()
        session.close()
        return 1
    else:
        session.close()
        return -1

resUpd = updateFilme(1, "O Dia Depois de Amanhã", 2015, 10.0)
print(f"{resUpd}")


# 3 - Deletar um filme
def delFilme(id):
    Session = sessionmaker(bind=engine)
    session = Session()

    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        session.delete(filme)
        session.commit()
        session.close()
        
        return 1
    else:
        session.close()
        return -1

resDel = delFilme(2)
print(f"{delFilme}")