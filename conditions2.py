while True:
    user_age = input("quel est votre age ? ")  #rempli variable avec input

    try:                                       #test pour erreurs
        user_age = int(user_age)
        break
    except:                                    #handle error
        pass

print(f"Vous avez {user_age} ans")

#########

while True:
    user_has_payment = input("Avez vous un moyen de paiement ? [o/n] ")
    if user_has_payment == "o":
        user_has_payment = True
        break
    elif user_has_payment == "n":
        user_has_payment = False
        break
print(user_has_payment)

#######

film1 = (user_age, user_has_payment)
user1 = (16, True)

if film1[0] > 0:
    print("un age minimum est requis")
    if user1[0] >= film1[0]:
        print("l'utilisateur a l'age requis")
    else:
        print("l'utilisateur n'a pas l'age requis")
        print("l'utilisateur ne peut pas regarder le film")
        exit()
else:
    print("un age minimum n'est pas requis")

if film1[1] == True:
    print("un moyen de paiement est necessaire")
    if user1[1] == True:
        print("l'utilisateur a un moyen de paiment")
    else:
        print("l'utilisateur n'a pas de moyen de paiement")
        print("l'utilisateur ne peu pas regarder le film")
        exit()
else:
    print("un moyen de paiement n'est pas necessaire")
