# exo 6.18
# Avec le même tableau en 2 dimensions, affichez toutes les valeurs plus petites ou égales à 50 ainsi que leur cordoonnées (ligne et colonne)
# Vous pouvez réutiliser la variable `size` qui a permis de construire le tableau en 2 dimensions
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

import random

size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

print(matrix)

# réponse 6.18

# liste = []

# for l in range(0, size):
#     for c in range(0, size):
#         if matrix[l][c] <= 50:
#             liste.append(matrix[l][c])
#             liste.append(l)
#             liste.append(c)
# print(liste)

for l in range(0, size):
    for c in range(0, size):
        if matrix[l][c] <= 50:
            print(((matrix[l][c], f"ligne {l + 1}", f"colonne {c + 1}")))
