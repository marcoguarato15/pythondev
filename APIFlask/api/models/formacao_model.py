from api import db

class Formacao(db.Model):
    __tablename__ = 'formacao'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(40), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)

