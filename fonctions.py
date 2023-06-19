#definition :
def hello():
    print("hello world !")

#appel fonction
hello()

def moyenne(valeurs):
    somme = 0

    for valeur in valeurs:
        somme += valeur
    return somme / len(valeurs)

nombres = [100, 123, 3.14, 46]
m = moyenne(nombres)
print('myenne des nombres : ', m)

points = [100, 143, 167]
m = moyenne(points)
print('moyenne des points : ', m)

#####################################
def addition(a, b):
    return a + b

c = 1
d = 2
resultat = addition(c, d)
print(resultat)

resultat = addition(3,4)
print(resultat)

####################################
def incrementer(a, b=1):
    return a + b

a = 0
print(f"a = {a}")
a = incrementer(a)
print(a)

a = incrementer(a, 2)
print(a)

a = incrementer(a, b=3)
print(a)

###################################
def ma_fonction(a, b=1, c=2):
    return a + b + c
# resultat = ma_fonction(1, b=2)
# print(resultat)
# resultat = ma_fonction(1, c=3)
# print(resultat)
#modifie b mais pas c
# resultat = ma_fonction(1, 2)
# print(resultat)
# #modifie b et c pour 2 et 3
resultat = ma_fonction(1,2,3)
print(resultat)

#assignement destructuré :
print("assignement destructuré")
def ma_fonction2(a, b):
    return a + b, a - b

addition, soustraction = ma_fonction2(1,2)
print(addition)
print(soustraction)


#nombres = [100, 123, 3.14, 46]
def modifier_valeurs(valeurs):
    valeurs[1] = "foo"

print(nombres)
modifier_valeurs(nombres)
print(nombres)

#type hinting

def ma_fonction3(a:float, b:float) -> bool:
    return a > b
resultat = ma_fonction3("foo", "bar")
print(resultat)

#les fonctions sont des variables, elles peuvent etre copier dans une autre variable
#points = [100, 143, 167]
#max() renvoie la plus grande valeur, si str renvoie le plus grand ordre alphabetique
print(points)
py_max = max
def max():
    pass

print(py_max(points))
max = py_max
print(max(points))