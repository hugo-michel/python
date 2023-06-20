# exo 3.1
#
# Écrivez une fonction nommée `fizzbuzz()` qui compte à partir de 1
# jusqu'au paramètre `n` inclus, passé en paramètre de la fonction, et
# qui respecte les règles du jeu "Fizz buzz".
#
# Appelez la fonction `fizzbuzz()` avec la valeur `20`.

# réponse 3.1

def fizzbuzz(i):
    for i in range(1, i+1):
        if (i % 3 == 0 ) and (i % 5 == 0):
            print("fizz buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz(20)

