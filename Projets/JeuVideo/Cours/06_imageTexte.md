

### 6. Ajout de texte dans la fenêtre

Nous allons maintenant écrire du texte dans la fenêtre. Cela pourrait vous servir pour afficher le score pendant le jeu (ou tout autre message).

Dans la fenêtre, pygame sait dessiner des images (on les appelle **surfaces** selon la terminologie de pygame mais on s'en moque)

Il s'agit donc de créer une image contenant le texte.

L'image que l'on veut créer dépend de la police choisie qui prend en compte trois choses :
- la famille de police utilisée
- la taille du texte à afficher
- la couleur

Encore une fois, votre programme manipule des variables... Créons donc une police adaptée avant le début de la boucle *while*.

```python
## Ajoutons un texte fixe dans la fenetre :
# Choix de la police pour le texte
font = pygame.font.Font(None, 34)
```
ma police, stockée dans la variable *font* crée par le code précédent va me servir à générer une image de texte :

```python
# Creation de l'image correspondant au texte
imageText = font.render('<Escape> pour quitter', True, (255, 255, 255))
```
Dans le code qui précède, l'objet *font* propose une fonction *render* qui crée l'image.
Cette fonction a besoin de 3 paramètres :

- *' < Escape > pour quitter'* est le texte à afficher.

- *True* est un truc sans intérêt (un booléen pour choisir ou non l'option d'anti-aliasing)

- *(255, 255, 255)* est un triplet de valeur qui définit une couleur RGB. Ici, c'est du blanc. *(255,0,0)* serait du rouge

Le reste a déja été vu :

- on crée un rectangle, qu'on positionne.
```python
# creation d'un rectangle pour positioner l'image du texte
rectText = imageText.get_rect()
rectText.x = 10
rectText.y = 10
```

- on *blit* l'image du texte.
```python
# Affichage du Texte
fenetre.blit(imageText, rectText)
```

Vous trouverez ici [le fichier complet](../Sources/06_imageTexte.py) de cette étape.
