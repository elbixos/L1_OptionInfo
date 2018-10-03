
# Petit cours d'algorithmique et de python

# Auteur : Vincent Pagé : <vincent.page@univ-antilles.fr>


## Introduction

Dans ce cours, nous verrons les rudiments de l'algorithmique pour vos formations. Mon objectif est simple : ne pas focaliser sur les détails, mais vous permettre de faire des choses rapidement. Ce document est extrêmement synthétique. Il ne vous dispense pas d'aller en cours ni d'essayer de programmer vous même.

Pour plus de détails, vous pouvez me poser des questions et/ou chercher un peu sur le net ou dans des cours plus détaillés. Si vous ne voulez pas chercher, vous trouverez quelques liens vers ce type de ressources [ici](98_liens.md)

Les concepts présentés dans ce cours s'appliquent à la plupart les langages que je connais. Lorsque je devrais faire un vrai programme pour vous présenter quelque chose, je le ferais en **python**.

Le dépot dans lequel vous avez trouvé ce document contient également les exemples que nous avons vu en cours.

___
Vous pouvez repartir vers le [Sommaire](99_sommaire.md)
___


### Concepts d'algorithmique d'aujourd'hui.

Ceci est ma vision de la programmation actuelle. Tout le monde ne s'y retrouvera peut être pas, mais il me semble que la plupart des développeurs en entreprise seront d'accord avec le constat suivant :
Programmer (ou coder) fait appel à deux grands capacités :
- la stratégie
- la tactique

#### La stratégie

C'est, dans le domaine militaire, ce qui vous fait gagner une guerre (*si vous le faites bien et que vous avez de la chance*). C'est la planification vue de loin.

Les généraux, autour d'une table, décident d'envoyer tel bataillon à gauche, pendant que tel autre bataillon partira à droite pour prendre en sandwich l'armée adverse. Ils peuvent aussi planifier de faire un siège pour affamer l'armée ennemie, et quand ils auront faim, ils attaqueront.

#### La tactique
C'est, dans le domaine militaire, ce qui vous fait gagner une bataille (*si vous le faites bien et que vous avez de la chance*). C'est la planification vue de très près.

Le sergent, au coeur du champ de bataille, décide d'envoyer 2 hommes a gauche de la petite colline, pendant que ...

Les sergents font souvent de mauvais généraux, les généraux font souvent de mauvais sergents.

#### Quel rapport avec l'algorithmique et la programmation ?
Prenons un exemple plus ou moins simple : Vous souhaitez faire un programme qui reconnaisse le visage des différents étudiants de la promotion.

Plus précisément, nous devons faire un programme auquel on donne une image, et il doit retrouver le nom de l'étudiant correspondant.

Je vais supposer que nous disposons d'images des visage chaque étudiant de la promotion, associé à son nom.

La partie **Stratégie** c'est la définition des grandes étapes de mon programme. Pour l'exemple, on pourrait penser à quelque chose comme ceci :
lorsqu'on me donne un fichier image à reconnaitre, je vais :


1. lire l'image du fichier -> une image *inconnue*

2. lire l'ensemble de mes images connues -> *maBase*

3. pour chaque image de *maBase*

    3.1 Je mesure la distance de mon image *inconnue* a l'image connue -> dist

    3.2 Je retiens l'image connue ayant la plus distance *dist* -> *imageLaPlusProche*

4. J'annonce avoir reconnu l'étudiant dont le nom corresspond à *imageLaPlusProche*

Vous ne savez pas lire une image ? Ce n'est pas très grave (internet ou votre sergent le sait)

Vous ne savez pas définir une distance entre deux images ?  Raffinez votre stratégie. Par exemple, une solution classique (assez peu efficace, il faut reconnaître) consiste à calculer la somme des carrés des différences pixel à pixel entre les 2 images.

Tout ce travail n'est pas forcément fait par un informaticien.

La partie **tactique** c'est, pour une partie précise de mon programme, la réalisation d'un algorithme dans un langage donné.

Pour l'exemple, Si je dois faire cette somme des carrés ... je pourrais faire quelque chose comme ceci :

```python
  distance = 0;
  for x in range(len(image1.width) :
    for y in range()(image1.height)) :
      dist += (image1[x][y] - image2[x][y]) **2
```

Vous ne comprenez pas ce code ? c'est normal. Vous devriez en comprendre l'essentiel d'ici quelques cours.

La **tactique**, c'est de la programmation les mains dans le cambouis (*ou dans la boue si on conserve l'image du sergent*)

Les cours d'algorithmique focalisent souvent sur la tactique, alors que les langages actuels permettent d'en faire abstraction assez fréquemment. Par exemple, si je dois trier un tableau par ordre croissant, nous avons, dans tous les langages évolués, des fonctions pour le faire sans faire la moindre boucle.

La **stratégie**, est utile pour programmer mais aussi pour la coordination de n'importe quel projet que vous aurez à réaliser : vous aller choisir d'enchainer des actions, certaines requérant des résultats obtenus par des actions précédentes...

Ce cours a pour objectif de vous apprendre un peu de **tactique** (les variables, les boucles, les fonctions...) et beaucoup de **stratégie**.

Voyons donc le minimum de tactique à savoir pour commencer


### Les variables

Comprenons une chose tout d'abord : un programme informatique ne fait qu'une chose : il manipule des variables. Toutes les informations que doit gérer votre programme doivent donc se retrouver dans des variables. Vous en connaissez vraisemblablement quelques types simples de variables :
- les entiers (int)
- les nombres à virgules (float)
- les vrais ou faux (boolean)
- les chaînes de caractères (string)

Dans les variables, je stocke des valeurs.

```python
  a=5
  b=7
  print(a+b)
```
j'ai créé une variable *a*, lui ai donné la valeur 5, puis crée une variable *b*, lui ai donné la valeur 7,
puis affiché le résultat de la somme des valeurs des deux variables.
### Les tests conditionnel (*if*)
Une grande partie de l'algorithmique consiste a dire ce que l'on fait dans tel ou tel cas. Au coeur de tout ceci se trouve le test conditionnel.
Ici, on fait un programme qui compare la valeur de *a* avec celle de *b*. Si *a* est plus petit, on écrit qu'il est plus petit, sinon, on écrit qu'il est plus grand. Enfin, notre programme continuera à écrire des inepties. Voici la syntaxe en python :

```python
if a < b :
    print ("a est plus petit")
    print ("mais il est vaillant")
else :
    print ("a est plus grand ou égal")

print ("la taille importe peu")
```
Notez le décalage horizontal qui signale ce qui est dans le if, et ce qui ne l'est pas. "Ce qui est dans le if" est appelé **un bloc d'instructions**.

En python, il est décalé (on dit **indenté**) et il y a deux points avant...

Eventuellement, il pourrait être intéressant d'avoir 3 cas :
- *a* < *b*
- *a* > *b*
- *a* = *b*

La solution consisterait à imbriquer des *if* ou a utiliser *elif* (cherchez sur le net, on le verra en cours mais je ne vais pas surcharger ce support)

#### Exercices
Vous **devez** être en mesure de faire les exercices suivants :

1. faites un programme qui demande à l'utilisateur un entier *a* et affiche un message adapté si l'on est dans l'un des deux cas suivants

   - a < 10

   - a >= 10

2. faites un programme qui demande à l'utilisateur son nom *nom* et affiche :

  - "Bienvenue mr page" si le nom est "page"

  - "Sortez d'ici" dans les autres cas

3. faites un programme qui demande à l'utilisateur un entier *a* et affiche un message adapté si l'on est dans l'un des trois cas suivants

      - a = 10

      - a < 10

      - a > 10

4. faites un programme qui demande à l'utilisateur un entier *a* et affiche un message adapté si l'on est dans l'un des 4 cas suivants

      - a <= -3

      - -3 < a < 0

      - 0 < a < 2

      - 2 <= a


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


### Les fonctions.
Le code que j'ai présenté juste avant est le **programme principal**. C'est ce que fait mon programme.

Un vrai bon programme découpe le code en petites actions que le programme principal organise. Ces petites actions seront des fonctions.

Programmer en utilisant des fonctions va nous permettre de
- simplifier notre programme principal
- limiter les risques d'erreur
- simplifier l'évolution de mon programme.

#### Création d'une fonction
Commençons par un exemple simple : un programme qui affiche 3 fois "bonjour" et le nombre de tours faits.
```python
i = 0
while (i < 3):
  print ("bonjour à tous")
  i = i+1
```
Je vais créer une fonction qui devra effectuer cette action. ma fonction s'appellera *affiche3FoisBonjour*
```python
def affiche3FoisBonjour():
    i = 0
    while (i < 3):
      print ("bonjour à tous")
      i = i+1
```
Cette fonction est comparable à un ouvrier spécialisé que l'on appelle chaque fois que l'on veut qu'il travaille.

Pour l'appeler, mon **programme principal** va utiliser son nom, sans oublier les parenthèses, comme suit :
```python
affiche3FoisBonjour()
```

Je peux appeler ma fonctions plusieurs fois au besoin :
```python
def affiche3FoisBonjour():
    i = 0
    while (i < 3):
      print ("bonjour à tous")
      i = i+1


affiche3FoisBonjour()
affiche3FoisBonjour()
```
le code ci dessus définit la fonction puis le **programme principal** l'appelle 2 fois.

Pour préparer la section suivante, je vais ré-écrire le code précédent en entrant le nombre de fois ou j'écris le message dans une variable :

```python
def affiche3FoisBonjour():
    n=3
    i = 0
    while (i < n):
      print ("bonjour à tous")
      i = i+1


affiche3FoisBonjour()
affiche3FoisBonjour()
```
Le programme fait exactement la même chose qu'auparavant.

#### Passage d'un paramètre à une fonction
Le gros intérêt des fonctions est la possibilité de les paramétrer.

Si mon programme doit afficher un certain nombre de fois "bonjour a tous", il faudrait que le **programme principal** puisse dire à la fonction quelle valeur on veut donner à sa variable *n*

Le problème est que les fonctions travaillent avec des variables que elles seules connaissent (on parle de **variables locales**). Donc le programme principal ne connait pas la variable *n* de la fonction. Il faut donc établir une communication entre le programme principal et la fonction.

On dit qu'on **passe un argument à la fonction**. Ceci se fait comme suit :
```python
def afficheNFoisBonjour(n):
    i = 0
    while (i < n):
      print ("bonjour à tous")
      i = i+1


afficheNFoisBonjour(5)
```
Mon programme principal dit *5* à la fonction. La fonction récupère ce *5* et le met dans sa variable *n* (entre les parenthèses) et peut faire ce qu'on lui demande.

Notez que ma fonction s'appelle maintenant *afficheNFoisBonjour* vu qu'elle est paramétrable. Changez la valeur (ici *5*) passée a la fonction et ré-executez le code. Observez que ma fonction sait maintenant faire beaucoup plus de choses qu'avant.

#### Passage de plusieurs paramètres à une fonction
Je vais encore modifier ma fonction pour qu'elle affiche plusieurs fois un message variable quelconque.

Vu de la fonction, le message à afficher sera également une variable *message*, que le programme principal lui communiquera.

```python
def afficheNFoisTruc(n,message):
    i = 0
    while (i < n):
      print (message)
      i = i+1


afficheNFoisTruc(5, "bonjour")
afficheNFoisTruc(3, "au revoir")
```
Lors de l'appel de la fonction par le programme principal, celui ci donne maintenant 2 informations à la fonctions (2 arguments) : le nombre et le message. C'est l'ordre qui détermine dans quelle variable finit la valeur passée par le programme principal.

Ainsi, dans le programme qui précède :
- au premier appel, le 5 atterrit dans la variable *n* de la fonction et "bonjour" dans la variable *message* de la fonction.
- au second appel, le 3 atterrit dans la variable *n* de la fonction et "au revoir" dans la variable *message* de la fonction.

Au final, mon programme affiche donc 5 fois "bonjour" puis 3 fois "au revoir"

#### Valeur de retour d'une fonction
Les fonctions que nous avons vues font des choses a partir des informations que leur donne le programme principal.

Comment faire si maintenant ces fonctions doivent communiquer des informations au programme principal ?

Par exemple, si je dois faire une fonction qui fait la somme de deux nombres :

```python
def somme(a,b):
    resu = a +b

somme (3,5)
```
ma fonction calcule bien la somme de *a* et *b* et met le résultat dans resu. Le programme principal fournit les valeurs de *a* et de *b* lors de l'appel, mais il ne peut pas utiliser le résultat calculé car **resu** est locale à la fonction.

Il faut que la fonction *réponde* au programme. On dit qu'elle **retourne une valeur** au programme.
Cela se fait avec le mot clef **return**.

```python
def somme(a,b):
    resu = a +b
    return resu

resultat = somme (3,5)
print(resultat)
```
Dans ce qui précède la fonction calcule *resu* le renvoie au programme principal.
Le programme principal récupère ce résultat et le place dans la variable *resultat*. On peut ensuite l'afficher.

Tout se passe comme si l'appel de la fonction était remplacé par la valeur que la fonction renvoie.

#### Exercices
Vous devez être capables de faire ce qui suit :

- faire une fonction qui calcule le produit des nombres entiers de 1 à *n* et l'appeler pour que le programme principal affiche la somme. *n* sera fixé par l'utilisateur du programme.

- reprendre **tous** les exercices des sections précédentes pour les transformer en fonctions que le programme principal utilise.
## Cours 2 : Tableaux

### intérêt
Avec les types de variables que nous avons vus dans le cours précédent, nous pouvons faire beaucoup de choses, mais cela devient vite pénible.

Imaginons que je doive faire un programme qui gère vos notes, je doiS stocker une note (un float) par étudiant. Je pourrait par exemple choisir un ordre pour rentrer les notes et stocker la note de chaque étudiant dans une variable.
Disons que ma classe ne contient que 3 étudiants.

```python
e1 = 12
e2 = 9.5
e3 = 14
```
Pour calculer la moyenne de ma promotion, je pourrais ajouter ceci au code qui précède :
```python
moyenne = (e1+e2+e3) / 3
print (moyenne)
```

Si finalement, je dois ajouter un 4eme étudiant arrivé en retard, mon code est transformé à de multiples endroits pour devenir :
```python
e1 = 12
e2 = 9.5
e3 = 14
e4 = 2 # oui, il est mauvais, en plus

moyenne = (e1+e2+e3+e4) / 4
print (moyenne)
```
A chaque ajout d'étudiant, il faudra que je pense à faire toutes les modifications. A terme, je suis sûr de faire une erreur...

De plus, dans le cas de votre promotion, il me faudrait une vingtaine de variables, ce qui devient lourd et pénible. Il est temp d'introduire les tableaux. En python, on les appelle des *listes*, mais c'est sans importance pour nous.

Voici ce que je voudrais : une seule variable contenant ces informations, rangées dans des cases séparées.

| notes |
|---|
|12|
|9.5|
|14|
|2|

Ici, *notes* est le nom de mon tableau.
L'intérêt est simple : si j'ajoute un étudiant, j'ajoute juste une case à mon tableau. **Mes notes ne sont contenues que dans une seule variable** : *notes*

Je peux créer un tableau de ce type comme ceci
```python
notes = [12, 9.5, 14, 2]
print(notes)
```
Pour accéder à une case, je vais utiliser son numéro (on parle d'*indice* de la case). Les indices commencent à 0. Une bonne représentation de mon tableau serait la suivante :

indice | valeur
---|---
0|12
1|9.5
2|14
3|2

Si je veux accéder à la case numéro 2, j'utiliserais l'écriture suivante : notes[2]

Le code suivant :
- affiche la valeur de la case 2 (qui vaut 14)
- modifie la valeur de la case 3 pour y mettre la valeur 11
- affiche tout le tableau

```python
print (notes [2])
notes[3] = 11
print(notes)
```

### Manipulations de base sur les tableaux

#### Création d'un tableau
Pour créer un tableau, on peut le créer déja rempli, comme nous l'avons fait. Nous aurions pu également créer un tableau vide et le remplir quand nous voulons (ce qui permettrait d'ajouter des étudiants à n'importe quel moment)

Ce qui suit crée un tableau vide, et le remplit avec des chaines de caractères contenant les noms de chaque étudiant de ma promo.
```python
noms = []

print (noms)

noms.append("moutoussamy")
noms.append("destouches")
print (noms)

noms.append("julan")
print (noms)

noms.append("naejus")
print (noms)
```
#### longueur d'un tableau
il peut être utile de connaitre le nombre de cases d'un tableau nommé *tab* : on l'obtient avec la fonction *len*
```python
nbEtudiants = len(noms)
print (nbEtudiants)
```

#### parcours de tableaux
Si je veux afficher le contenu de chaque case du tableau de notes, je peux utiliser print(notes).
Ici, je vais le faire d'une autre manière, que je réutiliserais de plusieurs façons différentes utilisant toutes la notion de parcours de tableau.
Cela me permettra de faire des choses plus compliquées plus tard (comme calculer la moyenne ou trouver le nom du major de promo).

Si je veux afficher le tableau, ce que je veux faire est en fait afficher successivement le contenu de chaque case.

Je vais donc visiter chaque case du tableau afficher le contenu de la case en cours.

Nous allons voir 3 façon de le faire, chacune ayant ses intérêts (surtout les 2 dernières en fait)

#### parcours d'un tableau avec une boucle while.
je peux le faire comme suit avec la boucle *while* vue dans le cours précédent :
```python
notes = [12, 9.5, 14, 2]

i = 0
while i<4 :
    print(notes[i])
    i = i+1
```
Mais ceci ne marche que pour un tableau de 4 cases. Je peux améliorer ceci facilement en modifiant légèrement mon code en prenant en compte la taille du tableau.

```python
notes = [12, 9.5, 14, 2]

i = 0
while i<len(notes) :
  print(notes[i])
  i = i+1
```
C'est fonctionnel mais peu sympathique à écrire. Voyons une version plus pratique.

#### parcours d'un tableau avec une boucle for.
```python
notes = [12, 9.5, 14, 2]

for e in notes :
  print (e)
```
Dans ce type de boucle, à chaque tour de boucle, la variable *e* va prendre la valeur du contenu de la case visitée. le *for* se débrouille tout seul pour se promener de case en case.

Le code précédent se lit quasiment comme en francais : pour chaque *e* dans le tableau *notes*, j'affiche *e*

Vous choisissez le nom que vous donnez à la variable qui visite les cases. Le nom du tableau (après *in*) est celui que vous avez donné à votre variable contenant le tableau. Je pourrais tout aussi bien écrire :
```python
notes = [12, 9.5, 14, 2]

for biten in notes :
  print (biten)
```
C'est la version la plus simple pour parcourir tout tableau.

#### parcours avec une boucle for et l'indice de la case
il peut arriver que j'ai besoin de me déplacer dans mon tableau en utilisant le numéro des cases du tableau. C'est ce que nous allons essayer de faire ici...

Commençons par ce code. Vous devriez vite comprendre qu'il affiche les chiffres de 0 à 3.
```python
indices = [0,1,2,3]

for i in indices :
  print (i)
```

Je peux me servir de ce *i* variable pour afficher le contenu de la case numéro *i* d'un tableau, comme ceci :
```python
for i in indices :
  print (notes[i])
```
Le problème est que je dois définir manuellement le tableau indice. Ce qui est pénible, si mon tableau a de nombreuses cases.
Pour générer un tableau allant de 0 à n-1, nous disposons de *range(n)*.
```python
indices  = range(4)
for i in indices :
  print (notes[i])
```
ou encore
```python
for i in range(4) :
  print (notes[i])
```
Mais ceci ne fonctionne que pour des tableaux de 4 cases. Il suffit d'intégrer la longueur du tableau à mon code et c'est réglé :

```python
for i in range(len(notes)) :
  print (notes[i])
```
#### Quelques exemples
Si vous avez compris ces parcours, au lieu d'afficher simplement le contenu de chaque case, nous allons pouvoir faire des choses plus complexes.

##### Somme des éléments d'un tableaux
Pour faire la somme des éléments d'un tableau, il me suffit d'avoir une variable *somme* qui vaudra 0 au départ, et que je vais augmenter au cours de mon parcours de la valeur de chaque case visitée.

N'importe quel parcours parmi les 3 précédents fonctionne, je vais prendre le plus simple.
```python
notes = [12, 9.5, 14, 2]

somme = 0
for n in notes :
    somme = somme + n

print ("somme :", somme)
```
A moindre frais, je peux aussi calculer la moyenne en ajoutant la ligne qui suit :
```python
print ("moyenne :", somme/len(notes))
```

##### recherche du maximum d'un tableaux
Si je cherche le maximum de mon tableau, il suffit que je dispose d'une variable *maxi* qui vaut, disons 0. Je parcours mon tableau et chaque fois que je vois quelque chose de plus grand que ce que j'ai déja vu, mon *maxi* est mis à jour.

Quelque chose comme ceci.
```python
notes = [12, 9.5, 14, 2]

maxi = 0
for n in notes :
    if n > maxi:
      maxi =  n

print ("somme :", somme)
```
Avec un peu d'expérience, je peux me méfier de la ligne qui dit *maxi = 0*. En effet si mon tableau ne contient que des éléments négatifs, aucune case ne va déclencher mon *if*. Par conséquent, a la fin de la boucle, le maximum de mon tableau sera resté à zéro, alors que tous les éléments sont négatifs...
De fait, il vaut mieux initialiser mon maxi à la valeur de la premiere case du tableau, comme suit :

maxi = notes[0]
for n in notes :
    if n > maxi:
      maxi =  n

print ("maxi :", maxi)

##### parcours de 2 tableaux conjoints
Bon. Imaginons que je veuille maintenant gérer aussi les noms de mes étudiants.
Je pourrais stocker le nom des étudiants dans un tableau de chaînes de caractères.
```python
noms = ["moutoussamy","destouches","julan","naejus"]
```
L'idée est que l'étudiant dont le nom est dans la case numéro 2 du tableau *nom* a eu la note contenue dans la case numéro 2 du tableau *notes*

Si je souhaite afficher les noms et les notes de ma promotion : je vais me déplacer de case en case en utilisant un indice variant de 0 à 3. Pour chaque indice, j'affiche la case correspondante dans le tableau des noms et la case correspondante dans le tableau de notes.

```python
noms = ["moutoussamy","destouches","julan","naejus"]
for i in range(len(notes)):
    print(noms[i], notes[i])
```
Cela commence a ressembler a quelque chose !
Voyons si l'on peut compliquer un tout petit peu.

##### affichage du nom du major
Pour afficher le nom du major de promo, c'est relativement simple : je vais chercher le numéro de la case contenant le maximum du tableau de notes.
Je peux alors afficher le nom situé dans la case correspondante dans le tableau de noms.

Pour trouver la position du maximum : on veut retenir la valeur du maximum, mais aussi sa position. On aura donc ces variables à mémoriser.

Lors du parcours du tableau, chaque fois que je mets a jour mon maximum, je met également à jour sa position.

```python
maxi = notes[0]
imaxi = 0

for i in range(len(notes)):
    if notes[i]> maxi:
        maxi = notes[i]
        imaxi = i

print ("major", noms[imaxi])
```

##### Nettoyage et mise en fonctions.
Pour avoir du code propre il est toujours recommandé de coder en utilisant des fonctions.

Chacune des petites actions que j'ai faites va donc être déplacée dans une fonction spécifique. A dire vrai, j'aurais tendance à le faire au fur et à mesure. Ici, et c'est la dernière fois de l'année, je le fais à la fin du chapitre pour ne pas tout mélanger.

En se souvenant de ce qui a été fait dans le cours précédent sur les fonctions, vous devriez pouvoir comprendre ce qui suit, qui reprend la totalité de nos travaux, mais proprement.

```python
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

afficher(noms)
afficher(notes)

afficherPromo(noms, notes)

somme = calculerSomme (notes)
print ("somme :", somme)

moyenne = somme / len(notes)
print ("moyenne :", moyenne)

maxi = maximum(notes)
print ("maxi :", maxi)

iMajor = imaximum(notes)

print ("major :", noms[iMajor])
```
### les fichiers
Les sources de tout ce que nous avons fait dans ce cours sont dans le répertoire [Sources](../Sources/index.md).
On y trouvera en particulier :
- [L'intro sur les tableaux](../Sources/02_tableaux.py)
- [Les parcours de tableaux](../Sources/02_parcoursTableaux.py)
- [Les exemples de calcul](../Sources/02_calculsTableaux.py)
- [La version finale](../Sources/02_finalTableaux.py)
## Quelques liens externes

Le problème quand on enseigne l'informatique (ou quoi que ce soit d'autre), est d'adapter son discours a son public. Ce que je propose dans ce cours est un kit de survie pour l'algorithmique et la programmation utile pour tout ingénieur.

J'y fais d'énormes raccourcis.
Si vous souhaitez aller un peu plus loin voici quelques liens que j'ai glané sur internet.

### Un tutoriel pour se former :

Si vous souhaitez des informations plus détaillées, d'autres exemples, des exercices à faire, voici
 [un tutoriel](https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python)
 Je vous conseille de faire tout le début, vous pourrez vous arrêter quand vous voudrez.

### Le tutoriel officiel :
Vous voulez quelque chose de plus rigoureux, toujours sous forme de tutoriel ? Voici [un autre tutoriel](https://docs.python.org/fr/3/tutorial/index.html)
Il est bien aussi, mais il suppose souvent que vous travaillez sous Linux et/ou que vous ayez quelques bases en informatique...

### Un cours :
Vous souhaitez un gros pdf avec tout ce qu'on peut vouloir savoir sur python ? Voici [un gros cours](https://inforef.be/swi/download/apprendre_python3_5.pdf)
J'aurais tendance à louer son côté très complet, tout en lui reprochant de ne pas être ...synthétique...  

### Autres ressources
Si vous trouvez d'autres ressources utiles, n'hésitez pas à m'en faire part, je pourrais les ajouter...

___
Vous pouvez repartir vers le [Sommaire](99_sommaire.md)
___
