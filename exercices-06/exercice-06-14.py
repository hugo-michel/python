# exo 6.14
# Créez une deuxième liste nommée `new_list` ne contenant que les nombres entiers de la liste
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.14

new_list = []

for i in range(0, len(my_list)):
    if type(my_list[i]) == int:
        new_list.append(my_list[i])
print(new_list)

