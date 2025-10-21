from ..models import curso_model
from flask import request
from ..models.curso_model import Curso
from api import db

def cadastrar_curso(curso):
    curso_bd = curso_model.Curso(nome=curso.nome, descricao=curso.descricao, data_criacao=curso.data_criacao, formacao_id=curso.formacao_id)

    db.session.add(curso_bd)
    db.session.commit()

    return curso_bd

def listar_cursos():
    page = request.args.get("page", 1, type=int)
    per_page = 2
    cursos = Curso.query.paginate(page=page, per_page=per_page)
    return cursos

def listar_curso_id(id):
    curso = curso_model.Curso.query.filter_by(id=id).first()
    return curso

def alterar_curso(id, nome, descricao,formacao):
    curso = curso_model.Curso.query.get(id)
    curso.nome = nome
    curso.descricao = descricao
    curso.formacao_id = formacao
    db.session.commit()
    return curso

def delete_curso(id):
    curso = curso_model.Curso.query.filter_by(id=id).delete()
    if curso == 1:
        db.session.commit()
        return curso
    else:
        return -1
    