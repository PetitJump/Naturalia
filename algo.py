from random import randint
import json

def naissance(data: dict, jour: int, predateur: dict, proie: dict, vegetal: dict):
    """Regarde les règles et change les variables en fonction des naissance"""
    if jour % data[predateur["nom"]]["reproduction"][0] == 0: #Si il peut se reproduire en fonction des règles
        nouveau_en_plus = data[predateur["nom"]]["reproduction"][1] * (predateur["nombres"] // 2) #On prend le nombres de nouveau né et on le mutltiplie avec le nombre de couple de loup
        nv_predateur = {"nom" : predateur["nom"], "nombres" : predateur["nombres"] + nouveau_en_plus}
    else:
        nv_predateur = predateur

    if jour % data[proie["nom"]]["reproduction"][0] == 0: 
        nouveau_en_plus = data[proie["nom"]]["reproduction"][1] * (proie["nombres"] // 2)
        nv_proie = {"nom" : proie["nom"], "nombres" : proie["nombres"] + nouveau_en_plus}
    else:
        nv_proie = proie

    if jour % data[vegetal["nom"]]["reproduction"][0] == 0: 
        nouveau_en_plus = data[vegetal["nom"]]["reproduction"][1] * (vegetal["nombres"] // 2)
        nv_vegetal = {"nom" : vegetal["nom"], "nombres" : vegetal["nombres"] + nouveau_en_plus}
    else:
        nv_vegetal = vegetal

    return nv_predateur, nv_proie, nv_vegetal

def mort(data: dict, jour: int, predateur: dict, proie: dict, vegetal: dict):
    """Regarde les règles et change les variables en fonction des morts."""
    
    if jour % data[predateur["nom"]]["mange"][1] == 0:
        proie_necessaires = predateur["nombres"] // data[predateur["nom"]]["mange"][1]
        if proie["nombres"] >= proie_necessaires:
            proie = {"nom": proie["nom"], "nombres": proie["nombres"] - proie_necessaires}
        else:
            predateur = {"nom": predateur["nom"], "nombres": proie["nombres"] * data[predateur["nom"]]["mange"][1]}
            proie = {"nom": proie["nom"], "nombres": 0}

    if jour % data[proie["nom"]]["mange"][1] == 0:
        vegetal_necessaires = proie["nombres"] * data[proie["nom"]]["mange"][2]
        if vegetal["nombres"] >= vegetal_necessaires:
            vegetal = {"nom": vegetal["nom"], "nombres": vegetal["nombres"] - vegetal_necessaires}
        else:
            proie = {"nom": proie["nom"], "nombres": vegetal["nombres"] // data[proie["nom"]]["mange"][2]}
            vegetal = {"nom": vegetal["nom"], "nombres": 0}
    
    return predateur, proie, vegetal


def random_repro(data: dict) -> dict:
    """
    La fonction va prendre en compte la reproduction des êtres vivants. Un nombre aléatoire de bébés vont naitre.
    C'est ce que la fonction va nous permettre de faire. randomiser le nombre de bébés a chaque naissance pour chaque couples.
    """
    for i in data:
        nvl_repro = randint(data[i]["reproduction"]["nombre_de_nv_nee"][0], data[i]["reproduction"]["nombre_de_nv_nee"][1])
        data[i]["reproduction"]["nombre_de_nv_nee"] = nvl_repro 
    return data


def update(jour, predateur, proie, vegetal):
    """Fonction principal qui va etre utiliser par Flask"""
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    data = random_repro(data)

    nv_predateur, nv_proie, nv_vegetal = naissance(data, jour, predateur, proie, vegetal)
    nv_predateur, nv_proie, nv_vegetal = mort(data, jour, predateur, proie, vegetal)
    
    return nv_predateur, nv_proie, nv_vegetal
