from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from ..entidades import curso
from ..services import curso_service, formacao_service
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
            formacao = request.json["formacao_id"]

            formacao_curso = formacao_service.listar_formacao_id(formacao)

            if formacao_curso is None:
                return make_response(jsonify("Formação não foi encontrada"), 404)

            # Chama a entidade de Curso
            novo_curso = curso.Curso(nome=nome, descricao=descricao, formacao=formacao)

            resultado = curso_service.cadastrar_curso(curso=novo_curso)

            return make_response(cursoSchema.dump(resultado), 201)

class CursoDetail(Resource):
    def get(self, id):
        curso = curso_service.listar_curso_id(id)
        
        if curso is None:
            return make_response("Curso não encontrado", 484)
        
        cursoSchema = curso_schema.CursoSchema()
        return make_response(cursoSchema.dump(curso), 200)

    def put(self, id):
        try:
            curso_bd = curso_service.listar_curso_id(id)
            if curso_bd is None:
                return make_response("Curso não foi encontrado", 484)
            cursoSchema = curso_schema.CursoSchema()
            validate = cursoSchema.validate(request.json)
            if validate:
                return make_response(f"{validate}", 400)
            else:
                nome = request.json['nome']
                descricao = request.json['descricao']
                formacao = request.json["formacao_id"]
                
                formacao_curso = formacao_service.listar_formacao_id(formacao)

                if formacao_curso is None:
                    return make_response(jsonify("Não foi possível encontrar a formação"), 404)

                resposta = curso_service.alterar_curso(id, nome, descricao, formacao)
                
                if resposta is not None:
                    curso = curso_service.listar_curso_id(id)
                return make_response(cursoSchema.dump(curso), 200)
        except Exception as e:
            return make_response({"error":str(e)}, 501)

    def delete(self, id):
        resposta = curso_service.delete_curso(id)
        print(resposta)
        if resposta == '-1' or resposta == -1:
            return make_response("Falha ao excluir dado",400)
        else:
            return make_response("Sucesso ao excluir o curso", 200)

api.add_resource(CursoList, '/api/cursos')
api.add_resource(CursoDetail, '/api/cursos/<int:id>')