

### 4. Ajout d'une image du personnage

Cette étape est la dernière vraiment importante de ce tutoriel. Vous pourrez presque faire tout le projet avec. Notamment, l'étape suivante peut en être déduite.

A la fin de cette étape, je vous demanderais de faire des choses tout seul pour tester.

Il s'agit ici d'afficher une image dans la fenêtre.
Voyons cela plus précisément :

- nous avons sur le disque dur un fichier "perso.png" contenant l'image.

- notre programme a une fenêtre graphique (pour notre programme cette fenêtre est stockée dans une variable nommée *fenetre* )

- on voudrait dessiner le contenu du fichier dans la fenêtre, a une position que notre programme va contrôler.

Programmer, c'est manipuler des variables, souvent par l'intermédiaire de fonctions.

#### Lecture de l'image.

La première chose à faire, c'est de lire le fichier "perso.png", extérieur au programme, et à en stocker le contenu dans une variable (ici encore, c'est une variable de type *objet*) dont on se servira plus tard.

Cette lecture peut se faire une seule fois au début du programme. Il ne serait pas très malin de le faire a chaque tour de boucle...

Voici le code correspondant.
```python
# lecture de l'image du perso
imagePerso = pygame.image.load("perso.png").convert_alpha()
```
mon image est maintenant stockée dans la variable nommée *imagePerso*.

#### Variable de positionnement

Il faut comprendre que la mémorisation de la position et l'action d'affichage sur l'écran sont deux choses différentes. Concentrons nous sur la première :

Pour stocker la position de notre personnage, nous avons 2 variables à stocker : un *x* et un *y*, en pixels, correspondant à la position souhaitée de notre image dans la fenêtre.

Mais notre image est un rectangle. Si je choisis une position *x = 10*, *y = 20*, est ce la position du centre de l'image ou du coin supérieur gauche ou d'un autre point ?

Dans pygame (et la plupart des librairies du même type), on considère toujours la position **du coin supérieur gauche**.

De plus, on va stocker ces informations (*x* et *y*) au sein d'une variable plus compliquée : un objet de type *Rect*, qui contiendra *x* et *y* mais aussi la largeur et la hauteur de mon rectangle.

pour un rectangle *r* existant, 4 données nous intéressent :
- *r.x* : l'abscisse du point supérieur gauche.
- *r.y* : l'ordonnée du point supérieur gauche.
- *r.w* : la largeur du rectangle
- *r.h* : la hauteur du rectangle

Ces 4 données sont des entiers.
si je veux afficher la largeur d'un rectangle nommé *r*, je taperais :

```python
print (r.x)
```
si je veux donner à mon rectangle la position verticale 37, je ferais comme suit :

```python
r.y = 37
```

Reste à obtenir un rectangle... Le plus simple est de demander à l'image que l'on veut positionner de nous le fournir.

Notre variable *imagePerso* est un objet capable de fournir un rectangle avec hauteur et largeur pré-remplies.

```python
# creation d'un rectangle pour positioner l'image du personnage
rectPerso = imagePerso.get_rect()
```

Nous disposons donc d'une variable de type *Rect* nommée *rectPerso* pour **stocker** position voulue du personnage.

Disons que nous voudrons dessiner plus loin notre personnage en *x = 60* et *y = 80*, cela se fait donc comme ceci :

```python
rectPerso.x = 60
rectPerso.y = 80
```
#### Affichage dans la fenêtre

J'ai une variable contenant l'image (*imagePerso*), une variable contenant la fenêtre (*fenetre*) et une variable contenant la position souhaitée (*rectPerso*).

Voici la ligne qui demande l'affichage :
```python
# Affichage Perso
fenetre.blit(imagePerso, rectPerso)
```
En termes informatiques, j'appelle la fonction *blit* de l'objet *fenetre* qui se charge de dessiner.

Cette fonction de dessin prend comme paramètres l'image et le rectangle de positionnnement.

Enfin, il reste une ligne mystérieuse qui ne sera faite qu'une fois après le ou les *blit*
```python
# rafraichissement
pygame.display.flip()
```

Imaginons que ma fonction blit dessine directement sur l'écran. Dans un jeu vidéo contenant 50 objets, je vais dessiner 50 fois sur l'écran. Cela poserait des problèmes.

Pour être plus efficace, la fonction *blit* ne dessine pas vraiment sur l'écran. Elle dessine dans une version cachée de la fenêtre.

Je peux donc dessiner 50 fois sur la version cachée de la fenêtre sans toucher l'écran. Une fois tous mes dessins finis, je révèle ma version cachée.

C'est ce que fait la fonction *display.flip*

Vous trouverez ici [le fichier complet](../Sources/04_imagePerso.py) de cette étape.

#### Jouons un peu

Vous en savez suffisamment pour faire beaucoup de choses...

##### Un personnage qui bouge tout seul
