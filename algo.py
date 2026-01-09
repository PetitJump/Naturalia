from random import randint
import json

def initialisation_variables():
    """Initalise les variables d'environements"""
    nb_de_jour = int(input("Combien de jour la simulation ? : "))
    nb_loup = int(input("Combien de loup ? : "))
    nb_mouton = int(input("Combien de mouton ? : "))
    herbe = int(input("Combien d'herbe ? : "))

    predateur = {"nom" : "loup", "nombres" : nb_loup}
    proie = {"nom" : "mouton", "nombres" : nb_mouton}
    vegetal = {"nom" : "herbe", "nombres" : herbe}
    return nb_de_jour, predateur, proie, vegetal


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
    
    if jour % 2 != 0:
        proie_necessaires = predateur["nombres"] // data[predateur["nom"]]["mange"][1]
        if proie["nombres"] >= proie_necessaires:
            proie = {"nom": "mouton", "nombres": proie["nombres"] - proie_necessaires}
        else:
            predateur = {"nom": "loup", "nombres": proie["nombres"] * data[predateur["nom"]]["mange"][1]}
            proie = {"nom": "mouton", "nombres": 0}
        vegetal_necessaires = proie["nombres"] * data[proie["nom"]]["mange"][2]
        if vegetal["nombres"] >= vegetal_necessaires:
            vegetal = {"nom": "herbe", "nombres": vegetal["nombres"] - vegetal_necessaires}
        else:
            proie = {"nom": "mouton", "nombres": vegetal["nombres"] // data[proie["nom"]]["mange"][2]}
            vegetal = {"nom": "herbe", "nombres": 0}
    
    return predateur, proie, vegetal


def random_repro(data: dict) -> dict:
    """
    La fonction va prendre en compte la reproduction des êtres vivants. Un nombre aléatoire de bébés vont naitre.
    C'est ce que la fonction va nous permettre de faire. randomiser le nombre de bébés a chaque naissance pour chaque couples.
    """
    for i in data:
        nvl_repro = randint(data[i]["reproduction"][1][0], data[i]["reproduction"][1][1])
        data[i]["reproduction"][1] = nvl_repro 
    return data

def main():
    print("Bienvenue sur ce jeu")
    nb_de_jour, predateur, proie, vegetal = initialisation_variables()

    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    data = random_repro(data)
    for i in range(nb_de_jour):
        predateur, proie, vegetal = naissance(data, i+1, predateur, proie, vegetal)
        proie, predateur, vegetal = mort(data, i+1, predateur, proie, vegetal)
        print("") #Saute une ligne
        print("Jour :", i + 1)
        print(f"{predateur["nom"]} : {predateur["nombres"]}")
        print(f"{proie["nom"]} : {proie["nombres"]}")
        print(f"{vegetal["nom"]}, {vegetal["nombres"]}")
        input("Appuyer pour continuer")
main()

def tester(jour, continent):
    """Fonction principal qui va etre utiliser par Flask"""
    nb_predateur = ...
    nb_proie = ...
    nb_vegetal = ...
    
    return nb_predateur, nb_proie, nb_vegetal
