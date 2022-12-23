from random import randint


def min(liste):
  global comparaison
  indice_min = 0
  for indice in range(len(liste)):
    comparaison += 1
    if liste[indice] < liste[indice_min]:
      indice_min = indice
  return indice_min

def echange(i, j, liste):
  aux = liste[i] # variable auxiliaire
  liste[i] = liste[j]
  liste[j] = aux

def tri(liste):
  global comparaison
  comparaison = 0
  #liste = [randint(0, 1000) for a in range(randint(5, 10))]
  print("Voici votre liste en désordre : ")
  print(liste)
  for a in range(len(liste)-1):
    if a == 0:
      # si a == 0, liste[a:len(liste)] ne renvoie pas la liste entière,
      # elle revoie la liste sans l'élém d'indice 0
      minimum = min(liste)
    else:
      minimum = min(liste[a:len(liste)])
      # Ne prend pas en compte les nombres déja triés
      # donc l'indice renvoyé est l'indice dans liste[a:len(liste)]
      # pour avoir l'indice de la dans la vrai liste, on fait minimum+a
    echange(a, minimum+a, liste)
    print(liste)
    
  print("")
  print("Voici votre liste triée : ")
  print(liste)
  print(f"Cela a pris {comparaison} comparaisons")
  print("---------------------------")
  return liste

assert tri([2,5,1,3,4]) == [1,2,3,4,5]
assert tri([11,20,17,5,19,13,16]) == [5, 11, 13, 16, 17, 19, 20]
assert tri([65, 839, 433, 21, 983, 249, 56]) == [21, 56, 65, 249, 433, 839, 983]
assert tri([-5, -4, -0.5, -3.42, -1221]) == [-1221, -5, -4, -3.42, -0.5]
print("Test passé")
