# exo 2.2
#
# Reprenez votre boucle de type « for each » et modifiez-là de façon à
# utiliser un index et la fonction `range()` pour parcourir le liste
# des nombres de Fibonacci.

# réponse 2.2

fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

for i in range(0, len(fibonacci_numbers)):
    print(fibonacci_numbers[i])