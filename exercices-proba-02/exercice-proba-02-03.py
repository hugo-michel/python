# exo 2.3
# Rédigez le code qui indique toutes les issues possibles de deux lancers successifs d'un seul dé.
# Inspirez-vous des exemples 2.2 et 2.3.

# réponse 2.3

counter = 0


for i in range (1, 7):
    for j in range (1,7):
        counter += 1
        print(i, j)

print(f"il y a {counter} issues en tout")