def afficher(tab):
    for e in tab :
        print(e)

def afficherPromo(noms, notes):
    for i in range(len(noms)) :
        print(noms[i], notes[i])

def calculerSomme(tab):
    somme = 0
    for e in tab :
        somme = somme + e

    return somme

def maximum(tab):
    maxi = tab[0]
    for e in tab :
        if e > maxi:
            maxi = e

    return maxi

def imaximum(tab):
    maxi = tab[0]
    imaxi = 0

    for i in range(len(tab)) :
        if tab[i] > maxi:
            maxi = tab[i]
            imaxi = i

    return imaxi




notes = [12, 9.5, 14, 2]
noms = ["moutoussamy","destouches","julan","naejus"]

print ("=============")
print ("Les noms")
print ("=============")
afficher(noms)

print ("=============")
print ("Les notes")
print ("=============")
afficher(notes)

print ("=============")
print ("La promo")
print ("=============")
afficherPromo(noms, notes)

print ("=============")
print ("La somme")
print ("=============")
somme = calculerSomme (notes)
print ("somme :", somme)

print ("=============")
print ("La moyenne")
print ("=============")
moyenne = somme / len(notes)
print ("moyenne :", moyenne)

print ("=============")
print ("La meilleure note")
print ("=============")
maxi = maximum(notes)
print ("maxi :", maxi)

print ("=============")
print ("Le major de promo")
print ("=============")
iMajor = imaximum(notes)

print ("major :", noms[iMajor])
