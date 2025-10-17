from api import app
from flask import render_template
from api.views.curso_views import CursoList
from api.schemas.curso_schema import CursoSchema
from api.services import curso_service

@app.route("/cursos")
def cursos():
    cursos = curso_service.listar_cursos()
    schema = CursoSchema(many=True)
    cursos_serializados = schema.dump(cursos)
    return render_template('lista.html', cursos=cursos_serializados)

@app.route("/cursos/<int:id>")
def curso_id(id):
    curso = curso_service.listar_curso_id(id)
    schema = CursoSchema()
    curso_serializado = schema.dump(curso)
    return render_template("lista.html", cursos=[curso_serializado])

if __name__ == "__main__":
    app.run()