# exo 4.1
# Rédigez le code qui affiche la valeur et la couleur de chaque carte du jeu.

# réponse 4.1

my_tuple = ('foo', 123)

# code 4.2
# Les tuples ressemblent aux listes car on peut y lire des données à la façon d'une liste.

cards = []

for i in range(0, 4):
    for j in range(1, 14):
        if i == 0:
            color = 'rouge'
            symbol = 'cœur'
        elif i == 1:
            color = 'rouge'
            symbol = 'carreau'
        elif i == 2:
            color = 'noir'
            symbol = 'pique'
        elif i == 3:
            color = 'noir'
            symbol = 'trèfle'
        cards.append((symbol, color, j))


for i in range(0, len(cards)):
    print(cards[i][1], cards[i][2])