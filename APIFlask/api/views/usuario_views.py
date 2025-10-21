from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from ..entidades import usuario
from ..services import usuario_service
from flask import request, make_response, jsonify
from ..models.usuario_model import Usuario
from ..paginate import paginate

class UsuarioList(Resource):
    def get(self):
        usuarioSchema = usuario_schema.UsuarioSchema(many=True)
        return paginate(Usuario, usuarioSchema)
    
    def post(self):
        # Cria o schema de validação de dados
        usuarioSchema = usuario_schema.UsuarioSchema()
        # Passa a validação
        validate = usuarioSchema.validate(request.json)
        # Se tiver erro fale onde estão os erros e retorne junto o status 400
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome = request.json["nome"]
            email = request.json["email"]
            senha = request.json["senha"]

            # Chama a entidade de Professor
            novo_usuario = Usuario(nome=nome, email=email, senha=senha)

            resultado = usuario_service.cadastrar_usuario(usuario=novo_usuario)

            return make_response(usuarioSchema.dump(resultado), 201)

class UsuarioDetail(Resource):
    def get(self, id):
        usuario = usuario_service.listar_usuario_id(id)
        
        if usuario is None:
            return make_response("Usuario não encontrado", 484)
        
        usuarioSchema = usuario_schema.UsuarioSchema()
        return make_response(usuarioSchema.dump(usuario), 200)

    def put(self, id):
        usuario = usuario_service.listar_usuario_id(id)
        if usuario is None:
            return make_response("Usuario não foi encontrado", 484)
        usuarioSchema = usuario_schema.UsuarioSchema()
        validate = usuarioSchema.validate(request.json)
        if validate:
            return make_response(f"{validate}", 400)
        else:
            nome = request.json["nome"]
            email = request.json["email"]
            senha = request.json["senha"]

            resposta = usuario_service.alterar_usuario(id, nome, email, senha)
            if resposta is not None:
                usuario = usuario_service.listar_usuario_id(id)
            return make_response(usuarioSchema.dump(usuario), 200)


    def delete(self, id):
        resposta = usuario_service.delete_usuario(id)
        print(resposta)
        if resposta == '-1' or resposta == -1:
            return make_response("Falha ao excluir Usuario",400)
        else:
            return make_response("Sucesso ao excluir o Usuario", 200)

api.add_resource(UsuarioList, '/api/usuarios')
api.add_resource(UsuarioDetail, '/api/usuarios/<int:id>')