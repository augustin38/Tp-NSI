def nombres_premiers():
  nbrepet = int(input("combien de nombres premiers voulez vous chercher :"))
  dico_nb = {} # on crée le dico qui va donner les infos sur chaque nombre
  for nombre in range(1,nbrepet): # on uttilise la double boucle pour tester les diviseurs 
    listdiv = []
    sommediv = nombre
    listdiv.append(nombre)
    for diviseur in range(1,nombre):
      reste = nombre % diviseur
      if reste == 0: # teste si le nombre a bien pour diviseur la valeur "diviseur"
        listdiv.append(diviseur) # on ajoute le diviseur a la liste des diviseurs
        sommediv += diviseur #on ajoute le diviseur a la somme des diviseurs
    if len(listdiv) > 2: # teste si le nb est premier
      premier = False
    else:
      premier = True
    dico_nb[nombre] = (listdiv,sommediv,premier) # ajoute toute les infos sur le nb dans le dico
  print(dico_nb)

def nombres_amicaux():
  nbrepet = int(input("combien de nombres amicaux voulez vous chercher :"))
  dico_nb = {}
  for nombre in range(1,nbrepet):
    sommediv = 0
    sommediv = diviseurs(nombre,sommediv) #fait la somme de tout les diviseurs de nombre
    nb_amical = sommediv
    sommediv_nb_amical = 0
    sommediv_nb_amical = diviseurs(nb_amical,sommediv_nb_amical) #fait la somme de tout les diviseurs du nombre amical
    if sommediv_nb_amical == nombre and nb_amical != nombre:# teste si l'un est egal a l'autre
      if nb_amical not in dico_nb: # teste si la valeur est deja dans la liste
        dico_nb[nombre] = (nb_amical) # on ajoute nombre et son nombre amical a la liste
  print(dico_nb)
  return(dico_nb)

def diviseurs(nombre,sommediv):
  for diviseur in range(1,nombre):
    reste = nombre % diviseur
    if reste == 0: # teste si chaque nombre est diviseur du nombre de base
      sommediv += diviseur
  return sommediv

nombres_premiers()
print("---------------------")
dico_nb = nombres_amicaux()
print("---------------------")
assert dico_nb[220] == 284
assert dico_nb[1184] == 1210
assert dico_nb[2620] == 2924
print("pas d'erreur")

      
      
      