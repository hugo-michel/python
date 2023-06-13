# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15

i = 0
longueur = 0
valeur = ""
index = 0

for i in range(0, len(my_list)):
    if len(my_list[i]) > longueur:
        longueur = len(my_list[i])
        valeur = my_list[i]
        index = i

print(index)
print(valeur)
print(longueur)