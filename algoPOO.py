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
        ...
    
    def mort(self): #A faire par Marre Go
        """Regarde les règles et change les variables en fonction des morts."""
        ...
    
    def update(self, jour): #A faire par Carl
        """Fonction principal qui va etre utiliser par Flask"""
        ...
