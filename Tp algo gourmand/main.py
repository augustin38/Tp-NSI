def rendu(monnaie_total,list_devises):
  devises = {}
  for a in range(0,len(list_devises)):
    if list_devises[a] <= monnaie_total:  
      devises[list_devises[a]] = monnaie_total // list_devises[a]
      monnaie_total = monnaie_total % list_devises[a]
  print ("liste des devises uttilisées :", devises)
  return devises

list_devises = [200,100,50,20,10,5,2,1]
list_devises_test = [50,20,10,6,1]
assert rendu(9,list_devises) == {5:1,2:2} #test pour 9
assert rendu(17,list_devises) == {10:1,5:1,2:1} #test pour 17
assert rendu(89,list_devises) == {50:1,20:1,10:1,5:1,2:2} #test pour 89
assert rendu(40,list_devises) == {20:2} #test pour 40
assert rendu(12,list_devises_test) == {5:1,2:2} #test pour 9 avec une autre monnaie
