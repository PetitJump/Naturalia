class Predateur:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

class Meute:
    def __init__(self, predateurs: list[Predateur]):
        self.predateurs = predateurs

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
        self.predateurs = [k for k in self.predateurs if k.age < 20]
        self.proies = [k for k in self.proies if k.age < 20]

        if jour % data["loup"]["mange"]["tout_les"] == 0:
            combien = data["loup"]["mange"]["combien"]
            proie_necessaires = len(self.predateurs) * combien

            if len(self.proies) >= proie_necessaires:
                for i in range(proie_necessaires):
                    self.proies.pop() #Les plus jeunes meurts
            else: #Si il n'y a pas assez de moutons pour tout les loups
                predateur_survivants = len(self.proies) // combien
                self.proies = []
                if predateur_survivants <= 0:
                    self.predateurs = []
                for _ in range(predateur_survivants):
                    self.predateurs.pop() #Les plus jeunes meurts
    
    def update(self, jour): 
        """Fonction principal qui va etre utiliser par Flask"""
        import json
        from petites_fonctions import random_repro

        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        data = random_repro(data)

        self.naissance(data, jour)
        self.mort(data, jour)

        if len(self.vegetaux) < 10: 
            for _ in range(15):
                self.vegetaux.append(Vegetal("herbe"))
            
        return self.predateurs, self.proies, self.vegetaux
