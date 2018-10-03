

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
