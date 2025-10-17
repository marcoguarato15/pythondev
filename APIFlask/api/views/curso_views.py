from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from ..entidades import curso
from ..services import curso_service
from flask import request, make_response, jsonify

class CursoList(Resource):
    def get(self):
        cursos = curso_service.listar_cursos()
        cursoSchema = curso_schema.CursoSchema(many=True)
        return make_response(cursoSchema.dump(cursos), 200)
    

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

            # Chama a entidade de Curso
            novo_curso = curso.Curso(nome=nome, descricao=descricao)

            resultado = curso_service.cadastrar_curso(curso=novo_curso)
            res_criacao = cursoSchema.jsonify(resultado)
            return make_response(res_criacao, 201)

class CursoDetail(Resource):
    def get(self, id):
        curso = curso_service.listar_curso_id(id)
        
        if curso is None:
            return make_response("Curso não encontrado", 484)
        
        cursoSchema = curso_schema.CursoSchema()
        return make_response(cursoSchema.dump(curso), 200)

    def put(self, id, nome, descricao):
        pass

    def delete(self, id):
        pass

api.add_resource(CursoList, '/api/cursos')
api.add_resource(CursoDetail, '/api/cursos/<int:id>')