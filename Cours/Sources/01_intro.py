a = 5
b = 6
print(a+b)

print ("a", a)
print ("b", b)

if a < b :
    print ("a est plus petit")
else :
    print ("a est plus grand ou égal")


## décommentez ce qui suit donne une boucle infinie...
# a = 0
# while (a == 0):
#   print ("bonjour à tous")
#   print ("Appuyez sur Ctrl C pour quitter")

a = 0
while (a < 3):
  print ("bonjour à tous")
  print ("j'ai fait", a, "tours")
  a = a+1

print ("fin de la boucle")
