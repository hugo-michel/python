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
else:
    print("number1 est plus grand que number2")