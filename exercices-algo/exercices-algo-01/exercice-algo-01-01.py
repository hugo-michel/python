# exo 1.1
# Triez la liste suivante en ordre croissant en utilisant l'algorithme du tri bulle puis affichez la liste.
#
# ATTENTION : ne pas utiliser les fonctions sorted() et list.sort()

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 1.1

for j in range(0, len(my_list)):
    for i in range(0, len(my_list) - 1):
        if (my_list[i] > my_list[i+1]) :
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)


#au prmeier tour pas de valeur précedente
# previous = None
# for number in my_list:
#     #traitement des datas
#     #affiche valeur tour actuel
#     print(number)
#     #affiche valeur tour précedent
#     print(previous)
#     #preparation tour suivant
#     #on save tour actuelle pour le tour suivant qui devient previous
#     previous = number