from flask_restful import Resource
from api import api
from ..schemas import formacao_schema
from ..entidades import formacao
from ..services import formacao_service, professor_service
from flask import request, make_response, jsonify
from ..paginate import paginate
from ..models.formacao_model import Formacao
from flask_jwt_extended import jwt_required

class FormacaoList(Resource):
    @jwt_required()
    def get(self):
        formacaoSchema = formacao_schema.FormacaoSchema(many=True)
        return paginate(Formacao, formacaoSchema)
    
    @jwt_required()
    def post(self):
        # Validação com o schema de entrada
        input_schema = formacao_schema.FormacaoSchema()
        data = {
            "nome":request.json["nome"],
            "descricao":request.json["descricao"],
            "professores":[input_schema.dump(professor_service.listar_professor_id(id)) for id in request.json["professores"]]
            }
        validate = input_schema.validate(data)

        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json["nome"]
        descricao = request.json["descricao"]
        professores = request.json["professores"]
        print(professores)

        nova_formacao = formacao.Formacao(nome=nome, descricao=descricao, professores=professores)

        resultado = formacao_service.cadastrar_formacao(formacao=nova_formacao)

        # Serialização com o schema completo
        output_schema = formacao_schema.FormacaoSchema()
        return make_response(output_schema.dump(resultado), 201)

class FormacaoDetail(Resource):
    @jwt_required()
    def get(self, id):
        formacao = formacao_service.listar_formacao_id(id)
        
        if formacao is None:
            return make_response("Formacao não encontrado", 484)
        
        formacaoSchema = formacao_schema.FormacaoSchema()
        return make_response(formacaoSchema.dump(formacao), 200)

    @jwt_required()
    def put(self, id):
        formacao = formacao_service.listar_formacao_id(id)
        if formacao is None:
            return make_response("Formacao não foi encontrado", 484)
        formacaoSchema = formacao_schema.FormacaoSchema()
        validate = formacaoSchema.validate(request.json)
        if validate:
            return make_response(f"{validate}", 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            professores = request.json["professores"]

            # Chama a entidade de Formacao
            resposta = formacao_service.alterar_formacao(id, nome, descricao, professores)
            if resposta is not None:
                formacao = formacao_service.listar_formacao_id(id)
            return make_response(formacaoSchema.dump(formacao), 200)

    @jwt_required()
    def delete(self, id):
        resposta = formacao_service.delete_formacao(id)
        print(resposta)
        if resposta == '-1' or resposta == -1:
            return make_response("Falha ao excluir dado",400)
        else:
            return make_response("Sucesso ao excluir o Formacao", 200)

api.add_resource(FormacaoList, '/api/formacoes')
api.add_resource(FormacaoDetail, '/api/formacoes/<int:id>')