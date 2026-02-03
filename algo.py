from random import randint

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