## Explications des fichiers du tutoriel
## Vincent Pagé.

### Introduction

Dans ce document, je vais reprendre les explications
que j'ai faites en cours pour bien débuter la programmation d'un jeu vidéo en **python**, utilisant la librairie **pygame**

**Attention** :
1. Je suppose que les pré-requis ce projet sont remplis. Re-regardez [ce lien](../README.md) pour vous en assurer.

2. [ce même lien](../README.md) vous donne aussi accès à l'archive des fichiers sur lesquels nous allons travailler. Téléchargez l'archive et décompressez la, vous modifierez les fichiers pour vos tests.

Arrivés au terme de ce document, si vous suivez effectivement mes propositions, vous aurez déja fait une partie du TP. Il serait dommage de vous en priver.

L'archive contient les fichiers suivant :
- 01_fenetre.py
- 02_escape.py
- 03_horloge.py
- 04_imagePerso.py
- 05_imageFond.py
- 06_imageTexte.py
- background.jpg
- balle.png
- perso.png

les trois derniers fichiers sont des images.
les 6 premiers sont des programmes écrits en **python**. Ils doivent fonctionner pour **python 2.7** et **python 3**.

A l'université, cette année, vous utiliserez python 2.7. Chez vous, utilisez python 3. Globalement, cela ne changera pas grand chose pour vous.

Les 6 fichiers python sont en fait différentes étapes que j'ai suivies pour obtenir un début de jeu vidéo. A chaque étape, je n'ajoute que quelques lignes.

Voici les 6 étapes :
1. Création d'une fenêtre graphique pour notre jeu : [01_fenetre.py](../Sources/01_fenetre.py)

2. Ajout de la possibilité de quitter le jeu : [02_escape.py](../Sources/02_escape.py)

3. Ajout d'une horloge pour cadencer notre jeu :
[03_horloge.py](../Sources/03_horloge.py)

4. Ajout d'une image du personnage dans la fenêtre : [04_imagePerso.py](../Sources/04_imagePerso.py)

5. Ajout d'une image de fond dans la fenêtre :
[05_imageFond.py](../Sources/05_imageFond.py)

6. Ajout d'un texte fixe dans la fenêtre
[06_imageTexte.py](../Sources/06_imageTexte.py)

Je vais maintenant prendre chaque fichier pour vous expliquer tout son contenu.

### Premier fichier
