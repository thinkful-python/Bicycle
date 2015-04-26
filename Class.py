# Unit 1 Final: Bicycle Industry Project 

class Bicycle(object):
	""" Information and specifications about a bike """
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost
	pass

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

	def add_inventory(self, bicycle):
		self.inventory.append(bicycle)

class Customers(object):
	""" Information about the customers """
	def __init__(self, name, wallet):
		self.name = customer.name
		self.wallet = money
	pass

mountain_bike = Bicycle("Mountain Bike", 35, 500)
hybrid_bike = Bicycle("Hybrid Bike", 25, 650)
road_bike = Bicycle("Road Bike", 25, 120)
electric_bike = Bicycle("Electric Bike", 25, 750)

shop = Shop("Cycle House", 1.20)
shop.add_inventory(mountain_bike)
shop.add_inventory(hybrid_bike)
shop.add_inventory(road_bike)
shop.add_inventory(electric_bike)
shop.show_inventory()