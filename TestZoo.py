from Classes import Zoo,Cage,Animal

zoo_des_fous = Zoo()
cont = "Yes"

while True:
    action = input('Voulez-vous ajouter une [cage] ou un [animal] ? ([Quitter] pour sortir) : ').lower()
    if action in ["cage",'zone']:
        nom = input("nom de la cage ? ")
        zoo_des_fous.add_cage(Cage(nom))


    elif action in ["animal", "bebou"]:
        nom_cage = input("Nom de la cage où placer l'animal : ")
        cage_cible = zoo_des_fous.get_cage_by_name(nom_cage)
        if cage_cible:
            nom_animal = input("Nom de l'animal : ")
            espece_animal = input("Espèce de l'animal : ")
            cage_cible.add_animal(Animal(nom_animal, espece_animal))
            print(f"{nom_animal} ajouté à la cage {nom_cage}.")
        else:
            print("Cage introuvable.")


    elif action in ["quitter", "exit"]:
        break
    else:
        print('pas compris')


print(zoo_des_fous)