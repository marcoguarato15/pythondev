from ..models import usuario_model
from flask import request
from api import db


def cadastrar_usuario(usuario):
    usuario = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario.encriptar_senha()
    db.session.add(usuario)
    db.session.commit()

    return usuario

def get_usuario_by_email(email):
    usuario_email = usuario_model.Usuario.query.filter_by(email=email).first()
    return usuario_email

def listar_usuarios():
    page = request.args.get("page", 1, type=int)
    per_page = 2
    usuario = usuario_model.Usuario.query.paginate(page=page, per_page=per_page)
    return usuario

def listar_usuario_id(id):
    usuario = usuario_model.Usuario.query.filter_by(id=id).first()
    return usuario

def alterar_usuario(id, nome, email, senha):
    usuario = usuario_model.Usuario.query.get(id)
    usuario.nome = nome
    usuario.email = email
    usuario.senha = senha
    db.session.commit()
    return usuario

def delete_usuario(id):
    usuario = usuario_model.Usuario.query.filter_by(id=id).delete()
    if usuario == 1:
        db.session.commit()
        return usuario
    else:
        return None
    