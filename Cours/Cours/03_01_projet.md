### Cours 3 : Réalisation d'un vrai projet

#### Projet : Présentation et Méthodologie

#### Présentation du projet
Ici, on s'intéresse au **Jeu des Allumettes**.
- C'est un jeu à deux joueurs qui jouent chacun son tour.
- au départ les allumettes sont disposées comme suit :

|numéro de ligne | allumettes |
|---|---|
|0|I|
|1|III|
|2|IIIII|
|3|IIIIIII|

- A chaque tour, un joueur choisit une ligne et un nombre d'allumettes à retirer sur cette ligne (entre 1 et 3)
- le joueur qui retire la dernière allumette a perdu.

Il s'agit pour nous de faire un programme qui permette à deux joueurs humains de jouer sur l'ordinateur.

##### Méthodologie de développement du projet

Dans un tel projet, peut être trop complexe pour vous, il va néanmoins falloir commencer pour avancer. Le plus simple est de définir les grandes lignes du projet (notre stratégie).

Ensuite, nous transformerons ces grandes lignes en un programme principal et coderons toutes les fonctions utiles.

#### Grandes lignes
Ici, on se contente de décrire ce qui se passe dans une partie...
Nous traduirons ces grandes lignes en un programme principal plus tard.

```Markdown
1. Joueur départ : joueur 1
2. initialiser plateau

3. tant qu'il reste au moins une allumette
  - demander ligne et combien d'allumettes
  - retirer allumettes
  - afficher plateau
  - changer Joueur

4. afficherVainqueur
```

#### Transformation en programme principal.
Pour transformer proprement ces grandes lignes en un programme, je dois savoir quelles variables sont passées à toutes mes petites parties de programme.

La variable la plus importante est sans aucun doute l'état du plateau qui stocke quelles allumettes sont sur quelle ligne.
Une rapide reflexion montre que la seule information importante est le nombre d'allumettes présent sur chaque ligne. Je peux donc coder ceci avec un tableau de 4 entiers.
Mon initialisation du plateau peut donc s'écrire comme suit :

```python
plateau = [1,3,5,7]
```
Ensuite, je vais pour chaque action de mon plan, supposer l'existence d'une fonction qui fait ce qu'on lui demande et répond ce dont j'ai besoin.
Le code complet donnerait ceci :

```python
numJoueur = 1
plateau = [1,3,5,7]

while ( compteAllumettes(plateau) > 0 ) :
  numLigne, nbAllu = choisirStrategie(plateau)
  retirerAllumettes(plateau, numLigne, nbAllu)
  afficherPlateau(plateau)
  numJoueur = changerJoueur(numJoueur)

print ("le joueur ", numJoueur, "a gagne")
```
Ce code met en évidence des fonctions :
- *compteAllumettes* qui renvoie le nombre d'allumettes restantes
- *choisirStrategie* qui renvoie le nombre d'allumettes que l'utilisateur veut retirer et le numéro de ligne sur laquelle les retirer.
- *retirerAllumettes* qui retire effectivement ces allumettes.
- *afficherPlateau* qui affiche l'état du plateau actuel.
- *changerJoueur* qui fait la bascule entre joueur 1 et joueur 2.

Un grand intérêt doit être porté aux variables qui sont passées à chaque fonction et à l'enchainement des appels. Par exemple, *numLigne* est le numéro de ligne sur laquel le joueur veut retirer ses allumettes. Il a été choisi dans la fonction *choisirStrategie* et sera réutilisé par *retirerAllumettes*.

Quand chaque fonction aura été codée, tout le projet fonctionnera.

par exemple, coder (même salement) la fonction qui compte les allumettes peut se faire comme suit :
```python
def compteAllumettes(tab) :
    somme = tab[0]+tab[1]+tab[2]+tab[3]

    return somme
```
Ci nous faisons ce travail préalable, nous pouvons maintenant lancer une équipe de développeurs sur chaque fonction séparément, ils travailleront en autonomie.

Dans la pratique, cette approche est trop stricte. Sur cet exemple, je suis capable de définir une stratégie générale sans trop de difficulté, mais pour des projets très complexes, c'est parfois délicat.

**Ce que nous avons fait a surtout une valeur pédagogique** : Comprendre cette notion d'enchainement d'actions et de passage de variables. Oublions donc un peu ce que nous venons de faire pour repartir de l'étape des grandes lignes.

#### Méthodologie de développement réel
Un développeur un peu chevronné fait souvent le travail d'élaboration des grandes lignes dans sa tête. Si vous n'y arrivez pas, posez le sur un papier (ou dans un fichier).

Il définit ensuite la ou les variables dont il a le plus besoin. Pour nous, c'est clairement *plateau*, que j'ai vu comment définir en python :
```python
plateau = [1,3,5,7]
```

Puis il va élaborer directement une fonction parmi toutes celles à faire et la tester. Puis il s'intéressera a une autre fonction et à son chainage avec la première. Mais dans quel ordre ?
La règle standard est la suivante :
- les plus faciles d'abord
- les plus utiles pour les tests d'abord.

Notez qu'on ne finalisera peut être pas tout de suite ces fonctions, mais on les mettra dans un état permettant à notre projet d'avancer.

Ici, par exemple, la fonction par laquelle je commencerais serait clairement *afficherPlateau*. Celle ci est facilement testable et quand j'aurais fait les autres fonctions (retirer des allumettes, les compter,...), l'affichage pourra me permettre de comparer ce que je vois avec ce que calculent ces fonctions.

A votre niveau, une première version d'affichage pourrait être la suivante, avec son test :
```python
def afficherPlateau(tab) :
    print (tab)

plateau = [1,3,5,7]
afficherPlateau(plateau)
```
Cette version affiche tout le tableau. C'est moche...
A moindre coût, on peut faire la meme chose comme ceci, ce qui est toujours moche, mais j'ai fait une boucle et chaque tour de boucle (une **itération** de la boucle) sert à traiter une case du tableau, donc une ligne de mon plateau.
```python
def afficherPlateau(tab) :
    for i in range(len(tab)) :
        print (tab[i], end=" ")

    print("")

plateau = [1,3,5,7]
afficherPlateau(plateau)
```
Je peux améliorer mon affichage en créant une petite fonction responsable de l'affichage d'une ligne. Je lui donne un nombre entier et elle affiche autant de **I** que ce nombre avant de sauter à la ligne. Si je la code, je la teste dans la foulée.
```python
def afficherLigne(n) :
    for i in range(n):
        print("I", end = "")
    print("")

afficherLigne(4)
afficherLigne(2)
afficherLigne(-1)
```
Je peux chainer les deux fonctions : mon programme principal appelle la fonction *afficherPlateau* qui, pour chaque ligne, appelle la fonction *afficherLigne*. Et je teste le tout.
```python
def afficherLigne(n) :
    for i in range(n):
        print("I", end = "")
    print("")

def afficherPlateau(tab) :
    for i in range(len(tab)) :
        afficherLigne (tab[i])

plateau = [1,3,5,7]
afficherPlateau(plateau)
```
L'étape suivante consisterait :
1. à être capable de choisir un nombre représentant un numéro de ligne et un nombre d'allumettes...
2. retirer effectivement ces allumettes.
3. toutes les autres actions définies dans les grandes lignes
4. le bouclage sur un nouveau tour

Nous procèderons ainsi de proche en proche avec à chaque étape :
- un programme qui fonctionne
- un programme qui a été testé
- un programme qui s'approche de plus en plus de l'objectif

En cours, nous sommes allés un peu plus loin que ceci. Le résultat obtenu en cours est [ici](../Sources/03_vraiDev.py). Cela inclue la fonction qui demande au joueur quelle ligne / combien d'allumettes il veut retirer et la fonction qui retire effectivement ces allumettes du plateau.

Pour comprendre ces parties, ce n'est pas compliqué, il vous manque simplement une information : pour lire un entier que l'utilisateur entre avec le clavier :

1. On utilise la fonction *input()* qui renvoie ce que l'utilisateur a tapé au clavier sous forme d'une chaine de caractères (*string*)
2. On transforme cette chaine de charactères en entier avec la fonction *int*

ce qui donne ceci pour afficher le carré d'un entier choisi par l'utilisateur :
```python
print ("entrez un entier")
chaine = input()
monEntier = int(chaine)
print (monEntier**2)
```
ou en version courte
```python
print ("entrez un entier")
monEntier = int(input())
print (monEntier**2)
```

Voila...

### les fichiers
Les sources de tout ce que nous avons fait dans ce cours sont dans le répertoire [Sources](../Sources/).
On y trouvera en particulier :
- [Les grandes lignes](../Sources/03_plan.md)
- [le programme principal final](../Sources/03_TraductionPlan.py)
- [le développement pas à pas](../Sources/03_vraiDev.py)

### Exercices à faire
Vous **devez** être en mesure de faire les choses suivantes :
- Essayer de ré-écrire les grandes lignes sans regarder le modèle.
- refaire la traduction en un programme principal en comprenant pourquoi tout s'enchaine comme cela.

Mais vous ne pourrez pas le tester... vu que les fonctions manqueront.

Ensuite, vous **devez** être en mesure de :
- écrire tout seul la fonction *afficherLigne* et la tester
- écrire tout seul la fonction *afficherPlateau* et la tester
- écrire tout seul les fonctions contenues dans [ce fichier](../Sources/03_vraiDev.py) et les tester

Vous **devriez** essayer de faire les choses suivantes :
- ajouter toutes les fonctions utiles dans une version simple (par exemple, on ne vérifie pas si le numéro de ligne et le nombre d'allumettes choisis par le joueur sont valide)
- ajouter la boucle sur les tours de jeu.
- modifier la fonction d'affichage du plateau pour qu'elle affiche le numéro de ligne avant les allumettes, comme suit :
```
0: I
1: III
2: IIIII
3: IIIIIII
```
- modifier la fonction *choisirStrategie* pour qu'elle affiche un message incluant le numéro du joueur, tel que :
```
Joueur 2 :
Entrez un numéro de Ligne
```
il faudra sans doute modifier la fonction *afficherLigne* et peut être lui passer un paramètre supplémentaire.

Vous **pourriez** :
- Essayer de modifier le programme pour que les joueurs manipulent des numéros de ligne allant de 1 à 4 (et pas de 0 à 3). Notre programme, lui, continuera à stocker le nombre d'allumettes dans un tableau indexé de 0 à 3.
- Essayer de mettre en place la vérification du numéro de ligne et du nombre d'allumettes choisi par le joueur. Si ses choix sont non valides, on lui redemande...
