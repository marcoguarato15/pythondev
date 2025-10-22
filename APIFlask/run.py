from api import app
from flask import render_template, request, flash, redirect, url_for, make_response
from api.schemas.curso_schema import CursoSchema
from api.schemas.formacao_schema import FormacaoSchema, FormacaoInputSchema
from api.schemas.professor_schema import ProfessorSchema
from api.services import curso_service, formacao_service, professor_service, usuario_service
from api.entidades.curso import Curso
from api.entidades.formacao import Formacao
from api.entidades.professor import Professor
from api.schemas.login_schema import LoginSchema
from flask_jwt_extended import set_access_cookies, create_access_token, jwt_required
from datetime import timedelta



from sqlalchemy.exc import IntegrityError

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        loginSchema = LoginSchema()
        validate = loginSchema.validate({"email":email,"senha":senha})
        if validate:
            flash(f"Preencha os campos corretamente {validate}","error")
        else:
            usuario = usuario_service.get_usuario_by_email(email)
            if usuario and usuario.decriptar_senha(senha):
                access_token = create_access_token(
                    identity=str(usuario.id),
                    expires_delta=timedelta(seconds=100)
                )
                response = make_response(redirect(url_for("cursos")))
                set_access_cookies(response, access_token)
                return response
            else:
                flash("Credenciais inválidas","error")
    
    return render_template("login.html")

@app.route("/cursos")
@jwt_required()
def cursos():
    cursos = curso_service.listar_cursos()
    schema = CursoSchema(many=True)
    formacoes = formacao_service.listar_formacoes()
    f_schema = FormacaoSchema(many=True)
    formacoes_serializadas = f_schema.dump(formacoes)
    return render_template('lista.html', cursos=cursos, formacoes=formacoes_serializadas)

@app.route("/cursos/<int:id>")
@jwt_required()
def curso_id(id):
    curso = curso_service.listar_curso_id(id)
    if curso:
        schema = CursoSchema()
        curso_serializado = schema.dump(curso)
        return render_template("lista.html", cursos=[curso_serializado])
    else:
        return render_template("lista.html", cursos=None)

@app.route("/add_curso", methods=["GET","POST"])
@jwt_required()
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
@jwt_required()
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
@jwt_required()
def del_curso(id):
    resposta = curso_service.delete_curso(id)
    if resposta == -1:
        flash("Falha ao excluir curso","error")
    else:
        flash("Sucesso ao excluir curso","success")

    return redirect(url_for("cursos"))

@app.route("/formacoes")
@jwt_required()
def formacoes():
    formacoes = formacao_service.listar_formacoes()


    return render_template("lista_formacoes.html", formacoes=formacoes)

@app.route("/add_formacao", methods=["GET","POST"])
@jwt_required()
def add_formacao():
    nome = ""
    descricao = ""
    professores_ids = []
    if request.method == "POST":

        nome = request.form.get("nome")
        descricao =  request.form.get("descricao")
        professores_ids = [int(p) for p in request.form.getlist("professores")]
        if nome and descricao and professores_ids:
            data = {
                "nome":nome,
                "descricao":descricao,
                "professores":professores_ids
            }
            formacaoSchema = FormacaoInputSchema()
            validate = formacaoSchema.validate(data)

            if validate:
                flash(f"Informe os campos: {validate}","error")
            else:
                formacao = formacao_service.cadastrar_formacao(Formacao(nome, descricao, professores_ids))
                if formacao:
                    flash("Sucesso ao adicionar formação","success")
                    return redirect(url_for("add_formacao"))
                else:
                    flash("Falha ao adicionar Formação","error")
        else:
            erros = ""
            if nome == "": 
                erros += " Nome faltando "
            if descricao == "":
                erros += " Descrição faltando "
            if professores_ids == []:
                erros += " Professores faltando "

            flash(f"Preencha os campos corretamente: {erros}","error")

    professores = professor_service.listar_professores()
    print(professores)
    return render_template("add_formacao.html", professores=professores, nome=nome, descricao=descricao, professores_ids=professores_ids)

@app.route("/put_formacao/<int:id>", methods=["GET", "POST"])
@jwt_required()
def put_formacao(id):
    formacao = formacao_service.listar_formacao_id(id)
    professores = professor_service.listar_professores()

    if formacao is None:
        flash("Falha ao solicitar formação", "error")
        return redirect(url_for("formacoes"))

    if request.method == "POST":
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        professores = request.form.getlist("professores")

        if nome and descricao:
            formacao_schema = FormacaoInputSchema()
            validate = formacao_schema.validate({
                "nome": nome,
                "descricao": descricao,
                "professores": professores
            })

            if validate:
                flash(f"Preencha os dados corretamente: {validate}", "error")
            else:
                formacao = formacao_service.alterar_formacao(id, nome, descricao, professores)
                flash("Sucesso ao alterar formação", "success")

    return render_template("put_formacao.html", formacao=formacao, professores=professores)

@app.route("/del_formacao/<int:id>")
@jwt_required()
def del_formacao(id):
    try:
        formacao = formacao_service.listar_formacao_id(id)
        if formacao:
            formacao = formacao_service.delete_formacao(id)
            flash("Sucesso ao excluir formação","success")
        else:
            flash("Falha ao detectar formação","error")
    except IntegrityError as e:
        flash(f"Erro de integridade, impossível excluir","error")
        print(e)
    return redirect(url_for('formacoes'))


@app.route("/professores")
@jwt_required()
def professores():
    professores = professor_service.listar_professores()
    return render_template("lista_professor.html", professores=professores)

@app.route("/add_professor", methods=["GET","POST"])
@jwt_required()
def add_professor():
    if request.method == "POST":
        if (nome := request.form.get("nome")) and (idade := request.form.get("idade")):
            nome_professor = nome
            idade_professor = idade
            professorSchema = ProfessorSchema()
            validate = professorSchema.validate(request.form)
            if validate:
                flash(f"Informe os campos: {validate}","error")
            else:
                professor = professor_service.cadastrar_professor(Professor(nome_professor, idade_professor))
                if professor:
                    flash("Sucesso ao adicionar Professor","success")
                else:
                    flash("Falha ao adicionar Professor","error")
        else:
            flash("Preencha os campos corretamente","error")

    return render_template("add_professor.html")

@app.route("/put_professor/<int:id>",methods=["GET","POST"])
@jwt_required()
def put_professor(id):
    professor = professor_service.listar_professor_id(id)
    if professor is None:
        flash("Falha ao solicitar professor", "error")
        return redirect(url_for("professores"))
    else:
        if request.method == "POST":
            if (nome := request.form.get("nome")) and (idade := request.form.get("idade")):
                professor_schema = ProfessorSchema()
                validate = professor_schema.validate(request.form) 
                if validate:
                    flash("preencha os dados corretamente","error")
                else:
                    professor = professor_service.alterar_professor(id,nome,idade)
                    flash("Sucesso ao alterar Professor","success")
    return render_template("put_professor.html", professor=professor)

@app.route("/del_professor/<int:id>")
@jwt_required()
def del_professor(id):
    try:
        professor = professor_service.listar_professor_id(id)
        if professor:
            professor = professor_service.delete_professor(id)
            flash("Sucesso ao excluir professor","success")
        else:
            flash("Falha ao detectar professor","error")
    except IntegrityError as e:
        flash(f"Erro de integridade, impossível excluir","error")
        print(e)
    return redirect(url_for('professores'))


if __name__ == "__main__":
    app.run()