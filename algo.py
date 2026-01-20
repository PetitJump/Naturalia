from random import randint
import json

def init_age(predateur, proie):
    predateur["age"] = []
    for i in range(predateur["nombres"]):
        predateur["age"].append(randint(0, 5)) #Les loup de bases auront entre 0 et 5 ans

    proie["age"] = []
    for i in range(proie["nombres"]):
        proie["age"].append(randint(0, 5)) #Les moutons de bases auront entre 0 et 5 ans

    return predateur, proie
    
def naissance(data: dict, jour: int, predateur: dict, proie: dict, vegetal: dict): 
    """Regarde les règles et change les variables en fonction des naissance. Augmente également l'âge"""
    if jour % data[predateur["nom"]]["reproduction"]["tout_les"] == 0: #Si il peut se reproduire en fonction des règles
        nouveau_en_plus = data[predateur["nom"]]["reproduction"]["nombre_de_nv_nee"] * (predateur["nombres"] // 2) #On prend le nombres de nouveau né et on le mutltiplie avec le nombre de couple de loup
        for i in range(nouveau_en_plus):
            predateur["age"].append(0) #Un nouveau née
        nv_predateur = {"nom" : predateur["nom"], "nombres" : predateur["nombres"] + nouveau_en_plus, "age" : predateur["age"]}

    else:
        nv_predateur = predateur
    for i in range(len(predateur["age"])):
        nv_predateur["age"][i] += 1

    if jour % data[proie["nom"]]["reproduction"]["tout_les"] == 0: 
        nouveau_en_plus = data[proie["nom"]]["reproduction"]["nombre_de_nv_nee"] * (proie["nombres"] // 2)
        for i in range(nouveau_en_plus):
            proie["age"].append(0) #Un nouveau née
        nv_proie = {"nom" : proie["nom"], "nombres" : proie["nombres"] + nouveau_en_plus, "age" : proie["age"]}
    else:
        nv_proie = proie
    for i in range(len(proie["age"])):
        nv_proie["age"][i] += 1

    if jour % data[vegetal["nom"]]["reproduction"]["tout_les"] == 0 and vegetal["nombres"] < 2500: 
        nouveau_en_plus = data[vegetal["nom"]]["reproduction"]["nombre_de_nv_nee"] * (vegetal["nombres"] // 2)
        nv_vegetal = {"nom" : vegetal["nom"], "nombres" : vegetal["nombres"] + nouveau_en_plus}
    else:
        nv_vegetal = vegetal

    return nv_predateur, nv_proie, nv_vegetal

def mort(data: dict, jour: int, predateur: dict, proie: dict, vegetal: dict):
    """Regarde les règles et change les variables en fonction des morts."""
    predateur["age"] = [k for k in predateur["age"] if k < 20]
    proie["age"] = [k for k in proie["age"] if k < 20]

    if jour % data[predateur["nom"]]["mange"]["tout_les"] == 0:
        combien = data[predateur["nom"]]["mange"]["combien"]
        proie_necessaires = predateur["nombres"] * combien

        if proie["nombres"] >= proie_necessaires:
            proie = {"nom": proie["nom"],"nombres":  proie["nombres"] - proie_necessaires, "age" : proie["age"]} 
            for i in range(proie_necessaires):
                proie["age"].pop() #Les plus jeunes meurts
        else:
            predateur_survivants = proie["nombres"] // combien
            predateur = {"nom": predateur["nom"],"nombres": predateur_survivants, "age" : predateur["age"]}
            proie = {"nom": proie["nom"], "nombres": 0 , "age" : []} 
            if predateur_survivants <= 0:
                predateur["age"] = []
            for i in range(predateur_survivants):
                predateur["age"].pop() #Les plus jeunes meurts

    if jour % data[proie["nom"]]["mange"]["tout_les"] == 0:
        combien = data[proie["nom"]]["mange"]["combien"]
        vegetal_necessaires = proie["nombres"] * combien

        if vegetal["nombres"] >= vegetal_necessaires:
            vegetal = {"nom": vegetal["nom"],"nombres": vegetal["nombres"] - vegetal_necessaires}
        else:
            proie_survivantes = vegetal["nombres"] // combien
            proie = {"nom": proie["nom"],"nombres": proie_survivantes, "age" : proie["age"]}
            vegetal = {"nom": vegetal["nom"], "nombres": 0}

    return predateur, proie, vegetal


def random_repro(data: dict) -> dict:
    """
    La fonction va prendre en compte la reproduction des êtres vivants. Un nombre aléatoire de bébés vont naitre.
    C'est ce que la fonction va nous permettre de faire. randomiser le nombre de bébés a chaque naissance pour chaque couples.
    """
    for i in data:
        nv_j = randint(data[i]["reproduction"]["tout_les"][0], data[i]["reproduction"]["tout_les"][1])
        data[i]["reproduction"]["tout_les"] =  nv_j
        nvl_repro = randint(data[i]["reproduction"]["nombre_de_nv_nee"][0], data[i]["reproduction"]["nombre_de_nv_nee"][1])
        data[i]["reproduction"]["nombre_de_nv_nee"] = nvl_repro 
    return data

def anomalie(jour, predateur, proie, vegetal) -> bool:
    """Renvoie True si une anomalie est en vu. Sinon False"""
    for i in range(2):
        jour += 1
        predateur, proie, vegetal = update(jour, predateur, proie, vegetal)
    if predateur["nombres"] == 0 or proie["nombres"] == 0:
        return True
    return False

def update(jour, predateur, proie, vegetal):
    """Fonction principal qui va etre utiliser par Flask"""
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    data = random_repro(data)

    nv_predateur, nv_proie, nv_vegetal = naissance(data, jour, predateur, proie, vegetal)
    nv_predateur, nv_proie, nv_vegetal = mort(data, jour, nv_predateur, nv_proie, nv_vegetal)

    if nv_vegetal["nombres"] < 10:
        nv_vegetal["nombres"] = 10
        
    return nv_predateur, nv_proie, nv_vegetal
