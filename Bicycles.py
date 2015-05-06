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
		self.inventory = []
	def show_inventory(self):
		for bike in self.inventory: 
			print ("%s at cost %d" %(bike.name, bike.cost * self.margin ))
			# print "{} at cost {}".format(bike.name, bike.cost)
	
	def price(self,bicycle):
		return bicycle.cost * self.margin
	def add_inventory(self, bicycle):
		self.inventory.append(bicycle)

class Customer(object):
	""" Information about the customers """
	def __init__(self, name, wallet):
		self.name = name
		self.wallet = wallet