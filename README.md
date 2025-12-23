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

### Données à donné à l'algo
L'algo principale 'test()' prend en entrée un dict

Voici un exemple : 
```python
data: dict = {
    "level_id": 1,
    "program": [
        {"id": "1", "type": "IF", "value": None},
        {"id": "2", "type": "CONDITION", "value": "pluie"},
        {"id": "3", "type": "ACTION", "value": "arroser_plante"}
    ]
}

```
Ce que ca veut dire : 
* Niveau 1
* SI pluie
* ALORS arroser_plante



### Données que l'algo donne
Les données reçus servirtont a faire les actions necessaires en fonction de l'issus

Exemple :
```python
{
    "success": False,
    "type_erreur": "logic",
    "message": "La plante meurt car elle n’est jamais arrosée"
}
```

## Règles importantes :
- Le "program" est une liste ordonnée
- L’ordre des blocs représente la logique
- Flask ne valide pas la logique
- Toute l’analyse est faite par l’algorithme


---

## Bug actuels :
A remplir avec les bugs que l'on rencontre

# Présentation du projet

Notre projet est un site éducatif qui apprend la logique algorithmique à travers la nature et l’écologie, sans coder directement. 

L’utilisateur progresse dans des niveaux inspirés de phénomènes naturels (management d’un écosystème) en assemblant des blocs logiques pour résoudre chaque défi (un peu comme Scratch). 

Au fil de sa progression, les blocs évoluent : d’abord visuels et simples (« répéter x fois », « si ...», « sinon »), ils deviennent petit à petit de vrais blocs de code (« for i in range(x): », « if condition: », ...), guidant l’utilisateur vers la programmation réelle. Le moteur d’algorithmes, conçu par Killian, exécute les blocs et renvoie un feedback. Carl gère les niveaux JSON et la base SQL des utilisateurs, Hugo développe le front-end interactif et immersif, et Margot relie le tout via Flask (avec l’aide de Carl), assurant les échanges entre le moteur, la base et l’interface. 

Public visée : Collégiens qui veulent apprendre les bases de la logique algorithmique en python le tout de manière ludique. 

Pourquoi ça devrait marcher : Beaucoup des projets gagnants sont des projets éducatifs, donc je pense que lier éducatif, lucratif, le thème de la nature et python ensemble pourrait fonctionner.

Comment s’y prendre : Construire une version beta qui marche le plus rapidement possible. Puis améliorer cette version et faire le plus de mise à jours possible avant la date limite. 
A noté que l’on arrêtera de coder une semaine avant la date limite pour faciliter la création du dossier.