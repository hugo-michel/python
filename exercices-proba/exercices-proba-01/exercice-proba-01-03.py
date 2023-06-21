# exo 1.3
# Alice et Bob jouent à pierre papier ciseaux.
# - 1 équivaut à pierre
# - 2 équivaut à papier
# - 3 équivaut à ciseaux
# Rédigez le code qui indique qui gagne.

import random

alice = random.randint(1, 3)
bob = random.randint(1, 3)

print("1 : pierre, 2 : papier, 3 : ciseaux")
print(f" alice : {alice}, bob : {bob}")

# réponse 1.3

# if alice == bob:
#     print("match nul")
# else:
#     if alice == 1:
#         if bob == 3:
#             print("Alice gagne")
#         else:
#             print("Bob gagne")
#     elif alice == 2:
#         if bob == 1:
#             print("Alice gagne")
#         else:
#             print("Bob gagne")
#     if alice == 3:
#         if bob == 2:
#             print("Alice gagne")
#         else:
#             print("Bob gagne")

if alice == bob:
    print("match nul")
else: 
    if (alice > bob and alice == bob + 1) or (alice + 2 == bob) :
        print("Alice gagne")
    else:
        print("bob gagne")
