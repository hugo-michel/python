# exo 2.7
#
# Ça vous semble bon ? On va vérifier en créant un test.
#
# Appelez la fonction `fibonacci()` dans une boucle qui va de `0` à
# 10` en utilisant un index et la fonction `range()`. Utilisez cet index
# pour récupérer le nombre du rang correspondant dans la liste
# `fibonacci_numbers` puis comparez le résultat de votre fonction. S'il
# y a une différence, affichez un message d'erreur suivi du rang et des
# deux valeurs.

# réponse 2.7

fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else : 
        return (fibonacci(n-1)) + (fibonacci(n-2))

for i in range(0, 10):
    print(fibonacci(i))
