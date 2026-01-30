class Predateur:
    def __init__(self, nom: str, age: int):
        pass

class Proie:
    def __init__(self, nom: str, age: int):
        pass

class Vegetal:
    def __init__(self, nom: str):
        pass

class Jeu:
    def __init__(self, predateurs: list[Predateur], proies: list[Proie], vegetaux: list[Vegetal]):
        self.predateurs = predateurs
        self.proies = proies
        self.vegetaux = vegetaux

    def naissance(self):
        """Regarde les règles et change les variables en fonction des naissance. Augmente également l'âge"""
        ...
        return self.predateurs, self.proies, self.vegetaux
    
    def mort(self):
        """Regarde les règles et change les variables en fonction des morts."""
        ...
        return self.predateurs, self.proies, self.vegetaux

##########################################################################

def update(jour, predateur, proie, vegetal):
    """Fonction principal qui va etre utiliser par Flask"""
    ...