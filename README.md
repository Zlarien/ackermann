# Ackermann

Fonction d'Ackermann en Python, version itérative (pile explicite).

## Pourquoi ce code
On a travaillé la fonction d'Ackermann en TD d'algorithmique (L3 Informatique, Université d'Évry Paris-Saclay). La calculer à la main devient vite beaucoup trop long, alors j'ai écrit ce petit code pour la faire tourner et voir les étapes intermédiaires.

## Utilisation
`python ackermann.py` calcule les petits cas (A(3,2) = 29), puis tente A(4,4).

**A(4,4) est abandonné après 50 millions d'étapes** : le calcul est trop long, le résultat est une tour de puissances de 2 qu'aucune machine ne peut atteindre. Quelques étapes intermédiaires sont affichées : on voit la pile grossir sans fin.
