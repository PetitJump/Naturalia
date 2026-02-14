import random
import json

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
    def __init__(self, meute: Meute, proies: list[Proie], vegetaux: list[Vegetal]):
        self.meute = meute
        self.proies = proies
        self.vegetaux = vegetaux

    def naissance(self, data: dict, jour: int):
        """Regarde les règles et change les variables en fonction des naissances. Augmente également l'âge."""
        if jour % data["loup"]["reproduction"]["tout_les"] == 0: #Si il peut se reproduire en fonction des règles
            age_min = data["loup"]["reproduction"]["maturiter_sexuel"]
            predateurs_majeurs = [k for k in self.meute.predateurs if k.age > age_min] #Touts les predateurs qui on plus que x ans
            nouveau_en_plus = data["loup"]["reproduction"]["nombre_de_nv_nee"] * (len(predateurs_majeurs) // 2) #On prend le nombres de nouveau né et on le mutltiplie avec le nombre de couple de loup
            for _ in range(nouveau_en_plus):
                self.meute.predateurs.append(Predateur("loup", 0)) #Un nouveau née d'age 0

        for k in self.meute.predateurs: #On augmente l'age
            k.age += 1

        if jour % data["cerf"]["reproduction"]["tout_les"] == 0: 
            age_min = data["cerf"]["reproduction"]["maturiter_sexuel"]
            proies_majeurs = [k for k in self.proies if k.age > age_min] #Toutes les proie qui on plus que x ans
            nouveau_en_plus = data["cerf"]["reproduction"]["nombre_de_nv_nee"] * (len(proies_majeurs) // 2)
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
        self.meute.predateurs = [k for k in self.meute.predateurs if k.age < 20] #Tue tout les predateurs qui ont plus de 20 ans
        self.proies = [k for k in self.proies if k.age < 20] #Tue toutes les proies qui ont plus de 20 ans
        self.taux_de_survie()

        if jour % data["loup"]["mange"]["tout_les"] == 0:
            combien = data["loup"]["mange"]["combien"]
            proie_necessaires = len(self.meute.predateurs) * combien

            if len(self.proies) >= proie_necessaires:
                for i in range(proie_necessaires):
                    self.proies.pop() #Les plus jeunes meurts
            else: #Si il n'y a pas assez de cerfs pour tout les loups
                predateur_survivants = len(self.proies) // combien
                self.proies = []
                if predateur_survivants <= 0:
                    self.meute.predateurs = []
                for _ in range(predateur_survivants):
                    self.meute.predateurs.pop() #Les plus jeunes meurts
    
    def taux_de_survie(self):
        """Gère le système de taux de survie naturel"""
        survivants_predateurs = []
        for k in self.meute.predateurs:
            if k.age == 0:
                taux = 0.6 #Un nouveau né a un taux de survie de 60%
            else:
                taux = 0.9 #Taux de survie de 90%

            if random.random() < taux: #random.random() renvoie un float entre 0.0 et 1.0
                survivants_predateurs.append(k)

        self.meute.predateurs = survivants_predateurs

        survivants_proies = []
        for k in self.proies:
            if k.age == 0:
                taux = 0.6 #Un nouveau né a un taux de survie de 60%
            else:
                taux = 0.9 #Taux de survie de 90%

            if random.random() < taux:
                survivants_proies.append(k)

        self.proies = survivants_proies

    def evenement_meteo(self):
        """Gère les évènement météorologique"""
        with open('meteo.json', 'r', encoding='utf-8') as f:
            meteo = json.load(f)
        ... #On regarde si c le moment
        #Si c le moment alors on gère le système de dégats/mort

        """A un moment il y aura obligatoirement ca :"""
        self.meute.predateurs #Liste des Prédateurs dans le jeu
        self.proies #Liste des Proies dans le jeu
        self.vegetaux #Liste des Vegetal dans le jeu

    def update(self, jour): 
        """Fonction principal qui va etre utiliser par Flask"""
        from petites_fonctions import random_repro

        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        data = random_repro(data)

        self.naissance(data, jour)
        self.mort(data, jour)
        #self.evenement_meteo()
        #Si on veut tester la fonction on enlève le commentaire

        if len(self.vegetaux) < 10: 
            for _ in range(15):
                self.vegetaux.append(Vegetal("herbe"))
            
        return self.meute.predateurs, self.proies, self.vegetaux
