# exo 2.1
#
# Ajoutez les 10 premiers nombres de la suite de Fibonacci, que vous
# aurez calculé « à la main », dans une liste nommée
# `fibonacci_numbers`. Puis affichez cette liste en utilisant une
# boucle de type « for each ».
#
# ATTENTION : la suite doit démarre à 0.

# réponse 2.1

fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

for i, item in enumerate(fibonacci_numbers):
    print(item)

