from flask_restful import Resource
from api import api
from ..schemas import login_schema
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from datetime import timedelta

from ..services import usuario_service
from flask import make_response, jsonify

class RefreshList(Resource):
    @jwt_required(refresh=True)
    def post(self):
        usuario_id = get_jwt_identity()
        access_token = create_access_token(
            identity=usuario_id,
            expires_delta=timedelta(minutes=15)
        )
        refresh_token = create_refresh_token(
            identity=usuario_id
        )
        return make_response(jsonify({
            "access_token":access_token,
            "refresh_token":refresh_token
        }), 200)
    
api.add_resource(RefreshList, '/api/refresh')
