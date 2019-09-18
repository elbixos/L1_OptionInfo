
def saisirNoms():
    noms = ["Chery", "Niddam", "Mauline", "Geneix"]

    return noms

def saisirNotes(noms):
    n = len(noms)

    notes = []
    for i in range(n):
        print ("Entrez la note de", noms[i])
        saNote = input()
        saNote  = float(saNote)
        notes.append(saNote)


    return notes

def afficherPromo(noms, notes):
    print (noms)
    print (notes)

def calculMoyenne(notes):
    n = len(notes)

    somme = 0
    for i in range(n):
        somme = somme + notes[i]

    return somme / n


    return moyenne

def trouverMax(tab):
    imax = 0
    maxi = tab[0]

    n = len(tab)

    for i in range(n):
        if tab[i] > maxi:
            maxi = tab[i]
            imax = i
    return imax


def trouverMajor(noms, notes):
    i = trouverMax (notes)
    major = noms[i]
    return major

promo = saisirNoms()

notes = saisirNotes(promo)

afficherPromo(promo, notes)

moy = calculMoyenne(notes)

nomMajor = trouverMajor(promo, notes)

print ("Dans cette promo la moyenne est ", moy, "et le boss est ", nomMajor)
