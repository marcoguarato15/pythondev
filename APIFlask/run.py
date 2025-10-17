from api import app
from flask import render_template, request, flash
from api.views.curso_views import CursoList
from api.schemas.curso_schema import CursoSchema
from api.services import curso_service
from api.entidades.curso import Curso

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

@app.route("/add_curso", methods=["GET","POST"])
def add_curso():
    if request.method == "POST":
        if (nome := request.form.get("nome")) and (descricao := request.form.get("descricao")):
            schema = CursoSchema()
            validate = schema.validate(request.form)
            if validate:
                flash(f"Preencha os campos: {validate}", "error")
            else:
                curso = curso_service.cadastrar_curso(Curso(nome, descricao))
                if curso:
                    flash("Curso cadastrado com sucesso","success")
                else:
                    flash("Falha ao cadastrar curso","error")
    return render_template("add_curso.html")

if __name__ == "__main__":
    app.run()