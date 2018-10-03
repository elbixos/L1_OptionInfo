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
- les vrais ou faux (booleen)
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


### les fichiers
Les sources de tout ce que nous avons fait dans ce cours sont dans le répertoire [Sources](../Sources/index.md).
On y trouvera en particulier :
- [variables / tests / while](../Sources/01_intro.py)

- les exemples sur les fonctions dans les fichiers dont le nom commence par **01_0** dans le repertoire [Sources](../Sources/index.md)

___
Vous pouvez repartir vers le [Sommaire](99_sommaire.md)
___
