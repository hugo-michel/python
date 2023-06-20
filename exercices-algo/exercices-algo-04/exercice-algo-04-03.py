# exo 4.3
#
# Si vous avez pu répondre aux questions 4.1 et 4.2, vous allez pouvoir
# écrire une fonction nommée `convert_1d_index_to_2d_index()` qui :
#
# - prend un nombre entier nommé `index` en entrée
# - prend un nombre entier nommé `width` (largeur) en entrée
# - renvoie un tuple de nombres entiers indiquant l'index de la ligne et
#   l'index de la colonne (attention à l'ordre des données)
#
# Indice : il s'agit juste de renvoyer les mêmes données que dans `get_row()` et `get_column()` dans un tuple.
#
# Indice : pour tester votre code, utilisez une boucle `for` avec `range()` pour l'index et utilisez `3` pour le `width`.

# réponse 4.3

            # def get_row(index : int, width : int) -> int :
            #     return index // width                       #return index ligne dans matrice 



            # def get_column(index : int, width : int) -> int:
            #     return index % width                        #return index colonne


def convert_1d_index_to_2d_index(index : int, width : int) -> tuple:
    return (index // width, index % width)          #return (ligne, col)


foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]


            # for i in range(0, len(foo)):
            #      print(i, foo[i])
            #      print(convert_1d_index_to_2d_index(i, 3))

for i in range(0, len(foo)):
     print(f"index : {i} valeur : {foo[i]}")
     print(f"coordonnées : {convert_1d_index_to_2d_index(i, 3)}")

