from flask import Flask, render_template, request, session
import json
import copy
from algo import init_age, update, anomalie

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/init")
def init(): 
    return render_template('init.html')

@app.route("/update_ajouter", methods=['GET', 'POST'])
def update_ajouter():
    global predateur, proie, vegetal
    jour = int(request.form["base_jour"])

    nv_preda = int(request.form["loup"]) + int(request.form["base_loup"])
    nv_proie = int(request.form["mouton"]) + int(request.form["base_mouton"])
    nv_vegetal = int(request.form["herbe"]) + int(request.form["base_herbe"])

    while len(predateur["age"]) < nv_preda:
        predateur["age"].append(0) #On ajoute les nouveaux nées
    predateur["nombres"] = nv_preda

    while len(proie["age"]) < nv_proie:
        proie["age"].append(0) #On ajoute les nouveaux nées
    proie["nombres"] = nv_proie

    vegetal["nombres"] = nv_vegetal

    predateur, proie, vegetal = update(jour, predateur, proie, vegetal)
    jour += 1

    historique["loup"].append(predateur["nombres"])
    historique["mouton"].append(proie["nombres"])
    historique["herbe"].append(vegetal["nombres"])
    
    afficher_bouton = anomalie(jour, copy.deepcopy(predateur), copy.deepcopy(proie), copy.deepcopy(vegetal)) #Fait la boucle sans modifier les vrai données (copy.deepcopy())

    return render_template('game.html', predateur=predateur["nombres"], jour=jour, proie=proie["nombres"], vegetal=vegetal["nombres"], afficher_bouton=afficher_bouton)

@app.route("/ajouter", methods=['GET', 'POST'])
def ajouter(): 
    global predateur, proie, vegetal
    jour = int(request.form["jour"])
    predateur = {"nom" : "loup", "nombres" : int(request.form["loup"]), "age" : predateur["age"]}
    proie = {"nom" : "mouton", "nombres" : int(request.form["mouton"]), "age" : proie["age"]}
    vegetal = {"nom" : "herbe", "nombres" : int(request.form["herbe"])}

    return render_template('ajouter.html', predateur=predateur["nombres"], jour=jour, proie=proie["nombres"], vegetal=vegetal["nombres"])

@app.route("/game", methods=['GET', 'POST'])
def game(): 
    global predateur, proie, vegetal, historique
    jour = int(request.form["jour"])
    
    if jour == 0: #On init
        predateur = {"nom" : "loup", "nombres" : int(request.form["loup"])}
        proie = {"nom" : "mouton", "nombres" : int(request.form["mouton"])}
        vegetal = {"nom" : "herbe", "nombres" : int(request.form["herbe"])}
        predateur, proie = init_age(predateur, proie) #On init l'âges des être vivants
        print("Init :", predateur, proie) #Test


    predateur["nombres"] = int(request.form["loup"])
    proie["nombres"] = int(request.form["mouton"])
    vegetal["nombres"] = int(request.form["herbe"])

    predateur, proie, vegetal = update(jour, predateur, proie, vegetal)
    jour += 1

    historique["loup"].append(predateur["nombres"])
    historique["mouton"].append(proie["nombres"])
    historique["herbe"].append(vegetal["nombres"])

    #afficher_bouton = anomalie(jour, predateur, proie, vegetal)
    afficher_bouton = True #Juste pour tester car la commande du haut bug (il update tout seul)
    print("Jour :", predateur, proie) #Test
    print("Historique :", historique)
    return render_template('game.html', predateur=predateur["nombres"], jour=jour, proie=proie["nombres"], vegetal=vegetal["nombres"], afficher_bouton=afficher_bouton)

@app.route("/regles")
def regles(): 
    return render_template('regles.html')
    
    
@app.route("/modifier", methods=['GET', 'POST'])
def modifier(): 
    loup_reproduction_tout_les: int = int(request.form['nb_bebe_tout_les_preda'])
    loup_reproduction_combien: list[int] = [int(request.form['nb_bebe_predateur1']), int(request.form['nb_bebe_predateur2'])]
    loup_mange_tout_les: int = int(request.form['nb_de_nourriture_tout_les_predateur'])
    loup_mange_combien: int = int(request.form['nb_de_nourriture_predateur'])

    mouton_reproduction_tout_les: int = int(request.form['nb_bebe_tout_les_proie'])
    mouton_reproduction_combien: list[int] = [int(request.form['nb_bebe_proie1']), int(request.form['nb_bebe_proie2'])]
    mouton_mange_tout_les: int = int(request.form['nb_de_nourriture_tout_les_proie'])
    mouton_mange_combien: int = int(request.form['nb_de_nourriture_proie'])

    herbe_reproduction_tout_les: int = int(request.form['nb_bebe_tout_les_vegetal'])
    herbe_reproduction_combien: list[int] = [int(request.form['nb_bebe_vegetal1']), int(request.form['nb_bebe_vegetal2'])]

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
@app.route("/credit")
def credit():
    return render_template("credit.html")
    
if __name__ == '__main__':
    historique = {"loup" : [], "mouton" : [], "herbe" : []}
    app.run(host = '127.0.0.1', port=5000, debug=True)
