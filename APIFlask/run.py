from api import app
from flask import render_template, request, flash, redirect, url_for
from api.schemas.curso_schema import CursoSchema
from api.schemas.formacao_schema import FormacaoSchema
from api.services import curso_service, formacao_service
from api.entidades.curso import Curso
from api.entidades.formacao import Formacao

@app.route("/cursos")
def cursos():
    cursos = curso_service.listar_cursos()
    schema = CursoSchema(many=True)
    cursos_serializados = schema.dump(cursos)
    formacoes = formacao_service.listar_formacoes()
    f_schema = FormacaoSchema(many=True)
    formacoes_serializadas = f_schema.dump(formacoes)
    print(formacoes_serializadas)
    return render_template('lista.html', cursos=cursos_serializados, formacoes=formacoes_serializadas)

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
    formacoes = formacao_service.listar_formacoes()
    print(formacoes)
    if request.method == "POST":
        if (nome := request.form.get("nome")) and (descricao := request.form.get("descricao")) and (formacao_id := request.form.get("formacao_id")):
            schema = CursoSchema()
            validate = schema.validate(request.form)
            print(validate)
            if validate:
                flash(f"Preencha os campos: {validate}", "error")
            else:
                print(nome, descricao, formacao_id)
                curso = curso_service.cadastrar_curso(Curso(nome=nome, descricao=descricao, formacao_id=formacao_id))
                if curso:
                    flash("Curso cadastrado com sucesso","success")
                else:
                    flash("Falha ao cadastrar curso","error")
        else:
            flash("Preencha todos os campos","error")

    return render_template("add_curso.html", formacoes=formacoes)

@app.route("/put_curso/<int:id>", methods=["GET", "POST"])
def put_curso(id):
    schema = CursoSchema()
    formacoes = formacao_service.listar_formacoes()
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

    return render_template('put_curso.html', curso=schema.dump(curso), formacoes=formacoes)

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