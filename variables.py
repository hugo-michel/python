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

#transtypage change un type en un autre
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

#string multilignes
texte4 = """<div>
      <h1></h1>
</div>
"""

print(texte4)

#\n saut de ligne
#\t tabulation
texte5 = "<div>\n\t<h1></h1>\n</div>"
print(texte5)

#caractere echappement
#\\ = \
#\" = "
texte6 = "C\ProgramsFiles"
print(texte6)

texte7 = "Foo \"Bar\" Baz"
print(texte7)

#exo permutez la valeure des deux variables
a = 123
b = 42
temp = a
a = b
b = temp
print("a" , a)
print("b" , b)

a = 123
b = 42
a = a + b
b = a - b
a = a - b
print("a" , a)
print("b" , b)

a = 123
b = 42
c = a
d = b
a = d
b = c
print("a" , a)
print("b" , b)


#arrondi float
import decimal
from decimal import Decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP
print(Decimal("0.5").quantize(Decimal("1"))) # Decimal('1')
print(Decimal("1.5").quantize(Decimal("1"))) # Decimal('2')
print(Decimal("0.125").quantize(Decimal("0.1"))) # Decimal('0.1')

