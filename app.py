from flask import Flask, render_template, request, session
import json
from algo import update #tester() est la fonction principale (la seul utiliser par flask)
app = Flask(__name__)

@app.route("/")
def index(): #Par Hugo
    return render_template("index.html")

@app.route("/init")
def init(): #Par Hugo
    predateur = {"nom" : "loup", "nombres" : ...}
    proie = {"nom" : "mouton", "nombres" : ...}
    vegetal = {"nom" : "herbe", "nombres" : ...}
    jour = ... #Peut etre utiliser les sessions
    predateur, proie, vegetal = update(jour, predateur, proie, vegetal) #Va mettre a jour les datas avec les algos

    return render_template('init.html')

@app.route("/game")
def game(): #Par Margaux
    ...
    return render_template('game.html')


@app.route("/regles")
def regles(): #Par Killian et Carl
    ...
    return render_template('regles.html')
    
    
@app.route("/modifier")
def modifier(): #Par Killian et Carl
    loup_reproduction_tout_les: int = request.form['...']
    loup_reproduction_combien: list[int] = [request.form['...'], request.form['...']]
    loup_mange_tout_les: int = request.form['...']
    loup_mange_combien: int = request.form['...']

    mouton_reproduction_tout_les: int = request.form['...']
    mouton_reproduction_combien: list[int] = [request.form['...'], request.form['...']]
    mouton_mange_tout_les: int = request.form['...']
    mouton_mange_combien: int = request.form['...']

    herbe_reproduction_tout_les: int = request.form['...']
    herbe_reproduction_combien: list[int] = [request.form['...'], request.form['...']]

    data = {
        "loup" : {
            "reproduction" : {"tout_les" : loup_reproduction_tout_les, "nombre_de_nv_nee" : loup_reproduction_combien}, 
            "mange" : {"qui" : "mouton", "tout_les" : loup_mange_tout_les, "combien" : loup_mange_combien}
        },

        "mouton" : {
            "reproduction" : {"tout_les" : mouton_reproduction_tout_les, "nombre_de_nv_nee" : mouton_reproduction_combien},
            "mange" : {"qui" : "herbe", "tout_les" : mouton_mange_tout_les, "combien" : mouton_mange_combien}
        },

        "herbe" : {
            "reproduction" : {"tout_les" : herbe_reproduction_tout_les, "nombre_de_nv_nee" : herbe_reproduction_combien}
        }
}

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port=5000, debug=True)
