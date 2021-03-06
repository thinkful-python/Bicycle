from Bicycles import Bicycle, Shop, Customer, Wheels, Frames

bikes = []
bikes.append(Bicycle("Mountain Bike", 35, 120))
bikes.append(Bicycle("Hybrid Bike", 25, 150))
bikes.append(Bicycle("Road Bike", 25, 100))
bikes.append(Bicycle("Electric Bike", 25, 350))

wheels = []
wheels.append(Wheels("A1900", 1, 75))
wheels.append(Wheels("A500", 3, 60))
wheels.append(Wheels("A100", 5, 45))

frames = [] 
frames.append(Frames("carbon", 7, 100))
frames.append(Frames("aluminum", 10, 75))
frames.append(Frames("steel", 12, 50))

bikes[1].customize(wheels[0], frames[0])

shop = Shop("Cycle House", 1.20, 50000)
for bike in bikes:
  shop.add_inventory(bike, 5)

customers = []
customers.append(Customer("Jerry", 200))
customers.append(Customer("Angela", 500))
customers.append(Customer("Rayden", 1000))

for customer in customers:
        print "{0} can afford these".format(customer.name)
        for bike in shop.inventory:
                if shop.price(bike) <= customer.wallet:
                        print bike.name
                        can_afford = bike
        customer.purchase(can_afford, shop)
        print("{0} bought a {1} at {2} with {3} dollars left".format(customer.name, can_afford.name, shop.price(can_afford), customer.wallet))
        shop.show_inventory()