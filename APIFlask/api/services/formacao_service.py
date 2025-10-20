from ..models import formacao_model
from api import db

def cadastrar_formacao(formacao):
    formacao = formacao_model.Formacao(nome=formacao.nome, descricao=formacao.descricao)

    db.session.add(formacao)
    db.session.commit()

    return formacao

def listar_formacoes():
    formacao = formacao_model.Formacao.query.all()
    return formacao

def listar_formacao_id(id):
    formacao = formacao_model.Formacao.query.filter_by(id=id).first()
    return formacao

def alterar_formacao(id, nome, descricao):
    formacao = formacao_model.Formacao.query.get(id)
    formacao.nome = nome
    formacao.descricao = descricao
    db.session.commit()
    return formacao

def delete_formacao(id):
    formacao = formacao_model.Formacao.query.filter_by(id=id).delete()
    if formacao == 1:
        db.session.commit()
        return formacao
    else:
        return None
    