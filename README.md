## Conjecture de Syracuse (ou conjecture de Collatz)

La conjecture de Syracuse est l'hypothèse mathématique selon laquelle la suite de Syracuse de n'importe quel entier strictement positif atteint 1. Ce programme permet de constater cette simple mais mystérieuse théorie.

######  Il n'y a pas réellement d'objectif scientifique, il a surtout permis de prolonger et approfondir une discussion avec un enfant de 8 ans (très) curieux et de vulgariser cette théorie. Un graphique vaut parfois mieux que les mots d'un papa!

---
##### Le principe est simple, pour tout entier strictement positif:
    - s'il est pair, on le divise par 2
    - s'il est impair on le multiplie par 3 et on ajoute 1

En répétant l'opération, nous obtenons la suite de Syracuse... qui se termine inéluctablement par une boucle infinie 4,2,1,4,2,1,4,2,1,...
https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse

### Usage
    - définir l'entier ou la liste d'entiers à étudier dans args.json
    - python syracuse.py