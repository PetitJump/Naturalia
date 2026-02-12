from flask import Flask, render_template, request
import json
from algo import Predateur, Vegetal, Proie, Meute, Jeu
from graphique import creer_graphique

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/init")
def init(): 
    return render_template('init.html')


@app.route("/update_ajouter", methods=['GET', 'POST'])
def update_ajouter():
    global jeu, historique
    jour = int(request.form["base_jour"])

    for _ in range(int(request.form["loup"])):
        jeu.meute.predateurs.append(Predateur("loup", 0))

    for _ in range(int(request.form["cerf"])):
        jeu.proies.append(Proie("cerf", 0))

    for _ in range(int(request.form["herbe"])):
        jeu.vegetaux.append(Vegetal("herbe"))

    jeu.update(jour)
    jour += 1

    historique["loup"].append(len(jeu.meute.predateurs))
    historique["cerf"].append(len(jeu.proies))
    historique["herbe"].append(len(jeu.vegetaux))

    graph_url = creer_graphique(historique)

    return render_template(
        'game.html',
        predateur=len(jeu.meute.predateurs),
        jour=jour,
        proie=len(jeu.proies),
        vegetal=len(jeu.vegetaux),
        afficher_bouton=True,
        graph_url=graph_url
    )


@app.route("/ajouter", methods=['GET', 'POST'])
def ajouter(): 
    global jeu, historique
    jour = int(request.form["jour"])

    graph_url = creer_graphique(historique)

    return render_template(
        'ajouter.html',
        predateur=len(jeu.meute.predateurs),
        jour=jour,
        proie=len(jeu.proies),
        vegetal=len(jeu.vegetaux),
        graph_url=graph_url
    )


@app.route("/game", methods=['GET', 'POST'])
def game(): 
    global historique, jeu
    jour = int(request.form["jour"])
    
    if jour == 0:  # on init

        nb_loup = int(request.form["loup"])
        nb_cerf = int(request.form["cerf"])
        nb_herbe = int(request.form["herbe"])
        loups = [Predateur("loup", 0) for _ in range(nb_loup)]
        meute = Meute(loups)
        proies = [Proie("cerf", 0) for _ in range(nb_cerf)]
        vegetaux = [Vegetal("herbe") for _ in range(nb_herbe)]

        jeu = Jeu(meute, proies, vegetaux)

    jeu.update(jour)
    jour += 1

    historique["loup"].append(len(jeu.meute.predateurs))
    historique["cerf"].append(len(jeu.proies))
    historique["herbe"].append(len(jeu.vegetaux))

    graph_url = creer_graphique(historique)

    return render_template(
        'game.html',
        predateur=len(jeu.meute.predateurs),
        jour=jour,
        proie=len(jeu.proies),
        vegetal=len(jeu.vegetaux),
        afficher_bouton=True,
        graph_url=graph_url
    )


@app.route("/parametre")
def regles(): 
    return render_template('parametre.html')
    

@app.route("/modifier", methods=['GET', 'POST'])
def modifier(): 

    loup_reproduction_tout_les = int(request.form['nb_bebe_tout_les_preda'])
    loup_reproduction_combien = [
        int(request.form['nb_bebe_predateur1']),
        int(request.form['nb_bebe_predateur2'])
    ]
    loup_mange_tout_les = int(request.form['nb_de_nourriture_tout_les_predateur'])
    loup_mange_combien = int(request.form['nb_de_nourriture_predateur'])

    cerf_reproduction_tout_les = int(request.form['nb_bebe_tout_les_proie'])
    cerf_reproduction_combien = [
        int(request.form['nb_bebe_proie1']),
        int(request.form['nb_bebe_proie2'])
    ]
    cerf_mange_tout_les = int(request.form['nb_de_nourriture_tout_les_proie'])
    cerf_mange_combien = int(request.form['nb_de_nourriture_proie'])

    herbe_reproduction_tout_les = int(request.form['nb_bebe_tout_les_vegetal'])
    herbe_reproduction_combien = [
        int(request.form['nb_bebe_vegetal1']),
        int(request.form['nb_bebe_vegetal2'])
    ]

    data = {
        "loup": {
            "reproduction": {
                "tout_les": loup_reproduction_tout_les,
                "nombre_de_nv_nee": loup_reproduction_combien,
                "maturiter_sexuel": 2
            },
            "mange": {
                "qui": "cerf",
                "tout_les": loup_mange_tout_les,
                "combien": loup_mange_combien
            }
        },
        "cerf": {
            "reproduction": {
                "tout_les": cerf_reproduction_tout_les,
                "nombre_de_nv_nee": cerf_reproduction_combien,
                "maturiter_sexuel": 2
            },
            "mange": {
                "qui": "herbe",
                "tout_les": cerf_mange_tout_les,
                "combien": cerf_mange_combien
            }
        },
        "herbe": {
            "reproduction": {
                "tout_les": herbe_reproduction_tout_les,
                "nombre_de_nv_nee": herbe_reproduction_combien
            }
        }
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return render_template('index.html')


@app.route("/credit")
def credit():
    return render_template("credit.html")
    

if __name__ == '__main__':
    historique = {"loup": [], "cerf": [], "herbe": []}
    app.run(host='127.0.0.1', port=5000, debug=True)
