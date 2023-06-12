#liste vide
liste1 = [] #mm chose
liste2 = list() # mm chose
print(liste1)
print(liste2)

#append() ajoute une valeur à la fin d'un tableau
liste1.append(123)
print(liste1)

#on peut ajouter des variables
nombre1 = 42
liste1.append(nombre1)
print(liste1)

#on peut ajouter différents types de données
liste1.append(3.14)
liste1.append("foo")
print(liste1)

#creation liste ac differents types de valeur
list3 = [100, 3.14, "foo", True, False, None]
print(list3)

#idem avec variables
nombre2 = 123
nombre3 = 3.14
texte1 = "lorem"

list4 = [nombre2, nombre3, texte1]
print(list4)

#creation liste avec variable et valeures "directes"
liste5 = [nombre1, texte1, "foo", True]
print(liste5)

#affichage valeur avec index
print(liste5[0]) #premiere valeur de la liste : 42
print(liste5[3]) # dernière valeur de la liste : True

#index pour supprimer une valeur avec del
del liste5[0] #suppression premier element de la liste 5 (42)
print(liste5)
#ATTENTION : les index du reste du tableaux sont recalculés
print(liste5[0])

#longueur tableau : nombre element : len()
taille_tableau5 = len(liste5)
print(taille_tableau5)

#index du dernier element tableau : taille du tableau - 1
dernier_index = len(liste5) - 1
print(dernier_index)

#insérer elements au milieu d'un tableau
liste5.insert(1, "bar") #index pour ajout + valeur
print(len(liste5))
print(liste5)

#index pour remplacer (ecraser, reaffecter) une valeur
liste5[0] = 123 #à l'index 0 (premier element) remplace par 123
print(liste5)
texte2 = "baz"
liste5[1] = texte2 #peut etre ecraser avec une variable
print(liste5)

#nouveau tableau
liste6 = ["z", "d", "r", "x", "a"]
print(liste6)

#la fonction sorted() permet d'obtenir une copie d'un tableau trié par ordre alphabetique
liste7 = sorted(liste6)
#tableau original n'est pas modifié
print(liste6)
#la copie du tableau est triée
print(liste7)

#ATTENTION fonction sorted() != méthode .sort()
#ATTENTION le tri s'effectue sur les données, l'ordre original est perdu
#sort() permet de trier un tableau
liste6.sort()
print(liste6)

#la méthode pop() permet de supprimer la derniere valeur d'untableau
#et de l'affecter à une variable
derniere_valeur = liste6.pop()
print(liste6)
print(derniere_valeur)

#concaténation de listes
print(liste5)
print(liste6)
liste8 = liste5 + liste6
print(liste8)

#fusion de listes
liste5.extend(liste6)
print(liste5)
print(liste6)