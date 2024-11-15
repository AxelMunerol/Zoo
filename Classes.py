prédateur = ["lion","tigre",'politique','pretre']
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
        cages_liste = "\n\n".join([str(cage) for cage in self.cages])  # Double saut de ligne entre les cages
        return ("\n\n"
            f"Total : {self.nbcages} cage(s)"
            f"\nListe des cages dans le zoo : {noms_cages}\n\n"
            f"{cages_liste}"
        )
class Cage:
    def __init__(self, nom):
        self.animaux = {}  # Compte des espèces
        self.liste_animaux = []  # Liste des instances d'Animal
        self.nom = nom

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



    def __str__(self):
        liste_animaux = ", ".join([f"{espece} ({count})" for espece, count in self.animaux.items()])
        noms_individuels = ", ".join([f"{animal.nom} ({animal.espece})" for animal in self.liste_animaux])
        nbr_total = sum(self.animaux.values())
        return (
            f"Dans votre super prison pour les animaux il y a : \n"
            f"Voici la liste des animaux dans la cage '{self.nom}':\n"
            f"Espèces : {liste_animaux}\n"
            f"Noms : {noms_individuels}\n"
            f"Total : {nbr_total} individu(s)."
        )

class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def __str__(self):
        return f"Cet animal s'appelle {self.nom} et est un.e {self.espece}"


