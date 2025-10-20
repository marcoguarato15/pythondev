from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__,  template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))
app.config.from_object('config')
app.secret_key = '123'

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

api = Api(app)

from .views import curso_views, formacao_views
from .models import curso_model, formacao_model