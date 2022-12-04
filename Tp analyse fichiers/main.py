import random
import os


def f_tout_lire(file_name):
  file = open(file_name, "r")
  print(file.read())
  file.close


def f_lire_Noctets(file_name):
  file = open(file_name, "r")
  nboctets = int(input("combien d'octets voulez vous lire ? : "))
  texte_octets = ""
  texte_octets = file.read(nboctets)
  print(texte_octets)
  file.close


def f_lire_ligne_complete(file_name):
  file = open(file_name, "r")
  nblignes = int(input("combien de lignes voulez vous lire ? : "))
  for loop in range(nblignes):
    print(file.readline())
    file.close


def f_lire_lignes_en_liste(file_name):
  file = open(file_name, "r")
  print("voici la liste : ", file.readlines())
  file.close


def new_file():
  if os.path.exists("patrick.txt"):
    os.remove("patrick.txt")
  name_new_file = "patrick.txt"
  new_file = open(name_new_file, "x")
  for loop in range(random.randint(2000, 5000)):
    txt = ""
    for loop in range(random.randint(80, 100)):
      txt = txt + str(chr(random.randint(0, 255)))
    new_file.write(txt)
    new_file.write("\n")


def printer_file():
  name_new_file = "TP_mon_fichier.txt"
  texte_final = open(name_new_file, "w")
  lettre_fin = input("choisir un caractere de fin :")
  a = 1
  texte = ""
  print("Merci d'ecrire ici la ligne", a, "de votre fichier :")
  ligne = input("Ecrire ici :")
  texte = texte + ligne + chr(10)
  while texte[-2] != lettre_fin:
    a += 1
    print("Merci d'ecrire ici la ligne", a, "de votre fichier :")
    ligne = input("Ecrire ici :")
    texte = texte + ligne + chr(10)
  print(
    "C'est bon vous pouvez ouvrir votre fichier", name_new_file,
    "avec un éditeur de texte. En attendant, voici le texte que vous avez écrit:"
  )
  texte_final.write(texte[0:len(texte) - 2])
  print(texte[0:len(texte) - 2])


def search_in_file(mota, file_name):
  file = open(file_name, "r")
  liste_pos = []
  texte = file.read()
  for a in range(len(texte)):
    verifsysteme = 0
    for b in range(len(mota)):
      try:
        if file[a + b].lower() == mota[b].lower():
          verifsysteme += 1
      except:
        pass
    if verifsysteme == len(mota):
      liste_pos.append(a)
    if a + b > len(texte):
      return liste_pos, len(liste_pos)
  return liste_pos, len(liste_pos)
  print("le mot", mota, "est apparu", nbapparition, "fois dans le programme.")
  file.close


def modif_file(mota, motb, file_name, liste_pos, apparitions):
  with open(file_name, "r+") as file:
    texte = file.read()
    liste_pos.reverse()
  for a in liste_pos:
    débuttexte = texte[0:a] + motb
    fintexte = texte[(a + len(mota)):len(texte)]
    texte = débuttexte + fintexte
  with open(file_name, "w") as file:
    file.write(texte)
    print("le mot", mota, "a été remplacé par le mot", motb, ".")


file_name = "essai_lecture_fichier.txt"
print("Voici les 4 façons de lire un fichier")
print("1 - D'un seul coup : ")
f_tout_lire(file_name)
print("------------------")
print("2 - Les N premiers octets : ")
f_lire_Noctets(file_name)
print("------------------")
print("3 - Une ligne complète : ")
f_lire_ligne_complete(file_name)
print("------------------")
print("4 - Sous forme de liste de lignes : ")
f_lire_lignes_en_liste(file_name)
print("------------------")
print("le fichier patrick.txt a été actualisé")
new_file()
print("------------------")
printer_file()
print("------------------")
mot_a_remplacer = input("quel mot voulez vous remplacer dans le fichier ? : ")
mot_remplacement = input("par quel mot voulez vous le remplacer ? : ")
liste_pos, nbapparition = search_in_file(mot_a_remplacer, file_name)
print("------------------")
modif_file(mot_a_remplacer, mot_remplacement, file_name, liste_pos,
           nbapparition)