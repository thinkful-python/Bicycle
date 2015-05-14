class Bicycle(object):
			""" Information and specifications about a bike """
			def __init__(self, name, weight, cost):
				self.name = name
				self.weight = weight
				self.cost = cost
			def is_affordable(self,customer):
				return self.cost <= customer.wallet
			def __init__(self, name, weight, cost):
				self.name = name
				self.weight = weight
				self.cost = cost
			def customize(self, wheels, frame):
				self.cost = wheels.cost * 2 + frame.cost
				print ("Customizing {} for customer with {} wheels and a {} frame").format(self.name, wheels.model, frame.material)
				
class Shop(object):
	""" Information about the bike shop """
	def __init__(self, name, margin, balance):
		self.name = name
		self.margin = margin
		self.inventory = dict()
		self.balance = balance
	def show_inventory(self):
		for bike, count in self.inventory.iteritems(): 
						print ("Cycle House now has {0} {1}s left at {2} and a balance of {3}".format(count, bike.name, bike.cost * self.margin, self.balance))
						#print ("{0} {1}s left at {2}".format(count, bike.name, bike.cost * self.margin))
			#print("Cycle House now has a balance of {0}".format(self.balance)) 
	def price(self,bicycle):
		return bicycle.cost * self.margin
	def add_inventory(self, bicycle, count):
		self.inventory[bicycle] = count
	def remove_inventory(self, bicycle, count = 1):
				self.inventory[bicycle] = self.inventory[bicycle] - count
	def register(self, amount):
				self.balance = self.balance + amount

class Customer(object):
	""" Information about the customers """
	def __init__(self, name, wallet):
		self.name = name
		self.wallet = wallet
	def purchase(self, bicycle, shop):
			shop.remove_inventory(bicycle)
			self.wallet = self.wallet - shop.price(bicycle)
			shop.register(shop.price(bicycle))
			
class Wheels(object):
	"""Customized Wheels"""
	def __init__(self, model, weight, cost):
		self.model = model
		self.weight = weight
		self.cost = cost
		
class Frames(object):
	"""Customized Frames"""
	def __init__(self, material, weight, cost):
		self.material = material
		self.cost = cost
		self.weight = weight