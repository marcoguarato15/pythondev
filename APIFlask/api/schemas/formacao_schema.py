from api import ma
from ..models import formacao_model
from marshmallow import Schema, fields
from ..schemas import curso_schema, professor_schema

class FormacaoInputSchema(Schema):
    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    professores = fields.List(fields.Integer(), required=True)

class FormacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = formacao_model.Formacao
        _load_instance = True
        fields = ("id", "nome", "descricao", "cursos", "professores")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    cursos = fields.List(fields.Nested(curso_schema.CursoSchema, only=("id","nome")))
    professores = fields.List(fields.Nested(professor_schema.ProfessorSchema, only=("id","nome")))