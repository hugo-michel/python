import random
electricity_off = bool(random.randint(0, 1))
water_off = bool(random.randint(0, 1))
print(electricity_off)
print(water_off)


#and
if electricity_off and water_off:
    print("vous pouvez partir en vacances")
else:
    print("vous ne pouvez pas partir en vacances")

#not
if electricity_off and water_off:
    print("vous pouvez partir en vacances")
elif not electricity_off and water_off:
    print("il faut éteindre l'électricité")
elif electricity_off and not water_off:
    print("il faut couper l'eau")
else:
    print("il faut éteindre l'électricité et couper l'eau")


if True:
    print("le message s'affichera toujours")

if False:
    print("le message ne s'affichera jamais")

number1 = random.randint(0,10)
number2 = random.randint(0,10)
print(f"{number1 = }")
print(f"{number2 = }")
if number1 < number2:
    print("number1 est plus petit que number2")
elif number1 > number2:
     print("number1 est plus grand que number2")
else:
    print("number1 est egal à number2")


# reecriture
if number1 < number2:
    print("number1 est plus petit que number2")
else:
    if number1 > number2:
        print("number1 est plus grand que number2")
    else:
        print("number1 est egal à number2")


#opérateurs booleens
print(not True) #donne false
print(not False) #donne true

#Table de vérité  de not
#A      not A
#True   False
#False  True

# OU logique
print(True or True)
print(True or False)
print(False or False)
#table de vérité OR
#A  B   AorB
#T  T   T
#T  F   T
#F  T   T
#F  F   F

# AND
print(True and True)
print(True and False)
print(False and False)
#table vérité AND et #NAND not and
#A  B   AandB   NAND
#T  T   T       F
#T  F   F       T
#F  T   F       T
#F  F   F       T



