from flask import Flask, render_template
from algo import tester #tester() est la fonction principale (la seul utiliser par flask)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/world")
def world():
    return render_template('world.html')

app.run(host = '127.0.0.1', port=5000, debug=True)
