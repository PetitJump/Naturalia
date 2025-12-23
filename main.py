from flask import request
#Fichier principale où il y aura Flask
#Crée d'autre fichier python si nécessaire


condition = request.form["condition"] #On prend la condition
action = request.form["action"] #Et on prend l'action

data = {
    "level_id": 1,
    "program": [
        {"id": "1", "type": "IF", "value": None},
        {"id": "2", "type": "CONDITION", "value": condition},
        {"id": "3", "type": "ACTION", "value": action}
    ]
}
