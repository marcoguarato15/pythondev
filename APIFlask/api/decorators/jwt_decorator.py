from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, create_access_token
from flask_jwt_extended import  set_access_cookies, set_refresh_cookies, create_refresh_token, get_jwt
from flask import make_response, flash, redirect, url_for, jsonify, request
from flask_jwt_extended.exceptions import NoAuthorizationError
from api.services.usuario_service import listar_usuario_api_key
from jwt import ExpiredSignatureError
from datetime import timedelta
from functools import wraps

## PARA FRONTEND, VERIFICA O TOKEN E RETORNA PARA O LOGIN
def jwt_optional_refresh(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except Exception:
            # access_token expirou → tenta usar refresh
            try:
                verify_jwt_in_request(refresh=True)
                identity = get_jwt_identity()
                new_access_token = create_access_token(
                    identity=identity,
                    expires_delta=timedelta(minutes=15)
                    )
                new_refresh_token = create_refresh_token(identity=identity)
                response = make_response(view_func(*args, **kwargs))
                set_access_cookies(response, new_access_token)
                set_refresh_cookies(response, new_refresh_token)
                return response
            except Exception as e:
                flash(f"Sessão expirada. Faça login novamente.{e}", "error")
                return redirect(url_for("login"))
        return view_func(*args, **kwargs)
    return wrapper

## PARA API, VERIFICA OS ERROS E RETORNA EM JSON
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except NoAuthorizationError:
            return make_response(jsonify({"message":"Token ausente"}),401)
        except ExpiredSignatureError:
            return make_response(jsonify({"message":"Token expirado"}), 401)
        except Exception as e:
            return make_response(jsonify({"message":f"Token inválido"}))
        claims = get_jwt()
        if claims["roles"] != "admin":
            return make_response(jsonify({"message":"Usuario não possui autorização"}), 403)
        else:
            return fn(*args, **kwargs)
        
    return wrapper

def api_key_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # Necessário estar no padrão do flask X-NOME-DA-CHAVE se não ele ignora este header e não funciona
        api_key = request.headers.get("X-API-KEY")
        if api_key is not None:
            usuario = listar_usuario_api_key(api_key)
            if usuario.api_key == api_key:
                return fn(*args, **kwargs)
            else:
                return make_response(jsonify({"message":"Impedido, api key inválida"}), 401)
        else:
            return make_response(jsonify({"message":"Header api key faltando"}), 400)
    return wrapper