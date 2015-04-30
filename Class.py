# Unit 1 Final: Bicycle Industry Project 

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

bikes = []    
bikes.append(Bicycle("Mountain Bike", 35, 120))
bikes.append(Bicycle("Hybrid Bike", 25, 150))
bikes.append(Bicycle("Road Bike", 25, 100))
bikes.append(Bicycle("Electric Bike", 25, 350))


shop = Shop("Cycle House", 1.20)
shop.inventory = bikes
shop.show_inventory()

customers = []
customers.append(Customer("Jerry", 200))
customers.append(Customer("Angela", 500))
customers.append(Customer("Rayden", 1000))

for customer in customers:
	print "{0} can afford these".format(customer.name)
	for bike in shop.inventory:
		if shop.price(bike) <= customer.wallet
      print bike
      

