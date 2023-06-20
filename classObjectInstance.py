# #creation classe, 2 attributs, 1 méthode
# class Utilisateur:
#     statut = "Inscrit"
#     age = 0

#     def setNom(self, n):
#         self.nom = n

# #création instance (=objet) ds la classe
# pierre = Utilisateur()
# mathilde = Utilisateur()

# #
# print(pierre.statut) #print Inscrit
# print(pierre.age)    #print 0
# print(mathilde.statut)
# print(mathilde.age)

# pierre.setNom("Pierre")
# print(pierre.nom)    #print "Pierre"

# #changement attribut et nouveau attribut d'un objet
# pierre.statut = "Admin"
# print(pierre.statut) #renvoie "Admin" (a écrasé "Inscrit")
# pierre.sexe = "Homme" #nouvel attriubut pour l'objet pierre
# print(pierre.sexe) 
# # mathilde.sexe     #l'objet mathilde de la classe Utilisateur n'a pas d'attribut sexe => erreur

class Utilisateur:
    anciennete = 0

    def __init__(self, nom, age):
        self.user_name = nom
        self.user_age = age
    
    def getNom(self):
        print("Salut, je suis ", self.user_name)

pierre = Utilisateur("Pierre", 29)
mathilde = Utilisateur("Mathilde", 27)

print(pierre.user_name)
print(mathilde.user_age)
print(mathilde.anciennete)
pierre.getNom()

#création d'une sous classe (enfant de la classe Utilisateur)
class Client(Utilisateur):
    is_client = True
#Client hérite de ttes les variables et fonctions d'Utilisateur : name, age, getNom
#On peut rajouter des attributs et méthodes uniquement pour la sous classe : is_client
hugo = Client("Hugo", 34)
print(hugo.user_name)
print(hugo.user_age)
print(hugo.is_client)
hugo.getNom()

#surcharge
class Client(Utilisateur):
    is_client = True
    # anciennete = 10     mauvais car existe deja dans la classe mere

    def __init__(self, nom, age, mail):
        # self.user_name = nom              mauvais car existe deja dans la classe mere
        # self.user_age = age
        Utilisateur.__init__(self, nom, age)    #appel de la méthode __init__ de Utilisateur()
        self.user_mail = mail                   #rajout de l'attribut à la sous classe Client

    def getNom(self):
        print("Je suis ", self.user_name, ". Mon mail est : ", self.user_mail)

adrien = Client("Adrien", 29, "adrien@gmail.com")
print("ancienneté : ", adrien.anciennete, " ans. ")
print(adrien.user_mail)
adrien.getNom()

#test type instance avec fonction isinstance() : savoir si objet appartient à une classe
#idem avec issubclass : si une classe est enfant d'une autre
#renvoie True ou False
print(isinstance(pierre, Client)) #renvoie false
print(isinstance(pierre, Utilisateur)) #renvoie True
print(issubclass(Client, Utilisateur)) #true : Client est enfant de Utilisateur


#polymorphisme
class Animaux:
    def __init__(self, nom):
        self.animal_nom = nom
    
    def seNourrir(self):
        faim = True
        while faim == True:
            self.manger = True
    
    def seDeplacer(self):
        pass                        #ne fait rien, evite une erreur

