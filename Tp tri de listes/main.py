import random

def créer_tab(N):
  tab = [0]*N
  for i in range(0,N):
    tab[i] = random.randint(0,1000)
  return tab


def indice_min(tab,compteur,ind,N):
  nb = ind
  for i in range(ind,N):
    if tab[i] < tab[nb]:
      nb = i
    compteur = i
  return nb,compteur


def algo_echange(tab,i,j):
  aux = tab[i]
  tab[i] = tab[j]
  tab[j] = aux


def tri_selection(tab,N):
  compteur = 0
  for ind in range(0,N-1):
    min,compteur = indice_min(tab,compteur,ind,N)
    algo_echange(tab,ind,min)
  print("------------")
  print(tab)
  print("------------")
  print("le nombre de comparaisons :",compteur)

N = int(input("de quelle longueur voulez vous créer un tableau ? : "))
tab = créer_tab(N)
tri_selection(tab,N)