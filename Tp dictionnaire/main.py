file = open("texte_TP.txt","r",encoding="utf-8")
texte = file.read()
texte = texte.replace("."," ")
texte = texte.replace(","," ")
texte = texte.replace(":"," ")
texte = texte.replace(";"," ")
texte = texte.replace("!"," ")
texte = texte.replace("?"," ")
texte = texte.replace("le"," ")
texte = texte.replace("la"," ")
texte = texte.replace("les"," ")
texte = texte.replace("de"," ")
texte = texte.replace("des"," ")

for caractere in texte:
  if ord(caractere)>= 65 and ord(caractere)<= 90:
    texte = texte.replace(caractere,chr(ord(caractere)+32))

texte_split = texte.split()
dico = {texte[0]:1}

for loop in range(1,len(texte_split)):
  if texte_split[loop] in dico:
    dico[texte_split[loop]] += 1
  else:
    dico[texte_split[loop]] = 1

mot_max = 0
for mot in dico:
  if dico[mot] > mot_max:
    mot_most = mot
    mot_max = dico[mot]
print(dico)
print("le mot le plus frequent est ", mot_most ,"avec", mot_max ,"apparitions")