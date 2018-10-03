notes = [12, 9.5, 14, 2]

print ("===============")
print ("boucle while")
print ("===============")
i = 0
while i<4 :
    print(notes[i])
    i = i+1

print ("===============")
print ("boucle while et len")
print ("===============")
i = 0
while i<4 :
    print(notes[i])
    i = i+1

print ("===============")
print ("boucle for")
print ("===============")

for e in notes :
    print (e)

print ("===============")
print ("Affichage des indices")
print ("===============")
indices = [0,1,2,3]

for i in indices :
  print (i)

print ("===============")
print ("boucle for et indices version 1")
print ("===============")
for i in indices :
  print (notes[i])

print ("===============")
print ("boucle for et indices version 2")
print ("===============")
indices  = range(4)
for i in indices :
  print (notes[i])

print ("===============")
print ("boucle for et indices version 3")
print ("===============")
for i in range(4) :
  print (notes[i])

print ("===============")
print ("boucle for et indices version finale")
print ("===============")
for i in range(len(notes)) :
  print (notes[i])
