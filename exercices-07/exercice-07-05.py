# exo 7.5
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est plus grand ou égal à 6

import random

# réponse 7.5

for i in range(0, 99):
    r = random.randint(1, 10)
    if r >= 6:
        print(r)
