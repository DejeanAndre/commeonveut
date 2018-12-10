
"""
ville = ["Cayenne", "Kourou", "Sinnamary", "Iracoubo", "St Laurent", "Remire Montjoly", "Roura"]
ville.append("Kaw")
"""
#Afficher une liste
"""
for f in ville:
  print f
"""
#Calcul la taille d'un tableau
"""
i=0
while i < len(ville):
    print ville [i]
    i += 1
"""

# Demander de saisir un nom
def SayHello(name):
    if name:
        print("Hello " + name)
    else:
        name = raw_input("Vous n'avez pas saisi de nom, merci d'en saisir un: ")
        SayHello(name)
SayHello('')
