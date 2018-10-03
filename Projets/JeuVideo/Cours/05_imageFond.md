

### 5. Ajout d'une image de fond

Nous voulons ajouter une image de fond à notre fenêtre.

Cette partie est très simple, car il s'agit simplement d'ajouter une seconde image dans la fenêtre. Nous l'avons déja fait.

```python
# lecture de l'image du fond
imageFond = pygame.image.load("background.jpg").convert()
```

```python
# creation d'un rectangle pour positioner l'image du fond
rectFond = imageFond.get_rect()
rectFond.x = 0
rectFond.y = 0
```

et dans la boucle *while*
```python
# Affichage du fond
fenetre.blit(imageFond, rectFond)
```
**important :** ce dernier bloc doit être positionné avant le *blit* du personnage... (pourquoi ?)

Et voila !

Vous trouverez ici [le fichier complet](../Sources/05_imageFond.py) de cette étape.

#### Remarques
Notez ce qui se passe si vous ajoutez maintenant le déplacement du personnage (automatique ou au clavier) que je proposais dans l'étape précédente.

A chaque étape, on :
1. redessine tout le fond
2. redessine le Personnage

De ce fait, les "traces" du personnage sont écrasées par le nouveau dessin du fond.

Si vous trouvez inutile de redessiner tout le fond, alors que seuls quelques pixels du fond doivent être re-dessinés, sachez que c'est légitime (mais un poil compliqué à mettre en oeuvre).

 je vous inviterais dans ce cas à lire la partie de la documentation de pygame qui parle de **dirty rect animation**. On la trouve [ici](https://www.pygame.org/docs/tut/newbieguide.html).
