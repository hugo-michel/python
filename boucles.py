import math

#boucle while
i = 0
while i < 10:
    i += 1
    print("boucle" + str(i))

#while avec conditions d'arrets
i = 0
while True:
    i += 1
    print("boucle" + str(i))
    if i == 10:
        break

#while classique, incrementation en dernier
i = 0
while i < 10:
    print("boucle" + str(i))
    i += 1

#boucle while à rebours de 10 à 1
i = 10
while i > 0:
    print("boucle" + str(i))
    i -= 1

#boucle while à rebours de 9 à 0
i = 10
while i > 0:
    i -= 1
    print("boucle" + str(i))

#for classique 1 à 10
for i in range(1, 11):
    print("boucle" + str(i))

#for classique 0 à 9
for i in range(0, 10):
    print("boucle" + str(i))

#boucle for à rebours 10 à 1
for i in range(10, 0, -1):
    print("boucle" + str(i))

#boucle for à rebours 9 à 0
for i in range(9, -1, -1):
    print("boucle" + str(i))

#boucle foreach
items = [123, 2, 42, 3.14, 56]
for item in items:
    print(item)

#foreach avec index associés
for i, item in enumerate(items):
    print(i, item)
print(f"index 1 = {items[1]}")
#exemple utilisation
for i, item in enumerate(items):
    if i == 2:
        print(i, item)

#foreach à rebours : inverse les items dans liste
for item in reversed(items):
    print(item)

#foreach à rebours avec les index
for i in range(len(items) - 1, -1, -1):
    print(i, items[i])

#exercice cart

cart = [123, 2, 42, 3.14, 56]
total = 0

for item in cart:
    total += item
total_tva = total * 1.2
moyenne_article = total / len(cart)
print("total htva", total)
print("total tva", total_tva)
# affichage avec tous les chiffres après la virgule
print("moyenne article htva", moyenne_article)
# affichage avec seuls 2 chiffres après la virgule
print("moyenne article htva", "%.2f" % (moyenne_article))
# affichage avec seuls 2 chiffres après la virgule en utilisant un f string
print(f"moyenne article htva {moyenne_article:.2f}")
# calcul moyenne
moyenne_article_tronquee = math.floor(total / len(items) * 100 ) / 100
print(moyenne_article_tronquee)

