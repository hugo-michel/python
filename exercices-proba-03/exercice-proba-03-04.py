# exo 3.4
# Rédigez le code qui indique la probabilité que Alice gagne.

# réponse 3.4

issues = 0
counter = 0

for i in range (0,2):
    for j in range (0,2):
        for k in range (0,2):
            issues += 1
            if (i + j + k <= 1):
                counter += 1



probability = counter / issues
percentage = probability * 100

print(f"Il y a {percentage:.0f} % de chance d'avoir au moins deux piles avec trois lancers")