from ..models import professor_model
from api import db

def cadastrar_professor(professor):
    professor = professor_model.Professor(nome=professor.nome, idade=professor.idade)

    db.session.add(professor)
    db.session.commit()

    return professor

def listar_professores():
    professor = professor_model.Professor.query.all()
    return professor

def listar_professor_id(id):
    professor = professor_model.Professor.query.filter_by(id=id).first()
    return professor

def alterar_professor(id, nome, idade):
    professor = professor_model.Professor.query.get(id)
    professor.nome = nome
    professor.idade = idade
    db.session.commit()
    return professor

def delete_professor(id):
    professor = professor_model.Professor.query.filter_by(id=id).delete()
    if professor == 1:
        db.session.commit()
        return professor
    else:
        return None
    