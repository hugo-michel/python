# exo 7.11
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus petit ou égal à 2, ou plus grand ou égal à 9
# affichez la variable `count` après la boucle

import random

# réponse 7.11

count = 0

for i in range(0, 100):
    r = random.randint(1, 10)
    if (r <= 2) or (r >= 9):
        count += 1
print(count)
