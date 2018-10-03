

### Création de la fenêtre

**Attention** : si vous exécutez ce programme, il va entrer dans une boucle infinie qu'il faudra quitter en appuyant sur Ctrl+C pour le quitter.

Nous allons essayer de créer une fenêtre qui reste ouverte indéfiniment.

Voyons donc les lignes telles qu'elles arrivent :

```python
import pygame
```
Cette ligne dit à python que vous voulez utiliser la bibliothèque **pygame** (on parle du **module pygame** en python).

Si pygame n'est pas installé sur votre machine le programme s’arrêtera là avec une erreur.

```python
# Initialisation de la bibliotheque pygame
pygame.init()
```
Le \# est un commentaire en python. Cette ligne est ignorée par le programme. La phrase *Initialisation ....* est juste là pour aider la personne qui regarde mon fichier python à comprendre ce que je veux faire.

*pygame.init()* est un appel de la fonction *init()* de pygame qui va se charger de préparer le terrain pour notre jeu.
*(si cela vous intéresse, sachez que pygame va regarder quelles sont les propriétés de votre écran, carte graphique, carte son ... parce que notre programme va jouer avec. Mais nous ne nous en rendrons pas compte)*

```python
# creation de la fenetre
largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))
```
Ces lignes vont créer une fenêtre de 480 pixels de hauteur par 640 pixels de largeur.

les variables *largeur* et *hauteur* ne doivent pas vous poser de problèmes (sinon retournez voir le cours de python)

Cette ligne mérite quelques explications supplémentaires
```python
fenetre=pygame.display.set_mode((largeur,hauteur))
```
la fonction *set_mode()* va créer une fenêtre. J'aurais plus loin besoin de cette fenêtre (pour dessiner dedans). Je récupère donc la réponse de la fonction pour la mettre dans une variable que j'ai appelé *fenetre*.

Vous pouvez noter que *fenetre* n'est sans doute pas un type simple comme les entiers, float, string que vous avez sans doute vu avant. C'est vrai. c'est un **objet** (complexe). Mais on s'en moque. De notre point de vue, c'est juste la variable qui représente notre fenêtre.

---------------

A ce stade, si mon programme ne contenait que cela, je pourrais le lancer, les lignes s’exécuteraient jusque là, la fenêtre s'ouvrirait. Puis mon programme se termine, et il ferme la fenêtre avec lui...

Nous avons crée le jeu vidéo le plus court du monde (ou presque)

Pour que le jeu reste ouvert, il faut ajouter une boucle. qui s’exécute jusqu’à ce que l'utilisateur en ait assez.

Au plus simple, je vais ajouter une boucle infinie comme suit.
```python
# la boucle infinie dans laquelle on reste coince
i=1;
continuer=1
while continuer=1:
    i= i+1;
    print (i)
```
Dans les lignes qui précèdent, vous avez une boucle classique qui s'exécute tant que *continuer* a la valeur *1*. Si vous ne comprenez pas ce code, retournez voir la partie cours ICI.

Évidemment, comme mon code est entré dans une boucle infinie, je n'atteindrais jamais la suite du code. Je vous l'explique quand même car elle servira plus tard

```python
# fin du programme principal.
# On n'y accedera jamais dans le cas de ce programme
pygame.quit()
```
Normalement, quand un programme utilisant pygame se termine, il appelle la fonction *quit()* avant de se terminer (cela range bien tout comme il faut).

Voyons donc comment quitter notre programme.
