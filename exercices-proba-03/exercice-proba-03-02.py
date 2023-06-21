# exo 3.2
# Bob parie qu'il va obtenir "pile & pile & pile" ou "pile & pile & face" avec 3 lancers.
# Autrement dit, il pense qu'il va obtenir "pile & pile" lors des deux premiers lancers (sur les 3 en tout).
# Rédigez le code qui indique la probabilité que Bob gagne.

# réponse 3.2

issues = 0
counter = 0

for i in range (0,2):
    for j in range (0,2):
        for k in range (0,2):
            issues += 1

            if (i == 0 and j == 0) and (k == 0 or k == 1):
                counter += 1


probability = counter / issues
percentage = probability * 100

print(f"Il y a {percentage:.0f} % de chance d'avoir pile-pile-pile ou pile-pile-face avec trois lancers")