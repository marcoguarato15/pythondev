from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__,  template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))
app.config.from_object('config')


db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

api = Api(app)

from .views import curso_views, formacao_views, professor_views
from .models import curso_model, formacao_model, professor_model