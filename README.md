# Ecologic — Guide de lancement

## Prérequis

- Python 3.10 ou supérieur
- pip

## Installation

Depuis le répertoire racine du projet :

pip install -r requirements.txt

## Lancement

Depuis le répertoire sources/ :

cd sources
python main.py

Ouvrir ensuite un navigateur à l'adresse : http://127.0.0.1:5000

## Structure du projet

Ecologic/
├── sources/
│   ├── main.py
│   ├── app.py
│   ├── algo.py
│   ├── static/
│   │   ├── style.css
│   │   ├── app.js
│   │   ├── regle.js
│   │   └── update.js
│   └── templates/
│       ├── index.html
│       ├── init.html
│       ├── game.html
│       ├── fin.html
│       ├── parametre.html
│       └── ajouter.html
├── data/
│   ├── data.json
│   ├── meteo.json
│   └── succes_permanents.json
├── presentation.md
├── readme.md
├── LICENSE
├── requirements.txt
└── usage_ia.md

## Remarques

- succes_permanents.json est créé automatiquement dans data/ au premier lancement.
- Les paramètres biologiques sont modifiables depuis l'interface (page Paramètres).
- Le projet ne nécessite pas de base de données ni de connexion internet.