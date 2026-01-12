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
    
    
@app.route("/modifier", methods=['GET', 'POST'])
def modifier(): #Par Killian et Carl
    loup_reproduction_tout_les: int = request.form['nb_bebe_tout_les_preda']
    loup_reproduction_combien: list[int] = [request.form['nb_bebe_predateur1'], request.form['nb_bebe_predateur2']]
    loup_mange_tout_les: int = request.form['nb_de_nourriture_tout_les_predateur']
    loup_mange_combien: int = request.form['nb_de_nourriture_predateur']

    mouton_reproduction_tout_les: int = request.form['nb_bebe_tout_les_proie']
    mouton_reproduction_combien: list[int] = [request.form['nb_bebe_proie1'], request.form['nb_bebe_proie2']]
    mouton_mange_tout_les: int = request.form['nb_de_nourriture_tout_les_proie']
    mouton_mange_combien: int = request.form['nb_de_nourriture_proie']

    herbe_reproduction_tout_les: int = request.form['nb_bebe_tout_les_vegetal']
    herbe_reproduction_combien: list[int] = [request.form['nb_bebe_vegetal1'], request.form['nb_bebe_vegetal2']]

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

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port=5000, debug=True)
