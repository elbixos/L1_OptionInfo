

### 3. Ajout d'une horloge
Il est temps d'affiner un peu ce qu'est notre boucle *while*, à part un moyen d'éviter que la fenêtre se referme...

Pensez à notre jeu comme à un jeu par tours : dans un tour (qui prendra un certain temps), il faudra au final :

- regarder s'il faut déplacer le personnage joueur
- déplacer les ennemis du joueur
- ré-afficher l'écran
- regarder si le joeur veut quitter le programme.

et on recommence...

Ceci est pris en charge par notre boucle *while*.
C'est pour cette raison qu'a chaque tour de boucle,
on *regarde si le joueur veut quitter le programme*, ce que nous avons fait à l'étape précédente.

Nous allons, au cours du projet, ajouter toutes les étapes listées ci-dessus.

Le problème est que sans contrôle supplémentaire, les tours de boucle se font aussi vite que notre ordinateur peut le supporter.

Sur un ordinateur rapide, les ennemis vont donc se déplacer à toute vitesse. Sur un ordinateur lent, les ennemis auront tendance à lambiner.

Pour éviter cela, nous allons ajouter une horloge qui va servir à **définir la durée minimale** d'un tour de boucle.

Pygame utilise la notion de *Clock* (horloge).
Je vais donc, au début de mon programme, demander la création d'une variable de type *Clock*. Je vais nommer cette variable *horloge* :

```python
# servira a regler l'horloge du jeu
horloge = pygame.time.Clock()
```

Cette variable est encore une fois d'un type plus étrange qu'un entier (comme *fenetre*, c'est un objet. On dirait ici que *horloge* est une instance de la classe *Clock*)

Il se trouve que les objets ont des fonctions internes. Les objets de type Clock disposent d'une fonction nommée *tick()* qui fonctionne comme suit :

- quand on l'appelle pour la première fois : elle note l'heure (à la milliseconde près)

- quand on la rappelle :

  - elle note l'heure actuelle, et la compare à l'heure précédemment notée.

  - si la différence entre les heures est supérieure à la durée minimale souhaitée, elle ne fait rien.

  - sinon, elle endort le programme jusqu'à ce que cette durée soit atteinte.

Notez que la durée minimale est communiquée a la fonction *tick* en la passant entre parenthèses. On dit qu'on a **passé un argument à la fonction**.

Appliquons cela à notre cas : Nous voulons limiter la vitesse de notre boucle, nous allons donc placer l'appel à la fonction *tick* de notre *horloge* dans la boucle *while* (peu importe où).

Pour définir la durée on passe à la fonction l'inverse de la durée souhaitée :
- pour une durée de 0.5s, on passe 2 à la fonction *tick*
- pour une durée de 0.1s, on passe 10 à la fonction *tick*
- ...

Notre code à insérer pour faire au maximum 2 tours par seconde est donc :

```python
# fixons le nombre max de frames / secondes
horloge.tick(2)
```

Dans le jeu final, vous utiliserez sans doute une valeur de 30 tours par seconde.

```python
# fixons le nombre max de frames / secondes
horloge.tick(30)
```

Vous trouverez ici [le fichier complet](../Sources/03_horloge.py) de cette étape.
