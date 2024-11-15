from Classes import Zoo, Cage, Animal
zoo_des_fous = Zoo()

while True:
    action = input('Voulez-vous ajouter une [cage] ou un [animal] ? ([Quitter] pour sortir) : ').lower()

    # Ajouter une cage
    if action in ["cage", 'zone']:
        nom = input("Nom de la cage ? ")
        zoo_des_fous.add_cage(Cage(nom))

    # Ajouter un animal
    elif action in ["animal", "bebou"]:
        nom_cage = input("Nom de la cage où placer l'animal : ")
        cage_cible = zoo_des_fous.get_cage_by_name(nom_cage)
        if cage_cible:
            nom_animal = input("Nom de l'animal : ")
            espece_animal = input("Espèce de l'animal : ")
            cage_cible.add_animal(Animal(nom_animal, espece_animal))
        else:
            print("Cage introuvable.")

    # Quitter
    elif action in ["quitter", "exit"]:
        break

    # Saisie incorrecte
    else:
        print('Pas compris')

# Lancer le carnage dans chaque cage
for cage in zoo_des_fous.cages:
    cage.carnage()

# Afficher le zoo après carnage
print(zoo_des_fous)