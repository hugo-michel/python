# exo 12.1
# Créez une classe nommée `User` qui possède les attributs suivants :
# - firstname: valeur par défaut ''
# - lastname: valeur par défaut ''
# - email: valeur par défaut ''
# - newsletter: valeur par défaut False
# et la méthode suivante :
# - __init__() : le constructeur
# Pas la peine de créer de getters et de setters

# réponse 12.1

class User:
    firstname = " "
    lastname = " "
    email = " "
    newsletter = False


    def __init__(self, firstname, lastname, email, newsletter):
        self.user_firstname = firstname
        self.user_lastname = lastname
        self.user_email = email
        self.user_newsletter = newsletter
