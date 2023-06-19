# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur booléenne
# - renvoie True si `a` est plus grand que `b`
# - renvoie False dans les autres cas
# Appelez la fonction et affichez le résultat

# réponse 10.4

def is_greater(a:float, b:float) -> bool:
    if a > b:
       return True
    else:
        return False
    
print(is_greater(5,3)) #renvoie True
print(is_greater(3,4)) #renvoie False