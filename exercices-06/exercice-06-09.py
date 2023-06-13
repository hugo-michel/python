# exo 6.9
# Calculez la somme des nombres de la liste et affichez le résultat
#
# ATTENTION : ne pas utiliser la fonction sum()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.9

# total = 0
# i = 0

# for i in range(0, len(my_list)):
#     total += my_list[i]

# print(total)

somme = 0
for item in my_list:
    somme += item

print(somme)