# exo 2.4
#
# Reprenez votre fonction `fibonacci()`.
# Puis modifiez-là de façon à ce que la fonction :
# - renvoie la somme de `fibonacci(0)` et
# `fibonacci(1)` si on lui passe `2` en paramètre.
# - renvoie `None` dans les autres cas
#
# Appelez votre fonction dans une boucle qui va de `0` à `2` en
# utilisant un index et la fonction `range()`.

# réponse 2.4

def fibonacci(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return fibonacci(0) + fibonacci(1)
    return None

for i in range(0, 3):
    print(fibonacci(i))

    