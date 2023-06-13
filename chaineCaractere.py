from datetime import date

texte1 = "lorem"
texte2 = "ipsum"
print(texte1)
print(texte2)

# concatenation
texte3 = texte1 + texte2
print("concatenation")
print(texte3)
texte3 = texte1 + " " + texte2
print(texte3)

#repetition
print("repetition")
texte4 = texte1 * 3
print(texte4)

#concatenation et typecasting
print("concatenation et typecasting")
nombre1 = 123
nombre2 = 3.14
texte5 = "nombre1 : " + str(nombre1) + ", nombre2 : " + str(nombre2) + ", texte1 : " + texte1
print(texte5)

#interpolation (variables dans strings)
print("interpolation")
texte5 = f"nombre1: {nombre1}, nombre2: {nombre2}, texte1: {texte1}"
print(texte5)
texte5 = f"nombre1: {nombre1:.2f}, nombre2: {nombre2:.2f}, texte1: {texte1}"
print(texte5)

#operations arithmetiques dans une fstring
print("operations dans fstring")
annee_naissance = 1989
annee_courante = date.today().year
print(f"age : {annee_courante - annee_naissance} ans")

#affichage accolades
print(f"accolade ouvrante {{ et accolade fermante }}")

#manipulation strings
texte6 = "foo bar baz"
print(f"texte6 : {texte6}")
#longueur strings
print(f"longueur: " , len(texte6), "caracteres")
#index chaine de caractere dans string
#pour chercher une autre occurence du mm mot texte6.find("bar", position + 1)
#si la recherche ne renvoie rien (le mot n'est pas présent) renvoie -1
print(f"index bar : ", texte6.find("bar"))
#occurence chaine de caractere dans string
print(f"occurences ba dans texte6 : ", texte6.count("ba"))
#remplacement texte
print("rzmplacement bar par lorem")
texte6 = texte6.replace("bar", "lorem")
print(texte6)
#scinder texte : creer une liste
print("split espace separateur")
liste_mots = texte6.split(" ")
print(liste_mots)
#remplacement par split() et join()  join transforme une liste en strings : texte8= " ".join(list1)
old = "baz"
new = "ipsum"
tmp = texte6.split(old)
texte6 = new.join(tmp)
print(texte6)

#affichage partie d'une string via les index
print(f"texte 6 :", texte6)
print(f"texte 6 index 4 à 7 : ", texte6[4:7])
print(f"texte 6 index 4 à 7 pas de 2 : ", texte6[4:7:2])
print(f"texte 6 index 4 jusque la fin :", texte6[4:])
print(f"texte 6 debut à index 7 :", texte6[:7])
print(f"texte 6 caractere inversé : ", texte6[::-1])

#documentation focntion

def ouiNon(value):
    """"  "oui" si true
    "non" si false
    "" sinon 

    value bool
    return str
    """
    if value == True:
        return "oui"
    elif value == False:
        return "non"
    return ""

print(ouiNon.__doc__)