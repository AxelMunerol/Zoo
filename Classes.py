import random

prédateur = ["lion", "tigre", 'politique', 'pretre', 'loup']

class Zoo:
    def __init__(self):
        self.nbcages = 0
        self.cages = []

    def add_cage(self, cage):
        self.nbcages += 1
        self.cages.append(cage)

    def get_cage_by_name(self, name):
        return next((cage for cage in self.cages if cage.nom == name), None)

    def __str__(self):
        noms_cages = ", ".join([cage.nom for cage in self.cages])
        cages_liste = "\n\n".join([str(cage) for cage in self.cages])
        return f"\nTotal : {self.nbcages} cage(s)\nListe des cages dans le zoo : {noms_cages}\n\n{cages_liste}"

class Cage:
    def __init__(self, nom):
        self.animaux = {}
        self.liste_animaux = []
        self.nom = nom
        self.total_individus = 0

    def add_animal(self, animal):
        if animal.espece in prédateur:
            rep = input(f"Cet animal est un prédateur. Peut-il entrer dans cette cage : {self.nom} (Oui/Non) ? ").lower()
            if rep in ["oui", "y", "yes", "o"]:
                if animal.espece in self.animaux:
                    self.animaux[animal.espece] += 1
                else:
                    self.animaux[animal.espece] = 1
                self.liste_animaux.append(animal)
            else:
                print("Ajout annulé.")
        else:
            if animal.espece in self.animaux:
                self.animaux[animal.espece] += 1
            else:
                self.animaux[animal.espece] = 1
            self.liste_animaux.append(animal)

    def carnage(self):

        prédateurs_in_cage = [animal.nom for animal in self.liste_animaux if animal.espece in prédateur]
        proies_in_cage = [animal.nom for animal in self.liste_animaux if animal.espece not in prédateur]

        if prédateurs_in_cage and proies_in_cage:
            tueur = random.choice(prédateurs_in_cage)
            tué = random.choice(proies_in_cage)
            print(f"Le carnage... {tueur} a dévoré {tué}.")


            animal_tué = next((animal for animal in self.liste_animaux if animal.nom == tué), None)
            if animal_tué:
                self.liste_animaux.remove(animal_tué)
                self.total_individus = sum(self.animaux.values())-1

        else:
            self.total_individus = sum(self.animaux.values())
            print(f"Il n'y a pas eu de carnage dans cette cage : {self.nom}")

    def __str__(self):



        liste_animaux = ", ".join([f"{espece} ({count})" for espece, count in self.animaux.items()])
        noms_individuels = ", ".join([f"{animal.nom} ({animal.espece})" for animal in self.liste_animaux])
        return (
            f"Voici la liste des animaux dans la cage '{self.nom}':\n"
            f"Espèces affichées devant la cage (comprenant les animaux morts) : {liste_animaux}\n"
            f"Noms : {noms_individuels}\n"
            f"Total : {self.total_individus} individu(s)."
        )


class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def __str__(self):
        return f"Cet animal s'appelle {self.nom} et est un.e {self.espece}"

