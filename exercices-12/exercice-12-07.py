# exo 12.7
# Créez une classe nommée `TaxIncludedProduct` qui possède les attributs suivants :
# - _name: valeur str transmise par le constructeur
# - _price: valeur float par défaut 0.0
# - _tax: valeur float par défaut 0.0
# et les méthodes suivantes :
# - __init__(name, price, tax) : le constructeur
# - get_name() : renvoie le nom du produit
# - set_name() : détermine le nom du produit
# - get_price() : renvoie le prix du produit
# - set_price() : détermine le prix du produit
# - get_tax() : renvoie la taxe en pourcentage
# - set_tax() :  détermine la taxe en pourcentage (pour une taxe de 20 %, le paramètre doit être 20.0)
# - get_tax_fee() : cette méthode calcule le montant de la taxe et le renvoie ; par exmeple pour un produit de 100 € et une taxe de 20 %, le résultat est 20.0
# - get_tax_included_price() : cette méthode calcule le prix taxe incluse et le renvoie ; par exemple pour un produit de 100 € et une taxe de 20 %, le résultat est 120.0

# réponse 12.7

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

