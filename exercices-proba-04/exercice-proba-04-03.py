# exo 4.3
# Bob tire 3 cartes au hasard (sans les remettre dans le jeu) et les met dans son paquet.
# Rédigez le code qui effectue ces opérations.
# Ensuite affichez le paquet de Bob, le nombre de cartes qui restent dans le jeu et remettez toutes les cartes dans le jeu.

# réponse 4.3

import random

cards = []
bob_cards = []

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

for i in range(0,3):
    card = random.choice(cards)
    cards.remove(card)
    bob_cards.append(card)

print(bob_cards)
print(len(cards))

#remise des 2 cartes dans le paquet
cards.extend(bob_cards)
bob_cards.clear()

print(bob_cards)
print(len(cards))
