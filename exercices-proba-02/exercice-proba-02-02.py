# exo 2.2
# Maintenant, rédigez le code qui indique toutes les issues possibles d'un lancer de dé ainsi que le nombre total d'issues.
# Rappel, les issues possibles pour un lancer de dé sont  : 1, 2, 3, 4, 5 et 6.
# Inspirez-vous de l'exemple 2.2.

# réponse 2.2

counter = 0

for i in range (1, 7):
    counter += 1
    print(i)

print(f"il y a {counter} issues en tout")