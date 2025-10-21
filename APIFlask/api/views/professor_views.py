from flask_restful import Resource
from api import api
from ..schemas import professor_schema
from ..entidades import professor
from ..services import professor_service
from flask import request, make_response, jsonify
from ..models.professor_model import Professor
from ..paginate import paginate

class ProfessorList(Resource):
    def get(self):
        professorSchema = professor_schema.ProfessorSchema(many=True)
        return paginate(Professor, professorSchema)
    
    def post(self):
        # Cria o schema de validação de dados
        professorSchema = professor_schema.ProfessorSchema()
        # Passa a validação
        validate = professorSchema.validate(request.json)
        # Se tiver erro fale onde estão os erros e retorne junto o status 400
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome = request.json["nome"]
            idade = request.json["idade"]

            # Chama a entidade de Professor
            novo_professor = professor.Professor(nome=nome, idade=idade)

            resultado = professor_service.cadastrar_professor(professor=novo_professor)

            return make_response(professorSchema.dump(resultado), 201)

class ProfessorDetail(Resource):
    def get(self, id):
        professor = professor_service.listar_professor_id(id)
        
        if professor is None:
            return make_response("Professor não encontrado", 484)
        
        professorSchema = professor_schema.ProfessorSchema()
        return make_response(professorSchema.dump(professor), 200)

    def put(self, id):
        professor = professor_service.listar_professor_id(id)
        if professor is None:
            return make_response("Professor não foi encontrado", 484)
        professorSchema = professor_schema.ProfessorSchema()
        validate = professorSchema.validate(request.json)
        if validate:
            return make_response(f"{validate}", 400)
        else:
            nome = request.json['nome']
            idade = request.json['idade']

            resposta = professor_service.alterar_professor(id, nome, idade)
            if resposta is not None:
                professor = professor_service.listar_professor_id(id)
            return make_response(professorSchema.dump(professor), 200)


    def delete(self, id):
        resposta = professor_service.delete_professor(id)
        print(resposta)
        if resposta == '-1' or resposta == -1:
            return make_response("Falha ao excluir Professor",400)
        else:
            return make_response("Sucesso ao excluir o Professor", 200)

api.add_resource(ProfessorList, '/api/professores')
api.add_resource(ProfessorDetail, '/api/professores/<int:id>')