"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = 0
        if qty <= 3:
            total = 5 * qty  # TODO, calculate the real amount!
        else:
            total = (5 * qty) * 0.75
        return total

w = WatermelonOrder()
print w.get_price(qty = 5)


class CanteloupeOrder(object):
    species = "Canteloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered. Canteloupe's """
        if qty >= 5:
            total = 5 * qty  # TODO, calculate the real amount!
        else:
            total = (5 * qty) * 0.75
        return total

class CasabaOrder(object):
    species = "Casaba"
    color =  "green"
    imported =  True
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self,qty):
        """Determine price for this quantity of melons of this type.Return a float of the total price.
        """
        total = float(6*1.5 * qty)  # TODO, calculate the real amount!
        return total

p = CasabaOrder()
print p.get_price(5)    
 

class SharlynOrder(object):
    species = "Sharlyn"
    color =  "tan"
    imported =  True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price."""
        total = float(5*1.5 * qty)  # TODO, calculate the real amount!
        return total

s = SharlynOrder()
print s.get_price(5)   

class Santa_ClausOrder(object):
    species = "Santa_Claus"
    color =  "green"
    imported =  True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price."""
        total = float(5*1.5 * qty)  # TODO, calculate the real amount!
        return total

sa = Santa_ClausOrder()
print sa.get_price(5)   
         
class ChristmasOrder(object):
    species = "Christmas"
    color =  "green"
    imported =  False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self,qty):
        """Determine price for this quantity of melons of this type.

        Return a float of the total price.
        """
        total = 5* qty
        return total
we = ChristmasOrder()
print we.get_price(3)         

class Horned_MelonOrder(object):
    species = "Horned_Melon"
    color =  "yellow"
    imported =  True
    shape = 'square'
    seasons = ['Summer']

    def get_price(qty):
        """Determine price for this quantity of melons of this type.Return a float of the total price.
        """
        total = ((5*2)*1.5) * qty  # TODO, calculate the real amount!
        return total


class XiguaOrder(object):
    species = "Xigua"
    color =  "black"
    imported =  True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.Return a float of the total price.
        """
        total = (5 * 1.5)
        return total

x = XiguaOrder()
print x.get_price(5)    

class OgenOrder(object):
    species = "Ogen"
    color =  "tan"
    imported =  False
    shape = 'natural'
    seasons = ['Spring', 'Summer']        

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type. Return a float of the total price.
        """
        total = 0
        total = 6 * qty  # TODO, calculate the real amount!
    
        return total

r = OgenOrder()
print r.get_price(5)




