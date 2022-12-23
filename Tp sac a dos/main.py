objet = {"A":[13,700],"B":[12,400],"C":[8,300],"D":[10,300]}

def val_massique(objet):
  for obj in objet.keys():
    val_mass = objet[obj][1] / objet[obj][0]
    val_mass = round(val_mass)
    vals_massiques.append(val_mass)
  return vals_massiques

def tri_dico(objet):
  pass
    
def methode_3(objet):
  while sac < 30:
    pass


vals_massiques = val_massique(objet)
print(vals_massiques)
print("--------------")
most = tri_dico(objet)
print(most)
