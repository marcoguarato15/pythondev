from flask import Flask, render_template, request

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

@app.route("/sobre")
def sobre():
    aluno_nota = {"Fulano":5.0, "Beltrano":6.0, "Aluno":7.0, "Sicrano":8.5}
    return render_template("about/sobre.html",aluno_nota=aluno_nota)