from Classes import Zoo,Cage,Animal

zoo_des_fous = Zoo()

cage_des_lions = Cage("Cage des lions")
cage_des_oiseaux = Cage("Cage des oiseaux")

martin = Animal("Martin", "Lion")
luc = Animal("Luc", "Lion")
steven = Animal("Steven", "Tigre")
fredo = Animal("Fredo","Grue")
cage_des_lions.add_animal(martin)
cage_des_lions.add_animal(luc)
cage_des_lions.add_animal(steven)
cage_des_oiseaux.add_animal(fredo)

zoo_des_fous.add_cage(cage_des_oiseaux)
zoo_des_fous.add_cage(cage_des_lions)
print(zoo_des_fous)
print(martin)
print(cage_des_lions)