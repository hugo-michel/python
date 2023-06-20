# exo 12.6
# Reprenez la classe que vous avez créé pour l'exercice 12.4 et les
# instances que vous avez créé dans l'exercice 12.5.
# Ajoutez chacune des instances de la classe `TaxFreeProduct` à une liste nommée `products`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom et le prix de chaque produit
# Calculez la somme du prix des produits et affichez-en un arrondi à 2 chiffres après la virgule, après la boucle `for`

# réponse 12.6

class TaxFreeProduct:
    def __init__ (self, _name = "", _price = 0.0):
        self._name = _name
        self._price = _price
    
    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price
    
    def set_name(self, _name):
        self._name = _name
    
    def set_price(self, _price):
        self._price = _price

product1 = TaxFreeProduct()
product1.set_name("Foo")
product1.set_price(31.41)

product2 = TaxFreeProduct()
product2.set_name("Bar")
product2.set_price(27.18)

product3 = TaxFreeProduct()
product3.set_name("Baz")
product3.set_price(16.18)

products = [product1, product2, product3]

total = 0
for i in products:
    print(i._name, i._price)
    total += i._price
print(f"total : {round(total, 2)}")