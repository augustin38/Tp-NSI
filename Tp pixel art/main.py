from PIL import Image

def moyenne_pixel(x,y,tailleX,tailleY,img): #récupère la couleur moyenne d'une zone
  (newR,newV,newB)=(0,0,0)
  for i in range(0,tailleX):
    for j in range(0,tailleY):
      (rouge,vert,bleu) = img.getpixel((x+i,y+j))
      (newR,newV,newB)=(newR+rouge,newV+vert,newB+bleu)
  (newR,newV,newB)=(newR//(tailleX*tailleY),newV//(tailleX*tailleY),newB//(tailleX*tailleY))
  return newR,newV,newB

def replace_pixel(x,y,tailleX,tailleY,img,newR,newV,newB): #remplace tout les pixels d'une zone
  for i in range(0,tailleX):
    for j in range(0,tailleY):
      img.putpixel((x+i,y+j), (newR,newV,newB))

img = Image.open("astronaute_base.png") #initialisation du programme
(restX,restY) = img.size
restX_base, restY_base = restX, restY
tailleX = int(input("zone a pixeliser x ?"))
tailleY = int(input("zone a pixeliser y ?"))
x, y = 0, 0
contoursx = restX%tailleX
contoursy = restY%tailleY
while restY >= tailleY and restX >= tailleX : #répétition de la pixelisation pour la grande partie
  (newR,newV,newB) = moyenne_pixel(x,y,tailleX,tailleY,img)
  replace_pixel(x,y,tailleX,tailleY,img,newR,newV,newB)
  x = x + tailleX
  restX = restX - tailleX
  if restX < tailleX:
    y = y + tailleY
    restY = restY - tailleY
    restX = restX_base
    x = 0

x = 0   
if contoursx!=0: #répétition de la pixelisation pour la bordure du coté droit
  while restX>contoursx:
    newR,newV,newB = moyenne_pixel(x,y,tailleX,contoursy,img)
    replace_pixel(x,y,tailleX,contoursy,img,newR,newV,newB)
    restX = restX-tailleX
    x = x+tailleX

y = 0            
restY = restY_base
if contoursy!=0: 
  while restY>contoursy: #répétition de la pixelisation pour la bordure du bas
    x = restX_base - contoursx
    newR,newV,newB = moyenne_pixel(x,y,contoursx,tailleY,img)
    replace_pixel(x,y,contoursx,tailleY,img,newR,newV,newB)
    restY = restY-tailleY
    y = y+tailleY

x = restX_base-contoursx   
y = restY_base-contoursx
if contoursx!=0 and contoursy!=0: #répétition de la pixelisation pour le coin.
  newR,newV,newB = moyenne_pixel(x,y,contoursx,contoursy,img)
  replace_pixel(x,y,contoursx,contoursy,img,newR,newV,newB)
  
img.save("img_pixelisée.png") # sauvegarde de l'image