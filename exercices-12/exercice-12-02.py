# exo 12.2
# Reprenez la classe que vous avez créé pour l'exercice 12.1.
# Créez 4 instances de la classe `User` et affectez les valeurs suivantes à ses attributs :
# - user1
#   - firstname: Joe
#   - lastname: Dalton
#   - email: joe.dalton@example.com
#   - newsletter: true
# - user2
#   - firstname: William
#   - lastname: Dalton
#   - email: william.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: Jack
#   - lastname: Dalton
#   - email: jack.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: Avrel
#   - lastname: Dalton
#   - email: avrel.dalton@example.com
#   - newsletter: true

# réponse 12.2

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

user1 = User("Joe", "Dalton", "joe.dalton@example.com", True)
user2 = User("William", "Dalton", "william.dalton@example.com", False)
user3 = User("Jack", "Dalton", "jack.dalton@example.com", False)
user4 = User("Avrel", "Dalton", "avrel.dalton@example.com", True)