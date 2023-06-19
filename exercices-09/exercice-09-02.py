# exo 9.2
# Créez un dictionnaire nommé `my_dict` associant :
# - une clé booléenne et un nombre entier
# - une clé booléenne et un nombre à virgule flottante
# - une clé numérique et une chaîne de caractères
# - une clé alphanumérique et un booléen
# Puis affichez le résultat avec un simple `print()`

# réponse 9.2

#si clé numérique = 0 ou 1 --> bordel avec les clés booléennes !!
#les clés doivent etre unique, et vu qu'en python True + True = 2...


my_dict = {
    True : 123,
    False : 3.14,
    2 : "foobarbaz",
    "a" : True,
}

print(my_dict)