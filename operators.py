import random



# division entiere

a = 10 //3 # variable = operande operateur operande
print(a) # donne 3 (pas 3.33333)

#puissance

b = 2 ** 3 #2 * 2 * 2
print(b)

#modulo
c = 17 % 5 #17/5 = (15/5) + 2
print(c)

#exemple modulo
c = 50 % 24 #donne 2
print(c)

#nombre pair ou impair

d = 53 # si reste aprés modulo 2 nombre impair
print(53 % 2)
e = 54 #si pas de reste modulo 2 nombre pair
print(54 % 2 )

#operateur de comparison

print(123 == 123) #True
print(123 == 42)  #False

result = 123 == 42
print(result)       #False

print("abc" == "def") #False


#operateur plus grand que 
result2 = 123 > 42
print(result2)

#plus grand ou egal
print(42 >= 42)

#different de
print(42 != 42) #false

#opérateur composé
#incrementation
f = 0
f += 1
f += 1
print(f) #print f = 2

#decrementation
g = 0
g -= 1
print(g) #print -1

#multiplication
h = 3
#h = h * 2
h *= 2 #print 6
print(h)

#division
i = 10
#i = i / 3
i /= 3 #print 3.3333....5
print(i)

j = 10
j //= 3
print(j) #print 3

#operateur inclusion in
text1 ="Lorem ipsum"
print("rem" in text1) #true
print("l" in text1) # false car sensible a la casse

list1 = ["Lorem", "ipsum"]
print("e" in list1) #false
print("ipsum" in list1) #true


# comparaison nombres aléatoires

k = random.randint(0, 100) #0 et 100 inclus
l = random.randint(0, 100)
print(f"{k = : }")
print(f"{l = : }")

result = k == l
print(result)
result = k < l
print(result)

#expression
#1 + 1 -> 2
# (100 + 2 ) * 3 -> 306
# 1 + 1 > (100 + 2) * 3 -> false
#random.randint(0, 100) -> donne un int donc une expression
#print(100) -> pas une expression