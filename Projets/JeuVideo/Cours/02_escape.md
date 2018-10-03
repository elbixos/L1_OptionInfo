

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


le premier bloc de nouveautés est le suivant et concerne la détection d'un appui sur la touche *Escape*.

```python
# on recupere l'etat du clavier
touches = pygame.key.get_pressed();
```
*key.get_pressed()* est une fonction de pygame. Son nom m'indique plus où moins à quoi elle sert : Elle va me répondre quelles touches du clavier sont enfoncées au moment où je l'appelle.
Ma ligne met le résultat dans une variable que j'ai nommé *touches*

Pour traiter le cas qui m’intéresse (quand la touche *Escape* est enfoncée), il faut connaitre la tête de ma variable *touches*. La doc de pygame peut nous renseigner là dessus et en voici une explication très brève.

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

--------------

Adaptons ceci a notre cas...

```python
# si la touche ESC est enfoncee, on sortira
# au debut du prochain tour de boucle
if touches[pygame.K_ESCAPE] :
    continuer=0
```
```python
# Si on a clique sur le bouton de fermeture on sortira
# au debut du prochain tour de boucle
# Pour cela, on parcours la liste des evenements
# et on cherche un QUIT...
for event in pygame.event.get(): # parcours de la liste des evenements recus
    if event.type == pygame.QUIT: # Si un de ces evenements est de type QUIT
        continuer = 0
```
