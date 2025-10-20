from api import app
from flask import render_template, request, flash, redirect, url_for
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
    if curso:
        schema = CursoSchema()
        curso_serializado = schema.dump(curso)
        return render_template("lista.html", cursos=[curso_serializado])
    else:
        return render_template("lista.html", cursos=None)

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

@app.route("/put_curso/<int:id>", methods=["GET", "POST"])
def put_curso(id):
    schema = CursoSchema()
    if request.method == "POST":
        if (nome := request.form.get("nome")) and (descricao := request.form.get("descricao")):
            validate = schema.validate(request.form)
            if validate:
                flash(f"Preencha os campos corretamente \n{validate}", "error")
            else:
                curso = curso_service.alterar_curso(id, nome, descricao)
                if curso:
                    flash("Curso alterado com sucesso","success")
                else:
                    flash("Falha em alterar o curso","error")
        else:
            flash("Preencha os campos corretamente","error")

    curso = curso_service.listar_curso_id(id)

    return render_template('put_curso.html', curso=schema.dump(curso))

@app.route("/del_curso/<int:id>", methods=["GET", "POST"])
def del_curso(id):
    resposta = curso_service.delete_curso(id)
    if resposta == -1:
        flash("Falha ao excluir curso","error")
    else:
        flash("Sucesso ao excluir curso","success")

    return redirect(url_for("cursos"))

if __name__ == "__main__":
    app.run()