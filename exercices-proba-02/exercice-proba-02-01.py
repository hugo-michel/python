# exo 2.1
# Reprenez le code 2.3 et ajoutez-y un compteur pour calculer le nombre total d'issues.
# Inspirez-vous de l'exemple 2.2.

# réponse 2.1

counter = 0

# Premier lancer
for i in range(0, 2):
    # Deuxième lancer
    for j in range(0, 2):
        counter += 1
        if i == 0:
            # Le premier lancer donne pile
            # Le paramètre end='' permet de ne pas passer à la ligne
            print("pile", end='')
        else:
            # Le premier lancer donne face
            # Le paramètre end='' permet de ne pas passer à la ligne
            print("face", end='')

        if j == 0:
            # Le deuxième lancer donne pile
            print(" & pile")
        else:
            # Le deuxième lancer donne face
            print(" & face")

print(f"il y a {counter} issues en tout")