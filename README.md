# Natulgo

## Tache a faire :

### Hugo (front-end):
- Faire le style.css (parler avec Margaut et Cal pour savoir ce qu'ils veulent)
- Faire le système d'animations (possibilité d'utiliser javascript/css/pthon)
- Reussir a rendre le site joli, facile à utiliser

### Carl (back-end / front-end):
- Implementer SQL et gerer une base de donnée sécuriser. 
- Aider Margaut a faire les pages html et à utiliser Flask

### Killian (back-end):
- Crée l'algo qui va faire fonctioner le site

### Margaut (front-end):
- Crée les pages html
- Implementer Flask, avec les bon chemins
- utilser l'algo de Killian pour envoyer les infos aux pages html

---

## Type de données :

### En SQL :
- Nom utilsateur
- Mot de passe crypter
- Niveau actuel

### Données à donné aux algos
L'algo principale 'test()' prend en entrée un dico

Voici un exemple : 
```python
test: dico = {
    "level_id": 1,
    "blocs": [
        {
            "type": "if",
            "condition": {
                "operateur": "and",
                "gauche": {
                    "type": "not",
                    "valeur": "pluie"
                },
                "droite": {
                    "type": "?",
                    "valeur": "sol_sec"
                }
            },
            "actions": [
                {
                    "type": "action",
                    "valeur": "arroser_plante"
                }
            ]
        }
    ]
}
```
Problème : Comment arriver à avoir ce gros dico

### Données que les algos donnent
Les données reçus servirtont a faire les actions necessaires en fonction de l'issus

Exemple :
```python
{
    "succès": False,
    "type-erreur": "logic",
    "message": "La plante meurt car elle n’est jamais arrosée"
}
```

## Bug actuels :
A remplir avec les bugs que l'on rencontre