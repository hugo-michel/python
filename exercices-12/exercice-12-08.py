# exo 12.8
# Reprenez la classe que vous avez créé pour l'exercice 12.7.
# Créez 3 instances de la classe `TaxIncludedProduct` et affectez les valeurs suivantes à ses attributs en utilisant le constructeur :
# - product1
#   - name: Dolor
#   - price: 31,41
#   - tax: 20,0
# - product2
#   - name: Sit
#   - price: 27,18
#   - tax: 10,0
# - product3
#   - name: Amet
#   - price: 16,18
#   - tax: 5,5

# réponse 12.8

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