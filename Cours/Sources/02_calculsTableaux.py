notes = [12, 9.5, 14, 2]

print ("================")
print ("somme")
print ("================")
somme = 0
for n in notes :
    somme = somme + n

print ("somme :", somme)

print ("moyenne :", somme/len(notes))

print ("================")
print ("maximum version 1")
print ("================")
maxi = 0
for n in notes :
    if n > maxi:
      maxi =  n

print ("maxi :", maxi)

print ("================")
print ("maximum version 2")
print ("================")
maxi = notes[0]
for n in notes :
    if n > maxi:
      maxi =  n

print ("maxi :", maxi)


noms = ["moutoussamy","destouches","julan","najeus"]
for i in range(len(notes)):
    print(noms[i], notes[i])

maxi = notes[0]
imaxi = 0

for i in range(len(notes)):
    if notes[i]> maxi:
        maxi = notes[i]
        imaxi = i

print ("major", noms[imaxi])
