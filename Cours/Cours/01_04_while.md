### Les boucles *Tant que* (while)
Imaginons que je veuille écrire "bonjour à tous" 10 fois. Nous pouvons le faire en répétant 10 fois la ligne suivante :
```python
print ("bonjour à tous")
```
Mais c'est laid et peu efficace (si je veux changer le message en "au revoir à tous", il faudra que je fasse 10 modifications)

L'idée est de répéter une série d'instructions plusieurs fois. On parle d'une boucle (ici, une boucle Tant que ou **while**)

#### une premiere boucle infinie
Voici ce que l'on pourrait faire :
```python
a = 0
while (a == 0)
  print ("bonjour à tous")
  print ("Appuyez sur Ctrl C pour quitter")
```

Le déroulement est le suivant :
1. on initialise *a* à 0
2. on arrive sur la ligne du *while*. On teste si *a* est égal à 0. Si oui, on execute le code du bloc en dessous. Dans notre cas, *a* vaut bien 0.
3. on affiche "bonjour a tous"
4. on affiche "Appuyez"
5. le bloc d'instruction est terminé. On remonte à la ligne du while (comme en 2.) et on recommence (on boucle)

Dit autrement, on effectue des tous de boucle. Avant chaque nouveau tour, on vérifie si la condition est vraie (**True**) ou fausse (**False**)

Dans le cas de notre programme, vu que *a* ne change pas de valeur dans la boucle, nous allons boucler indéfiniment. Pour quitter une boucle infinie, suivez les instructions affichées par notre programme (Ctrl + c)

#### Une boucle qui compte les tours.
En modifiant un peu notre programme, on va se servir de *a* pour compter le nombre de tours que l'on fait...

```python
a = 0
while (a < 3):
  print ("bonjour à tous")
  print ("j'ai fait", a, "tours")
  a = a+1

print ("fin de la boucle")
```
Ici, à chaque tour de boucle, *a*, qui avait commencé à 0, est augmenté de 1. au bout de 3 tours, la condition *a<3* ne sera plus respectée et nous sortirons de la boucle pour afficher "fin de la boucle"

Nous verrons plus tard (ou vous chercherez) un autre célèbre type de boucle, la boucle **for** qui marche bien aussi, mais je n'en n'ai pas besoin pour le moment.

#### Exercices
Vous **devez** être en mesure de faire les exercices suivants :
1. faites un programme qui affiche les nombres entiers de 0 a 33

2. faites un programme qui affiche les nombres de 3 a 33

3. faites un programme qui calcule la somme des nombres de 0 à 33

4. faites un programme qui calcule la somme des inverses des nombres de 0 à 33

5. faites un programme qui calcule le produit des nombres de 1 à 33

4. faites un programme qui calcule le produit du carré des nombres de 1 à 33
