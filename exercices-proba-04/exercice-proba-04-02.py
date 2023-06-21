# exo 4.2
# Alice tire 1 carte au hasard (sans la remettre dans le jeu).
# Puis Alice tire 1 carte au hasard (sans la remettre dans le jeu).
# Rédigez le code qui effectue ces opérations.
# Ensuite affichez le nombre de cartes qui restent dans le jeu et enfin remettez toutes les cartes dans le jeu.

# réponse 4.2
import random

cards = []
alice_cards = []

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

for i in range(0,2):
    card = random.choice(cards)
    cards.remove(card)
    alice_cards.append(card)

print(alice_cards)
print(len(cards))

#remise des 2 cartes dans le paquet
cards.extend(alice_cards)
alice_cards.clear()

print(alice_cards)
print(len(cards))
