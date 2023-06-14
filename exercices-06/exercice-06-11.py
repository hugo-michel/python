# exo 6.11
# Trouvez l'index de la valeur `3.14` dans la liste et affichez le résultat
# Note : faites une boucle et n'utilisez pas la méthode `index()`
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.11

# for i in range(0, len(my_list)):
#     if my_list[i] == 3.14:
#         print(i)
    
for i, item in enumerate(my_list):
    if item == 3.14:
        print(f"l'index de la valeur 3.14 est {i}")
