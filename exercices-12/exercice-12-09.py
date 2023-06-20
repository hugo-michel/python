# exo 12.9
# Reprenez la classe que vous avez créé pour l'exercice 12.7 et les
# instances que vous avez créé dans l'exercice 12.8.
# Ajoutez chacune des instances de la classe `TaxIncludedProduct` à une liste nommée `products`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom, le prix (sans la taxe), la taxe et le prix taxe incluse de chaque produit
# Calculez :
# - la somme du prix des produits sans les taxes
# - la somme du montant des taxes
# - la somme du prix des produits taxes incluses
# Et affichez-en des arrondis à 2 chiffres après la virgule, après la boucle `for`

# réponse 12.9

class TaxIncludedProduct:

    def __init__(self, _name : str = "", _price : float = 0.0, _tax : float = 0.0):
        self._price = _price
        self._tax = _tax
        self._name = _name
    
    def get_name(self):
        return self._name
    
    def set_name(self, _name):
        self._name = _name
    
    def get_price(self):
        return self._price
    
    def set_price(self, _price):
        self._price = _price

    def get_tax(self):
        return self._tax
    
    def set_tax(self, _tax):
        self._tax = _tax

    def get_tax_fee(self):
        return (self._price * self._tax) / 100
       
    def get_tax_included_price(self):
        return self._price + ((self._price * self._tax) / 100)

product1 = TaxIncludedProduct()
product1.set_name("Dolor")
product1.set_price(31.41)
product1.set_tax(20.0)

product2 = TaxIncludedProduct()
product2.set_name("Sit")
product2.set_price(27.18)
product2.set_tax(10.0)

product3 = TaxIncludedProduct()
product3.set_name("Amet")
product3.set_price(16.18)
product3.set_tax(5.5)

totalHt = 0
totalTaxe = 0
totalTtc = 0
products = [product1, product2, product3]

for i in products:
    print(i._name, i._price, i.get_tax_fee(), i.get_tax_included_price())
    totalHt += i._price
    totalTaxe += i.get_tax_fee()
    totalTtc += i.get_tax_included_price()

print(f"total hors taxe : {round(totalHt, 2)}")
print(f"total des taxes : {round(totalTaxe, 2)}")
print(f"total TTC : {round(totalTtc, 2)}")
