## Grandes lignes
def afficherLigne(n) :
    for i in range(n):
        print("I", end = "")
    print("")

def afficherPlateau(tab) :
    for i in range(len(tab)) :
        afficherLigne (tab[i])

def compteAllumettes(tab) :
    somme = 0
    for e in tab :
        somme = somme + e

    return somme

def retirerAllumettes(tab, numLigne, nb) :
    tab[numLigne] = tab[numLigne] - nb


def choisirStrategie(tab) :
    print ("Entrez un numéro de Ligne")
    numLigne = input()
    numLigne = int(numLigne)

    print ("Entrez un nombre d'allumettes")
    nb = input()
    nb = int(nb)

    return numLigne, nb


plateau = [1,3,5,7]

#afficherLigne(3)
#afficherLigne(2)

afficherPlateau(plateau)

num, nb = choisirStrategie(plateau)
retirerAllumettes(plateau, num,nb)


afficherPlateau(plateau)
print (plateau)
#print (compteAllumettes(plateau))
