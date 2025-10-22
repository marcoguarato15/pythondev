from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
import os

## Importações para verificar erros internos de JWT da API
# from flask import jsonify, request
# from jwt import ExpiredSignatureError


app = Flask(__name__,  template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))
app.config.from_object('config')


db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
api = Api(app)

## Função que verifica todas requisições com /api/ na url e gera erros específicos para cada um
## Possui um erro quando vai verificar se possui um token valido mostrado a baixo
# -> jwt.exceptions.DecodeError: Invalid header string: 'utf-8' codec can't decode byte 0x88 in position 6: invalid start byte

# @app.before_request
# def intercept_expired_token():
#     from flask_jwt_extended.view_decorators import verify_jwt_in_request
#     from flask_jwt_extended.exceptions import NoAuthorizationError

#     # Só verifica JWT em rotas protegidas (que contêm /api/)
#     if "/api/" in request.path:
#         try:
#             verify_jwt_in_request(optional=True)
#         except ExpiredSignatureError:
#             return jsonify({
#                 "error": "token_expirado",
#                 "message": "O token JWT expirou. Faça login novamente."
#             }), 401
#         except NoAuthorizationError:
#             return jsonify({
#                 "error": "token_ausente",
#                 "message": "Você precisa enviar um token JWT para acessar este recurso."
#             }), 401
#         except Exception as e:
#             # Captura outros erros JWT
#             if "token" in str(e).lower():
#                 return jsonify({
#                     "error": "jwt_invalido",
#                     "message": str(e)
#                 }), 422

from .views import curso_views, formacao_views, professor_views, usuario_views, login_views
from .models import curso_model, formacao_model, professor_model, usuario_model