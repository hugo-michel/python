# exo 4.4
# Alice et Bob parient en jouant aux cartes.
# Voici comment se déroule le jeu :
# 1. Bob mélange les cartes, puis Alice tire trois cartes.
# 2. Elle parie que si un 3 (de n'importe quelle couleur) ou deux cœurs figurent parmi les cartes tirées, elle gagne.
# 3. Alice remets ses cartes dans le jeu, le mélange à nouveau, puis Bob tire 3 cartes.
# 4. Il parie que si un 7 (de n'importe quelle couleur) ou deux piques figurent parmi les cartes tirées, il gagne.
# 5. Bob remet ses cartes dans le jeu, ce qui termine une manche.
# Ils décident de faire trois manches.
# Rédigez le code qui modélise ce jeu et indiquez qui sera le gagnant des trois manches.

# réponse 4.4
import random

cards = []
alice_cards = []
bob_cards = []
counter_alice = 0
counter_bob = 0
nombre_manche = 3

#génération paquet
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

for i in range(0,nombre_manche):
    print("\n")
    print(f"Manche numéro {i + 1} :")
    #mélange paquet
    random.shuffle(cards)

    #alice tire 3 cartes
    for i in range(0,3):
        card = random.choice(cards)
        cards.remove(card)
        alice_cards.append(card)

    print(alice_cards)

    #test victoire
    for i in range(0, len(alice_cards)):
        if (alice_cards[i][2] == 3) or (sum(x.count("cœur") for x in alice_cards) >= 2 ):
            print("alice gagne")
            counter_alice += 1
            break

    #remise des cartes dans le paquet + melange le paquet
    cards.extend(alice_cards)
    alice_cards.clear()
    random.shuffle(cards)

    #bob tire 3 cartes
    for i in range(0,3):
        card = random.choice(cards)
        cards.remove(card)
        bob_cards.append(card)

    print(bob_cards)

    #test victoire          
    for i in range(0, len(bob_cards)):
        if (bob_cards[i][2] == 7) or (sum(x.count("pique") for x in bob_cards) >= 2 ):
            print("bob gagne")
            counter_bob += 1
            break

    cards.extend(bob_cards)
    bob_cards.clear()
    random.shuffle(cards)

#résultat final   
if counter_alice == counter_bob == 0:
    print("\n")
    print("Alice et Bob n'ont gagné aucune manche : égalité")
elif counter_alice == counter_bob :
    print("\n")
    print(f"Alice et Bob ont gagné {counter_alice} manche : égalité")
elif counter_alice > counter_bob :
    print("\n")
    print(f"Alice a gagné {counter_alice} manche, Bob a gagné {counter_bob} manche : Alice gagne")
else:
    print("\n")
    print(f"Alice a gagné {counter_alice} manche, Bob a gagné {counter_bob} manche : Bob gagne")
