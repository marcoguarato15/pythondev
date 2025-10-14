from flask import Flask, render_template, request
import urllib.request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Caso seja iniciado com python app.py é necessário ficar neste local pois
# ele configura o banco após inicializar o app para que não tenha uma importação circular (resolvida com uma fábrica de aplicativos)
if __name__ == "__main__":
    app.run()

# Cria a configuração de url do Banco de Dados e chama a instancia do banco passando o Flask(app criado na linha 5)
# No código with app.app_context():... cria as tabelas e o banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cursos.sqlite3'
db = SQLAlchemy(app)

# Importação das classes, Fazer uma fábrica de aplicativos para funcionar corretamente
# sem ser necessário importar após a criação da variável db (antes da erro de importação circular)
from Model.Cursos import Cursos


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

## Cria o banco e as tabelas se não existirem
with app.app_context():
    db.create_all()

