from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)

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
@app.route("/filmes")
def filmes():
    url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=8f70c995cc6e1aca07304b3324d1fe2b"

    request = urllib.request.urlopen(url)
    dados = request.read()
    jsonData = json.loads(dados)

    return render_template("filmes.html", filmes=jsonData['results'])