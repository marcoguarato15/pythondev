from flask_restful import Resource
from api import api
from ..schemas import login_schema
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

from ..services import usuario_service
from flask import request, make_response, jsonify

class LoginList(Resource):
    def post(self):
        # Cria o schema de validação de dados
        loginSchema = login_schema.LoginSchema()
        # Passa a validação
        validate = loginSchema.validate(request.json)
        # Se tiver erro fale onde estão os erros e retorne junto o status 400
        if validate:
            return make_response(jsonify(validate),400)
        else:
            email = request.json["email"]
            senha = request.json["senha"]

            usuario = usuario_service.get_usuario_by_email(email)

            if usuario and usuario.decriptar_senha(senha):
                access_token = create_access_token(
                    identity=str(usuario.id),
                    expires_delta=timedelta(seconds=100)
                )
                refresh_token = create_refresh_token(
                    identity=str(usuario.id)
                )

                return make_response(jsonify(
                    {
                        "access_token":access_token,
                        "refresh_token":refresh_token,
                        "message":"Login realizado com sucesso"
                    }
                ), 200)
            else:
                return make_response(jsonify({
                    "message":"Credenciais inválidas"
                }), 401)

api.add_resource(LoginList, '/api/login')
