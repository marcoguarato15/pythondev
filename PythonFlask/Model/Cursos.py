from app import db

class Cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    carga_horaria = db.Column(db.Integer)

    def __init__(self, nome, descricao, carga_horaria):
        self.nome = nome
        self.descricao = descricao
        self.carga_horaria = carga_horaria