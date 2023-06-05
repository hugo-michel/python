# nombre entier, integer. = opérateur d'affectattion
number1 = 123
number1 = 42
print(number1)

#nombre à virgule flottante float
number2 = 3.14
number2 = 2.71
print(number2)

#chaine de caratcere string
text1 = "foo.bar"
print(text1)

text2 = 'bar.bar'
print(text2)

#booleen
python_is_cool = True
print(python_is_cool)

python_is_boring = False
print(python_is_boring)

#null
user_accepted_terms = None
print(user_accepted_terms)

#type de données
print(type(number1))
print(type(number2))
print(type(text1))
print(type(python_is_boring))
print(type(user_accepted_terms))

#verification type donées
print(type(number1) is int)
print(type(number1) is str)
print(type(text1) is bool)
print(type(text1) is str)

#transtipage change un type en un autre
str(number1)
print(type(str(number1)))

print(type(bool(number1)))
print(bool(number1))

number3 = 0
print(bool(number3))

#int(text1)
#print(type(int(text1))) genere une erreur

text3 = "123456789"
print(type(int(text3)))

#les fonctions de transtypage
#str() : converti vers string
#int() : converti vers integer
#bool() : converti vers booleen
#float() : converti vers float
