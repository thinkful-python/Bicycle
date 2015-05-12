class Bicycle(object):
        """ Information and specifications about a bike """
        def __init__(self, name, weight, cost):
                self.name = name
                self.weight = weight
                self.cost = cost
        def is_affordable(self,customer):
                return self.cost <= customer.wallet

class Shop(object):
        """ Information about the bike shop """
        def __init__(self, name, margin):
                self.name = name
                self.margin = margin
                self.inventory = dict()
        def show_inventory(self):
                for bike, count in self.inventory.iteritems():
                        print ("{0} {1}s left at {2}".format(count, bike.name, bike.cost * self.margin))

        def price(self,bicycle):
                return bicycle.cost * self.margin
        def add_inventory(self, bicycle, count):
                self.inventory[bicycle] = count

class Customer(object):
        """ Information about the customers """
        def __init__(self, name, wallet):
                self.name = name
                self.wallet = wallet
                self.inventory = dict()
        def purchase(self, bike, bicycle):
                self.bike = (bike)
                self.purchase = self.inventory[bicycle]-1