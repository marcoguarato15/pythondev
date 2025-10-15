from flask import Flask, render_template, request, redirect, url_for, flash
import urllib.request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

## Utilizar uma chave segura com um .env, mas como é um app de aprendizado não farei isto
app.secret_key = "apenas_uma_chave"

# Cria a configuração de url do Banco de Dados e chama a instancia do banco passando o Flask(app criado na linha 5)
# No código with app.app_context():... cria as tabelas e o banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cursos.sqlite3'

print("URL db:",app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)

# Importação das classes, Fazer uma fábrica de aplicativos para funcionar corretamente
# sem ser necessário importar após a criação da variável db (antes da erro de importação circular)
from Model.Cursos import Curso

## Cria o banco e as tabelas se não existirem
with app.app_context():
    db.create_all()

# Caso seja iniciado com python app.py é necessário ficar neste local pois
# ele configura o banco após inicializar o app para que não tenha uma importação circular (resolvida com uma fábrica de aplicativos)
if __name__ == "__main__":
    app.run()

# Inicialização com escopo global para não resetar a lista sempre que executar a função principal
frutas = []

@app.route("/", methods=["GET","POST"])
def principal():
    nome = "fulano"
    idade = 25

    fruta1 = "Morango"
    fruta2 = "Uva"
    fruta3 = "Maça"
    fruta4 = "Laranja"

    # list_frutas = ["Abacaxi", "Banana", "Kiwi", "Pêssego"]
    # Verificando o método do
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html",
                            nome = nome, idade = idade,
                            fruta1 = fruta1, fruta2 = fruta2, fruta3 = fruta3, fruta4 = fruta4,
                            #frutas=list_frutas
                            fruta=frutas
                            )

# Inicialização do dicionário para não sobrescrever ao adicionar
registros = []

@app.route("/sobre", methods=["GET", "POST"])
def sobre():
    #aluno_nota = {"Fulano":5.0, "Beltrano":6.0, "Aluno":7.0, "Sicrano":8.5}
    if request.method == "POST":
        if request.form.get("nome") and request.form.get("nota"):
            registros.append({"nome":request.form.get("nome"), "nota":request.form.get("nota")})
        

    return render_template("about/sobre.html",registros=registros)

'''
Outras rotas
'''
@app.route("/filmes/<propriedade>")
def filmes(propriedade):
    if propriedade == "popular":
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=8f70c995cc6e1aca07304b3324d1fe2b"
    elif propriedade == "kids":
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=8f70c995cc6e1aca07304b3324d1fe2b"
    elif propriedade == "2010":
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=8f70c995cc6e1aca07304b3324d1fe2b"
    elif propriedade == "drama":
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by-vote_average.desc&api_key=8f70c995cc6e1aca07304b3324d1fe2b"
    elif propriedade == "tom_cruise":
        url = "https://api.themoviedb.org/3/discover/movie?with_cast=500&sort_by=vote_average.desc&api_key=8f70c995cc6e1aca07304b3324d1fe2b"
        
    request = urllib.request.urlopen(url)
    dados = request.read()
    jsonData = json.loads(dados)

    return render_template("filmes.html", filmes=jsonData['results'])

@app.route("/cursos/<propriedade>", methods=["GET","POST"], endpoint="cursos")
@app.route("/cursos/<propriedade>/<int:id>", methods=["GET","POST"], endpoint="cursos")
def cursos(propriedade, id=None):
    if propriedade == "lista_cursos":
        return render_template('lista_cursos.html', cursos=Curso.query.all())
    
    elif propriedade == "create_cursos":
        msg = None
        if request.method == "POST":
            print("Método post")
            if (nome := request.form.get("nome").strip()) and (descricao := request.form.get("descricao").strip()) and (carga_horaria := request.form.get("carga_horaria").strip()):
                print("com campos ok")
                try:
                    curso = Curso(nome, descricao, carga_horaria)
                    with (session := db.session()):
                        session.add(curso)
                        session.commit()
                        print("Comitado")
                    msg = 1
                    flash("Curso Adicionado com Sucesso.","success")
                except Exception as e:
                    flash("Erro ao adicionar curso.", "error")
                    db.session.rollback()
            else:
                flash("Informe todos os campos do formulario.", "error")
        return render_template("create_cursos.html", msg=msg)   #', msg=msg' para mensagens de tela, verificando no Jinja e funcionando 
                                                                # com JS futuramente ver  se isto funciona
    elif propriedade == "alter_cursos":
        print("Entrou no alter cursos")
        if id is None:
            print("ID veio como None, PROBLEMA")
            flash("Falha ao acessar id","error")
            return redirect(url_for("cursos",propriedade="lista_cursos"))

        else:
            print("Passou o id para alter cursos")
            curso = Curso.query.get(id)
            if curso:
                if request.method == "POST":
                    print("Entrou no post alter_cursos")
                    nome = request.form.get("nome")
                    descricao = request.form.get("descricao")
                    carga_horaria = request.form.get("carga_horaria")

                    Curso.query.filter_by(id=id).update({"nome":nome, "descricao":descricao, "carga_horaria":carga_horaria})
                    
                    db.session.commit()
                    flash("Sucesso ao alterar Curso","success")
                    return redirect(url_for("cursos",propriedade="lista_cursos"))
                
                return render_template("alter_cursos.html")
            else:
                print("Não achou o ID no banco, PROBLEMA")
                flash("Falha ao acessar id no banco","error")
                return redirect(url_for("cursos",propriedade="lista_cursos"))
    elif propriedade == "delete_cursos":
        if id == None:
            flash("Falha ao pegar ip", "error")
            return redirect(url_for("curso",propriedade="lista_cursos"))
        elif id:
            curso = Curso.query.filter_by(id=id).first()
            try:
                
                db.session.delete(curso)
                db.session.commit()
                flash("Curso excluído com sucesso","success")
            except Exception as e:
                flash(f"Falha ao excluir,erro: {e}","error")
            return redirect(url_for("cursos",propriedade="lista_cursos"))
        else:
            flash("Falha geral","error")
            return redirect("cursos",propriedade="lista_cursos")
            

