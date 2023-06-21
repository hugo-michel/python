# exo 3.1
# Alice et Bob jouent à pile ou face.
# Alice parie qu'elle va obtenir "pile & pile" en deux lancers.
# Rédigez le code qui indique la probabilité qu'Alice gagne.

# réponse 3.1

# Le nombre total d'issues
issues = 0
# Le nombre d'issues dont on veut calculer la probabilité
counter = 0

# Premier lancer
for i in range(0, 2):
    # Deuxième lancer
    for j in range(0, 2):
        issues += 1

        if i == 0 and j == 0:
            # le premier et le deuxième lancer donne pile
            counter += 1

probability = counter / issues
percentage = probability * 100

print(f"Il y a {percentage:.0f} % de chance d'avoir 2 pile en deux lancers")