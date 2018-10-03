

### 2. Sortir du jeu
Je n'ai ajouté que quelques lignes de code dans le programme précédent.
Essayez de les repérer avant de passer à la suite,
je vais les analyser avec vous.

L'objectif, je vous le rappelle, est de pouvoir
sortir de notre programme quand l'utilisateur
appuie sur la touche *Escape* de son clavier
ou quand il clique sur le bouton *fermer*
de la fenêtre de notre programme.

Ceci ce produit alors que notre fenêtre est déja ouverte, donc au coeur de notre boucle *while*

#### Traitement des touches enfoncées.

le premier bloc de nouveautés est le suivant et concerne la détection d'un appui sur la touche *Escape*.

```python
# on recupere l'etat du clavier
touches = pygame.key.get_pressed();
```
*key.get_pressed()* est une fonction de pygame. Son nom m'indique plus où moins à quoi elle sert : Elle va me répondre quelles touches du clavier sont enfoncées au moment où je l'appelle.
Ma ligne met le résultat dans une variable que j'ai nommé *touches*

Pour traiter le cas qui m’intéresse (quand la touche *Escape* est enfoncée), il faut connaître la tête de ma variable *touches*. La doc de pygame peut nous renseigner là dessus et en voici une explication très brève.

La réponse de la fonction *key.get_pressed()* est un tableau de booléens (des variables vraies ou fausse, True ou False en python). Chaque case du tableau est une touche du clavier. La valeur d'une case est *True* si la touche est enfoncée et *False* si la touche n'est pas enfoncée au moment de l'appel.

Le tableau peut être représenté comme suit

| indice | valeur |
|---|---|
|0|False|
|1|False|
|...| False|
|42| True |
|...|False|
|63|True|
|...|False|

Ici, on voit que les touches numéro 42 et 63 étaient
les seules enfoncées au moment ou l'appel de la fonciton a été fait.

Il ne me reste plus qu'a regarder les touches qui m'intéressent. Si je sais que la touche *ESC* porte le numéro 43, je pourrais faire quelque chose comme :
```python
if touches[43] == True:
  print "Vous avez appuyé sur Escape"
```
Mais les développeurs ne veulent pas apprendre par coeur le numéro des touches. Pygame leur fournit donc une assistance. Le numéro de la touche *Esc* est par exemple contenu dans une constante nommée *K_ESC*.
Le code précédent deviendrait donc :
```python
if touches[pygame.K_ESC] == True:
  print "Vous avez appuyé sur Escape"
```
Voici une petite liste de ces constantes :

- K_ESCAPE : la touche escape.
- K_RETURN : la touche d'entrée.
- K_SPACE : vous savez
- K_A : la touche A
- K_LEFT : la touche "flêche de gauche"

--------------

Adaptons ceci a notre cas...
Ce qui nous intéresse est, lorsque la touche Escape est enfoncée, de quitter la boucle.

Plus précisément, quand la touche Escape est enfoncée, **nous n'allons pas instantanément quitter la boucle**. Nous arrêterons la boucle au début du prochain tour (on parle de **la prochaine itération**).

Pour cela, il suffit de rendre faux le test du *while*. Nous mettrons donc *continuer* à une valeur différente de *0*.

Ceci explique le second bloc de nouveauté dans le fichier, présenté ci-dessous

```python
# si la touche ESC est enfoncee, on sortira
# au debut du prochain tour de boucle
if touches[pygame.K_ESCAPE] :
    continuer=0
```

*Remarque : juste ces modifications ne donneront pas un programme fonctionnel pour des raisons que je ne détaillerais pas ici. Il faudra ajouter la suite pour que l'ensemble fonctionne. Si cela vous intéresse, demandez moi, mais vous pouvez vivre sans le savoir.*

Occupons nous maintenant du bouton de fermeture de l'application.

#### Traitement du bouton QUIT

Il me faut ici vous parler du fonctionnement général de l'ordinateur lorsque l'on utilise des interfaces graphiques.

Nous attendons ici que notre programme réagisse à une action. Néanmoins, nous sommes ici très loin de l'attente de l'entrée d'un entier au clavier, car :

- nous ne savons pas quand cette action va se produire.
- notre programme ne doit pas être bloqué pendant l'attente.


Quand vous déplacez la souris, cliquez quelque part (ou même appuyez sur une touche du clavier), la seule entité qui soit au courant de cette action est votre système d'exploitation (votre **OS**, qui peut être Windows, Mac OS ou un Linux ou ...)

Prenons l'exemple d'un clic souris :

Votre **OS** sait quelle est l'application qui se trouve sous l’événement (il gère le positionnement de vos fenêtres sur votre écran).

Il va donc envoyer un message à l'application concernée.
Ce message, correspondant à une action faite par
l'utilisateur est appelé un **événement**.

Un programme qui utilise une interface graphique doit donc gérer ces événements.

un événement a plusieurs propriétés :
- un **type**. Voici quelques exemples :

  - Mouse_down : le bouton de gauche de la souris a été enfoncé.

  - Mouse_up : le bouton de gauche de la souris a été enfoncé.

  - Mouse_move : la souris a bougé

  - Key_down : une touche a été enfoncée


- des valeurs utiles :

  - pour un Mouse_up, il nous faut sa position.

  - Pour un Key_down, il nous faut savoir quelle touche est concernée

Dans notre cas, le **type** de l'événement qui nous intéresse est *QUIT* qui correspond au clic sur le bouton de fermeture. Cet événement n'a pas de valeur importante pour nous.

pygame dispose d'une fonction (*event.get*) qui renvoie un tableau de tous les événements qui se sont produits depuis la dernière fois qu'on l'a demandé.

Voici ce que nous allons faire.
A la fin de chaque tour de boucle :

1. on récupère la liste des événements.
2. on parcours cette liste à la recherche d'un événement de type QUIT.
3. Si on tombe sur un événement de type QUIT, on met *continuer* à *0* ce qui arrêtera la boucle au début de la prochaine itération.

Voici le code qui fait cela :

```python
# Si on a clique sur le bouton de fermeture on sortira
# au debut du prochain tour de boucle
# Pour cela, on parcours la liste des evenements
# et on cherche un QUIT...
for event in pygame.event.get(): # parcours de la liste des evenements recus
    if event.type == pygame.QUIT: # Si un de ces evenements est de type QUIT
        continuer = 0
```

Vous trouverez ici [le fichier complet](../Sources/02_escape.py) de cette étape.
