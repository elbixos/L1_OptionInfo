## Grandes lignes

def compteAllumettes(tab) :
    nbAllu = tab[0] + tab[1] + tab[2] + tab[3]
    return nbAllu

numJoueur = 1
plateau = [1,3,5,7]

while ( compteAllumettes(plateau) > 0 ) :
  numLigne, nbAllu = choisirStrategie(plateau)
  retirerAllumettes(plateau, numLigne, nbAllu)
  afficherPlateau(plateau)
  numJoueur = changerJoueur(numJoueur)

print ("le joueur ", numJoueur, "a gagne")
