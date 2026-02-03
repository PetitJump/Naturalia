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
        self.predateurs: list[Predateur] = predateurs
        self.proies: list[Proie] = proies
        self.vegetaux: list[Vegetal] = vegetaux

    def naissance(self, data: dict, jour: int):
        """Regarde les règles et change les variables en fonction des naissances. Augmente également l'âge."""
        if jour % data["loup"]["reproduction"]["tout_les"] == 0: #Si il peut se reproduire en fonction des règles
            nouveau_en_plus = data["loup"]["reproduction"]["nombre_de_nv_nee"] * (len(self.predateurs) // 2) #On prend le nombres de nouveau né et on le mutltiplie avec le nombre de couple de loup
            for _ in range(nouveau_en_plus):
                self.predateurs.append(Predateur("loup", 0)) #Un nouveau née d'age 0

        for k in self.predateurs: #On augmente l'age
            k.age += 1

        if jour % data["mouton"]["reproduction"]["tout_les"] == 0: 
            nouveau_en_plus = data["mouton"]["reproduction"]["nombre_de_nv_nee"] * (len(self.proies) // 2)
            for _ in range(nouveau_en_plus):
                self.proies.append(Proie("loup", 0)) #Un nouveau née d'age 0

        for k in self.proies: #On augmente l'age
            k.age += 1

        if jour % data["herbe"]["reproduction"]["tout_les"] == 0 and len(self.vegetaux) < 2500: 
            nouveau_en_plus = data["herbe"]["reproduction"]["nombre_de_nv_nee"] * (len(self.vegetaux) // 2)
            for _ in range(nouveau_en_plus):
                self.vegetaux.append(Vegetal("herbe"))

    
    def mort(self, data : dict, jour : int): 
        """Regarde les règles et change les variables en fonction des morts."""
        ...
    
    def update(self, jour): 
        """Fonction principal qui va etre utiliser par Flask"""
        import json
        from algo import random_repro

        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        data = random_repro(data)

        nv_predateur, nv_proie, nv_vegetal = self.naissance(data, jour)
        nv_predateur, nv_proie, nv_vegetal = self.mort(data, jour)

        if nv_vegetal["nombres"] < 10: #Probleme ici
            nv_vegetal["nombres"] = 10 #Probleme ici
            
        return nv_predateur, nv_proie, nv_vegetal
