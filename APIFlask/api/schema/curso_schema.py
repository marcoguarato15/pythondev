from api import ma
from ..models import curso_model
from marshmallow import fields

class CursoSchema(ma.SQLAlchemyAutoSchema):
    model = curso_model.Curso
    _load_instance = True

    fields = ("id", "nome", "descricao","data_criacao")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    data_criacao = fields.Date(required=True)

    
    