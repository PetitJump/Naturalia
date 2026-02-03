class Predateur:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

class Proie:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

class Vegetal:
    def __init__(self, nom: str):
        self.nom = nom

class Jeu:
    def __init__(self, predateurs: list[Predateur], proies: list[Proie], vegetaux: list[Vegetal]):
        self.predateurs: list = predateurs
        self.proies: list = proies
        self.vegetaux: list = vegetaux

    def naissance(self): #A faire par Petit Hugo
        """Regarde les règles et change les variables en fonction des naissance. Augmente également l'âge"""
        def naissance(self, data: dict, jour: int):
        """Regarde les règles et change les variables en fonction des naissances. Augmente également l'âge."""
        if self.predateurs:
            nom_p = self.predateurs[0].nom
            regle_p = data[nom_p]["reproduction"]
            for p in self.predateurs:
                p.age += 1
            if jour % regle_p["tout_les"] == 0:
                nb_bebes = regle_p["nombre_de_nv_nee"] * (len(self.predateurs) // 2)
                for _ in range(nb_bebes):
                    self.predateurs.append(Predateur(nom_p, 0)) 
        if self.proies:
            nom_pr = self.proies[0].nom
            regle_pr = data[nom_pr]["reproduction"]
            for pr in self.proies:
                pr.age += 1
            if jour % regle_pr["tout_les"] == 0:
                nb_bebes = regle_pr["nombre_de_nv_nee"] * (len(self.proies) // 2)
                for _ in range(nb_bebes):
                    self.proies.append(Proie(nom_pr, 0)) 
        if self.vegetaux:
            nom_v = self.vegetaux[0].nom
            regle_v = data[nom_v]["reproduction"]
            if jour % regle_v["tout_les"] == 0 and len(self.vegetaux) < 2500:
                nb_pousses = regle_v["nombre_de_nv_nee"] * (len(self.vegetaux) // 2)
                for _ in range(nb_pousses):
                    self.vegetaux.append(Vegetal(nom_v))
    
    
    def mort(self): #A faire par Marre Go
        """Regarde les règles et change les variables en fonction des morts."""
        ...
    
    def update(self, jour): #A faire par Carl
        """Fonction principal qui va etre utiliser par Flask"""
        import json
        from algo import random_repro

        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        data = random_repro(data)

        nv_predateur, nv_proie, nv_vegetal = self.naissance()
        nv_predateur, nv_proie, nv_vegetal = self.mort()

        if nv_vegetal["nombres"] < 10:
            nv_vegetal["nombres"] = 10
            
        return nv_predateur, nv_proie, nv_vegetal
