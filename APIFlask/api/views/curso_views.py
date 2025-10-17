from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from ..entidades import curso
from ..services import curso_service
from flask import request, make_response, jsonify

class CursoList(Resource):
    def get(self):
        return "Olá mundo!"
    def post(self):
        # Cria o schema de validação de dados
        cursoSchema = curso_schema.CursoSchema()
        # Passa a validação
        validate = cursoSchema.validate(request.json)
        # Se tiver erro fale onde estão os erros e retorne junto o status 400
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_criacao = request.json["data_criacao"]

            # Chama a entidade de Curso
            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_criacao=data_criacao)

            resultado = curso_service.cadastrar_curso(curso=novo_curso)
            res_criacao = cursoSchema.jsonify(resultado)
            return make_response(res_criacao, 201)

api.add_resource(CursoList, '/cursos')