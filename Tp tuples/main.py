from math import*

def milieu(pointA,pointB):
  print("le milieu :",(((pointA[0] + pointB[0]) / 2) , ((pointA[1] + pointB[1]) / 2)))

def distance(pointA,pointB):
  milieu(pointA, pointB)
  distance = (pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2
  return distance
def pythagore():
  C = (3,4)
  D = (1,7)
  E = (2,5)
  CD = distance(C,D)
  ED = distance(E,D)
  CE = distance(C,E)
  if CD < CE and ED < CE:
    dernier_coté = CE
    coté1 = CD
    coté2 = ED
  if CD > CE and ED < CD:
    coté1 = CD
    dernier_coté = CD
    coté2 = ED
  if ED > CE and ED > CD:
    coté1 = ED
    dernier_coté = ED
    coté2 = CE
  if dernier_coté == coté1 + coté2:
    print("le triangle est rectangle")
  else:
    print("le triangle n'est pas rectangle")
pointA = (int(input("x de A :")),int(input("y de A :")))
pointB = (int(input("x de B :")),int(input("y de B :")))
print("-------------------")
milieu(pointA, pointB)
print("-------------------")
distance = distance(pointA, pointB)
print("la distance :", sqrt(distance))
print("-------------------")
pythagore()