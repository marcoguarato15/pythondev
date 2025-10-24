from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, create_access_token, set_access_cookies, set_refresh_cookies, create_refresh_token
from flask import make_response, flash, redirect, url_for
from datetime import timedelta

def jwt_optional_refresh(view_func):
    def wrapper(*args, **kwargs):
        try:
            print("Teste")
            verify_jwt_in_request()
        except Exception:
            # access_token expirou → tenta usar refresh
            try:
                verify_jwt_in_request(refresh=True)
                identity = get_jwt_identity()
                new_access_token = create_access_token(
                    identity=identity,
                    expires_delta=timedelta(seconds=10)
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
    wrapper.__name__ = view_func.__name__
    return wrapper