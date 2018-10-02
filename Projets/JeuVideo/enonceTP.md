## Projet mini jeu vidéo
## Vincent Pagé.


Ce qu’il vous sera demandé :

A l'issue de ce TP, vous devrez avoir réalisé un programme qui affiche une fenêtre, dans
laquelle s'affiche un personnage (que vous contrôlerez avec les touches directionnelles du
clavier) ainsi que 2 balles (qui se déplaceront en ligne droite et rebondiront sur les bords de la
fenêtre)

Pas de panique, on va y aller doucement !


1. Etape 1 : (5 mn) :

    1.1 Bootez l'ordinateur sous Linux, loguez vous, et retrouvez cet énoncé sur le web :-)

    1.2 récuperez [le fichier du tutoriel](Sources/tutos.zip)

    1.3 Décompressez le dans un répertoire de travail. Ouvrez l'éditeur de texte de votre choix pour visualiser le fichier *06_imageTexte.py* et sauvegardez le sous le nom *baseJeu.py*.

    1.4 Ouvrez un terminal et déplacez vous jusqu'à
    votre répertoire de travail. Lancez le programme avec la commande python baseJeu.py

    1.4 Si vous voyez apparaître une fenêtre avec
    un fond d'herbe et un petit personnage fixe,
    vous avez terminé cette étape. Sinon, appelez
    votre encadrant !

2. Etape 2 : (10 mn)

  - Modifiez le code de façon à faire apparaître en plus du personnage une balle placée à la position x=250, y=300.
  N'oubliez pas que pour afficher une image dans la fenêtre, il faut 3 choses :

    - lire l'image,

    - définir le rectangle dans lequel cette image va se placer,

    - "bliter" l'image dans la fenêtre.

3. Etape 3 : (15 mn)

  - Modifiez le code de façon à ce que la balle remonte toute seule dans la fenêtre au fur et à mesure du temps (tant pis si elle disparaît à la fin).

  - Il s'agira sans doute de modifier la variable de positionnement de la balle. Demandez vous quelle est cette variable.

4. Etape 4 : (20 mn)

  - Modifiez le code de façon à ce que la balle reste bloquée quand elle arrive en haut de la fenêtre.
  - Il s'agira sans doute de contrôler  la variable de positionnement de la balle, et de spécifier sa valeur si elle sort de la fenêtre.

5. Etape 5 : (30 mn)

  - Modifiez le code de façon à ajouter une seconde balle en x = 50, y = 300. faites la DESCENDRE dans la fenêtre, et bloquez la quand elle arrive EN BAS.

  - Pour la bloquer au bon endroit, il vous manquera peut être une information. Trouvez laquelle et demandez à votre encadrant comment l'obtenir.

6. Etape 6 : (20 mn)

  - Modifiez le code de façon à ce que la première balle reparte vers le bas lorsqu'elle touche le haut de la fenêtre.

7. Etape 7 : (30 mn)

  - Modifiez le code de façon à pouvoir donner une direction initiale à chaque balle : (1,2) pour la balle 1 et (2, -1) pour la seconde balle

  - Il faut également qu'elles rebondissent sur les bords de la fenêtre lorsqu'elles les atteignent