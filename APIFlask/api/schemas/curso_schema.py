from api import ma
from ..models import curso_model
from marshmallow import fields

class CursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = curso_model.Curso
        _load_instance = True
        fields = ("id", "nome", "descricao","data_criacao", "formacao")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    data_criacao = fields.Date(dump_only=True)
    formacao = fields.Integer(required=True)
    
