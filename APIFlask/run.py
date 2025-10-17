from api import app
from flask import render_template
from api.views.curso_views import CursoList
from api.schemas.curso_schema import CursoSchema
from api.services import curso_service

@app.route("/")
def index():
    cursos = curso_service.listar_cursos()
    schema = CursoSchema(many=True)
    cursos_serializados = schema.dump(cursos)
    return render_template('index.html', cursos=cursos_serializados)


if __name__ == "__main__":
    app.run() 