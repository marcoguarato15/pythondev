from ..models import formacao_model
from .professor_service import listar_professor_id
from api import db

def cadastrar_formacao(formacao):
    formacao_bd = formacao_model.Formacao(nome=formacao.nome, descricao=formacao.descricao)
    for i in formacao.professores:
        professor = listar_professor_id(i)
        formacao_bd.professores.append(professor)

    db.session.add(formacao_bd)
    db.session.commit()

    return formacao_bd

def listar_formacoes():
    formacao = formacao_model.Formacao.query.all()
    return formacao

def listar_formacao_id(id):
    formacao = formacao_model.Formacao.query.filter_by(id=id).first()
    return formacao

def alterar_formacao(id, nome, descricao, professores):
    formacao = formacao_model.Formacao.query.get(id)
    formacao.nome = nome
    formacao.descricao = descricao

    formacao.professores.clear()

    for i in professores:
        professor = listar_professor_id(i)
        formacao.professores.append(professor)
    
    db.session.commit()

    return formacao

def delete_formacao(id):
    formacao = formacao_model.Formacao.query.filter_by(id=id).delete()
    if formacao == 1:
        db.session.commit()
        return formacao
    else:
        return None
    