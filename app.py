from flask import Flask, render_template
from algo import update #tester() est la fonction principale (la seul utiliser par flask)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/world")
def world():
    predateur = {"nom" : "loup", "nombres" : ...}
    proie = {"nom" : "mouton", "nombres" : ...}
    vegetal = {"nom" : "herbe", "nombres" : ...}
    jour = ... #Peut etre utiliser les sessions
    predateur, proie, vegetal = update(jour, predateur, proie, vegetal) #Va mettre a jour les datas avec les algos

    return render_template('world.html')

app.run(host = '127.0.0.1', port=5000, debug=True)

