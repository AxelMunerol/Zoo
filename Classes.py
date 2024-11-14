class Zoo:
    def __init__(self):
        self.nbcages = 0
        self.cages = []

    def add_cage(self, cage):
        self.nbcages += 1
        self.cages.append(cage)

    def __str__(self):
        cages_liste = "\n".join([str(cage) for cage in self.cages])
        return f"Voici la liste des cages dans le zoo :\n{cages_liste}\nTotal : {self.nbcages} cage(s)"


class Cage:
    def __init__(self,nom):
        self.animaux = {}
        self.nom = nom
    def add_animal(self, animal):
        if animal.espece in self.animaux:
            self.animaux[animal.espece] += 1  #
        else:
            self.animaux[animal.espece] = 1


    def __str__(self):
        liste_animaux = ", ".join([f"{animal} ({count})" for animal, count in self.animaux.items()])
        nbr_total = sum(self.animaux.values())
        return f"Voici la liste des animaux dans la {self.nom} : {liste_animaux}, avec un total de {nbr_total} individus."

class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def __str__(self):
        return f"Cet animal s'appelle {self.nom} et est un.e {self.espece}"


