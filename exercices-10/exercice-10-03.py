# exo 10.3
# Créer une fonction nommée `oui_non()` qui :
# - prend un paramètre booléen
# - renvoie une valeur booléenne
# - renvoie `oui` si le paramètre est égal à True
# - renvoie `non` si le paramètre est égal à False
# Appelez la fonction avec la valeur True et affichez le résultat
# Appelez la fonction avec la valeur False et affichez le résultat

# réponse 10.3

def oui_non(a:bool) -> bool:
    if a == True:
        print("oui")
    else:
        print("non")

# def oui_non(a:bool) -> bool:
#     if a == True:
#         return("oui")
#     else:
#         return("non")

oui_non(True)
oui_non(False)