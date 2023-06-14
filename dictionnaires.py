#declaration dict vide
fruits = {}

#declaration dict avec contenu
fruits = {
    "an" : "ananas", 
    "ba" : "banane",
    "ci" : "citron"
}
print(f"dict fruits : {fruits}")
print(type(fruits))

#parcourir un dict avec for renvoie les key
for key in fruits:
    print(key)

for key in fruits.keys():
    print(key)

for fruit in fruits.values():
    print(fruit)

for key, fruit in fruits.items():
    print(key,fruit)

#ATTENTION : un dict n'est pas ordonné donc pas triable

#ajout d'une key et d'une valeur : differents fromats de keys et de valeurs sont possible
fruits["d"] = "datte"
fruits[32.5] = 32.5
fruits["car"] = ["porshe", "ferrari"]
for key, fruit in fruits.items():
    print(key,fruit)

#suppression d'une entrée

if "b" in fruits:
    del fruits["b"]   #ne change rien, ne repère pas "b" in "ba" ou "banane"
print(fruits)


# if "d" in fruits:
#     del fruits["d"]   #supprime l'entrée "d" ATTENTION : mettre la key et nom pas la value
# print(fruits)

if "car" in fruits:
    del fruits["car"]   #del fonctionne aussi pour tous autres type de key
print(fruits)

print("a" in fruits)    #renvoie False car pas de key "a"
print("an" in fruits)   #renvoie True car "an" is a key

print("c" in fruits.keys())     #renvoie false
print("ci" in fruits.keys())    # renvoie True

print("citron" in fruits.values())      # renvoie true : "citron" existe en value dans dict
print("ci*" in fruits.values())         #False : les jokers ne focntionnent pas

##exemple dict dans une liste

users = [
    {
        'id': 1,
        'email': 'foo@example.com'
    },
    {
        'id': 2,
        'email': 'bar@example.com'
    },
    {
        'id': 3,
        'email': 'baz@example.com'
    }
]

for user in users:
    for key, value in user.items():
        print(f"{key}: {value}")

print(type(users[0]))