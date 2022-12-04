import math as m
def serie_test():
  def f_flottants_egaux(nb1,nb2) :
   egalite = False
   diff = abs(nb1-nb2)
   print("Différence entre les 2 nombres :",diff)
   if diff <= 10**(-9) :
     egalite = True
     print(nb1,"et",nb2,"sont égaux")
   else :
     print(nb1,"et",nb2,"ne sont PAS égaux")
   return egalite # true ou false
  
  def test_flottants_egaux() :
   import math as m
  
   assert f_flottants_egaux(0.3,0.1+0.2) == True
   assert f_flottants_egaux(m.sqrt(2),1.4142) == False
   assert f_flottants_egaux(0.1,(m.sqrt(0.1))**2) == True
   print("Test passé avec succès")
  test_flottants_egaux()

def pts_alignés():
  def pts(x1,y1,x2,y2,x3,y3):
    plat = True
    def distance(pointA,pointB): # calcule la distance entre 2 points
      distance = (pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2
      return distance
    def pythagore(): # cherche l'hypothénus en testant la quelle des 3 distances est la plus grande
      C = (x1,y1)
      D = (x2,y2)
      E = (x3,y3)
      CD = distance(C,D) # appelle la fonction distance pour la distance entre les cotés
      ED = distance(E,D)
      CE = distance(C,E)
      if CD < CE and ED < CE:
        dernier_coté = CE
        coté1 = CD
        coté2 = ED
      elif CD > CE and ED < CD:
        coté1 = CD
        dernier_coté = CD
        coté2 = ED
      elif ED > CE and ED > CD:
        coté1 = ED
        dernier_coté = ED
        coté2 = CE
      if m.sqrt(dernier_coté) - (m.sqrt(coté1) + m.sqrt(coté2)) <= 10**(-9) : # verifie si les points sonts alignés 
        plat = True
      else:
        plat = False
    return plat # renvoie true ou false en fonction du resultat
  
  assert pts(0.1,0.1,0.2,0.2,0.1+0.2,0.4-0.1) == True # les pts ne sont pas alignés
  print("les points sonts alignés !")
  assert pts(0.7,0.7,1.4,1.4,2.8,2.8) == True # les pts ne sont pas alignés
  print("les points sonts alignés !")
  assert pts(0.74,0.1,1.2,1.8,2.7,2.8) == True # les pts sont alignés
  print("les points ne sonts pas alignés !")

def triangle_rectangle():
  def pts(x1,y1,x2,y2,x3,y3):
    plat = True
    def distance(pointA,pointB): # calcule la distance entre 2 points
      distance = (pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2
      return distance
    def pythagore(): # cherche l'hypothénus en testant la quelle des 3 distances est la plus grande
      C = (x1,y1)
      D = (x2,y2)
      E = (x3,y3)
      CD = distance(C,D) # appelle la fonction distance pour la distance entre les cotés
      ED = distance(E,D)
      CE = distance(C,E)
      if CD < CE and ED < CE:
        dernier_coté = CE
        coté1 = CD
        coté2 = ED
      elif CD > CE and ED < CD:
        coté1 = CD
        dernier_coté = CD
        coté2 = ED
      elif ED > CE and ED > CD:
        coté1 = ED
        dernier_coté = ED
        coté2 = CE
      if dernier_coté - (coté1 + coté2) <= 10**(-9) : # verifie si le théoreme de pythagore fonctionne
        plat = True
      else:
        plat = False
    return plat # renvoie true ou false en fonction du resultat
  
  assert pts(0,0,0,1,1,4) == True # le triangle n'est pas rectangle
  print("le triangle est rectangle !")
  assert pts(7,7,7,5,5,9) == True # le triangle n'est pas rectangle
  print("le triangle est rectangle !")
  assert pts(8,0,1,1,97,4) == True # le triangle n'est pas rectangle
  print("le triangle n'est pas rectangle !")

serie_test()
print("----------------------")
pts_alignés()
print("----------------------")
triangle_rectangle()