### Concepts d'algorithmique d'aujourd'hui.
Ceci est ma vision de la programmation actuelle. Tout le monde ne s'y retrouvera peut être pas, mais il me semble que la plupart des développeurs en entreprise seront d'accord avec le constat suivant :
Programmer (ou coder) fait appel à deux grands capacités :
- la stratégie
- la tactique

#### La stratégie
C'est, dans le domaine militaire, ce qui vous fait gagner une guerre (*si vous le faites bien et que vous avez de la chance*). C'est la planification vue de loin.

Les généraux, autour d'une table, décident d'envoyer tel bataillon à gauche, pendant que tel autre bataillon partira à droite pour prendre en sandwich l'armée adverse. Ils peuvent aussi planifier de faire un siège pour affamer l'armée ennemie, et quand ils auront faim, ils attaqueront.

#### La tactique
C'est, dans le domaine militaire, ce qui vous fait gagner une bataille (*si vous le faites bien et que vous avez de la chance*). C'est la planification vue de très près.

Le sergent, au coeur du champ de bataille, décide d'envoyer 2 hommes a gauche de la petite colline, pendant que ...

Les sergents font souvent de mauvais généraux, les généraux font souvent de mauvais sergents.

#### Quel rapport avec l'algorithmique et la programmation ?
Prenons un exemple plus ou moins simple : Vous souhaitez faire un programme qui reconnaisse le visage des différents étudiants de la promotion.

Plus précisément, nous devons faire un programme auquel on donne une image, et il doit retrouver le nom de l'étudiant correspondant.

Je vais supposer que nous disposons d'images des visage chaque étudiant de la promotion, associé à son nom.

La partie **Stratégie** c'est la définition des grandes étapes de mon programme. Pour l'exemple, on pourrait penser à quelque chose comme ceci :
lorsqu'on me donne un fichier image à reconnaitre, je vais :


1. lire l'image du fichier -> une image *inconnue*

2. lire l'ensemble de mes images connues -> *maBase*

3. pour chaque image de *maBase*

    3.1 Je mesure la distance de mon image *inconnue* a l'image connue -> dist

    3.2 Je retiens l'image connue ayant la plus distance *dist* -> *imageLaPlusProche*

4. J'annonce avoir reconnu l'étudiant dont le nom corresspond à *imageLaPlusProche*

Vous ne savez pas lire une image ? Ce n'est pas très grave (internet ou votre sergent le sait)

Vous ne savez pas définir une distance entre deux images ?  Raffinez votre stratégie. Par exemple, une solution classique (assez peu efficace, il faut reconnaître) consiste à calculer la somme des carrés des différences pixel à pixel entre les 2 images.

Tout ce travail n'est pas forcément fait par un informaticien.

La partie **tactique** c'est, pour une partie précise de mon programme, la réalisation d'un algorithme dans un langage donné.

Pour l'exemple, Si je dois faire cette somme des carrés ... je pourrais faire quelque chose comme ceci :

```python
  distance = 0;
  for x in range(len(image1.width) :
    for y in range()(image1.height)) :
      dist += (image1[x][y] - image2[x][y]) **2
```

Vous ne comprenez pas ce code ? c'est normal. Vous devriez en comprendre l'essentiel d'ici quelques cours.

La **tactique**, c'est de la programmation les mains dans le cambouis (*ou dans la boue si on conserve l'image du sergent*)

Les cours d'algorithmique focalisent souvent sur la tactique, alors que les langages actuels permettent d'en faire abstraction assez fréquemment. Par exemple, si je dois trier un tableau par ordre croissant, nous avons, dans tous les langages évolués, des fonctions pour le faire sans faire la moindre boucle.

La **stratégie**, est utile pour programmer mais aussi pour la coordination de n'importe quel projet que vous aurez à réaliser : vous aller choisir d'enchainer des actions, certaines requérant des résultats obtenus par des actions précédentes...

Ce cours a pour objectif de vous apprendre un peu de **tactique** (les variables, les boucles, les fonctions...) et beaucoup de **stratégie**.

Voyons donc le minimum de tactique à savoir pour commencer
