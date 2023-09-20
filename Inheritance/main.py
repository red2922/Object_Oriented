class Restaurant:

    def __init__(self,name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        print(self.name + ' is now open!!!' + '\n')

    def describe_restaurant(self):
        print('Name: ' + self.name + '\n' + 'Cuisine type: ' + self.cuisine_type)

    def __str__(self):
        return self.name + ' ' + self.cuisine_type

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type, flavors = []):
        super().__init__(name,cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        for flavors in self.flavors:
            print(flavors)

    def __str__(self):
        return self.name + ' ' + self.cuisine_type + ' ' + self.flavors

class Automobile:

    def __init__(self,make, model, mileage = 0.0, price = 0.0):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    def set_make(self,make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_milage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

class Car(Automobile):
    def __init__(self,make, model, mileage = 0.0,price = 0.0,doors = 1):
        super().__init__(make, model, mileage, price)
        self.__doors = doors

    def set_doors(self,doors):
        self.__doors = doors

    def get_doors(self):
        return self.__doors

class Truck(Automobile):

    def __init__(self,make, model, drive_type, mileage = 0.0,price = 0.0):
        super().__init__(make, model, mileage, price)
        self.__drive_type = drive_type

    def set_drive_type(self, drive_type):
            self.__drive_type = drive_type

    def get_drive_type(self):
            return self.__drive_type


class SUV(Automobile):

    def __init__(self, make, model, pass_cap, mileage=0.0, price=0.0):
        super().__init__(make, model, mileage, price)
        self.__pass_cap = pass_cap

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    def get_pass_cap(self):
        return self.__pass_cap


r1 = Restaurant('Chinese Buffet', 'Chinese')
r2 = Restaurant('Sushi First', 'Sushi Bar')

i1 = IceCreamStand('MOOOO Ice Cream', 'Dessert', ['Chocolate', 'Vanilla', 'Mint'])

print(r1)
print(r2)
print('\n')

r1.describe_restaurant()
r1.open_restaurant()

r2.describe_restaurant()
r2.open_restaurant()

i1.describe_restaurant()
i1.display_flavors()

