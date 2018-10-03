## Installation de Python
## Vincent Pagé.

Voici plus ou moins quelques explications pour installer **pygame** et tester.

Vous pouvez aussi chercher sur le net comment faire, cela fonctionne assez bien. Les sites officiels donnent des procédures d'installation à jour, ce sont les seuls à le faire... Apprenez l'anglais dans ce cas, car il est rare que l'on trouve une version francaise sur le site officiel.

Il y a de très belles façons d'installer **pygame**, par exemple en utilisant des **virtual env** notamment.

Si vous avez entendu parler de cela, allez y c'est bien.

Sinon, faites ce qui suit :

### Sous Linux, Mac OS ou windows
Vous savez, depuis l'installation de python décrite [ici](installPython.md) quelle commande lance l’exécutable correspondant à **python 3** sur votre machine.
cela peut etre :
```
python
```
ou
```
python3
```
ou encore
```
py
```

Dans un terminal, lancez la commande :
```
python -m pip install pygame
```
(adaptez cette commande à ce qui fonctionne chez vous)

### Tester l'installation

Dans le terminal, lancez **python 3** puis dans l'interpreteur python, tapez

```python
import pygame
```

Si vous n'avez pas de message d'erreur, c'est fini.
Vous pouvez aller jouer avec le projet [Jeu Video](../Projets/JeuVideo/README.md) par exemple.


---

Vous pouvez revenir au [Sommaire](README.md)

---
