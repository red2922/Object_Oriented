
class Information:
    def __init__(self,name, age, phone, address = "unknown"):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone = phone

#Getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
#Setters
    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def set_address(self, address):
            self.__address = address

    def set_phone(self,phone):
        self.__phone = phone

    def __str__(self):
        info_str = str("Name: " + self.get_name() + " - age: " + str(self.get_age()) + " -address: " + self.get_address())
        return info_str

    def display_info(self):
        print("Name: " + self.get_name())
        print("Age: " + str(self.get_age()))
        print("Address: " + self.get_address())
        print("Phone: " + self.get_phone())
        print('\n')


c1 = Information('Alec Paul', 20, '3083338948', '2002 West Drive')
c2 = Information('Rose Kamiyama', 18, '3083900715', '4004 East Drive')

c1.display_info()

c2.display_info()

print(c2)

class RetailItem:
    retail_list = []
    def __init__(self):
        self.__description = ''
        self.__Units = 0
        self.__Price = 0

    #Getters
    def get_des(self):
        return self.__description

    def get_units(self):
        return self.__Units

    def get_Price(self):
        return float(self.__Price)

    #Setters
    def set_des(self,desc):
        self.__description = desc

    def set_units(self,units):
        self.__Units = units

    def set_Price(self,price):
        self.__Price = price

    def __str__(self):
        retail_str = str(self.get_des() + "  " + str(self.get_units()) + "  $" + str(self.get_Price()))
        return retail_str

#Make this input and store into a list

print('\n')
"""
num = int(input('How many retail items are on sale? '))
for n in range(num):
    desc = input('Enter a description: ')
    unit = int(input('Enter stock: '))
    price = float(input('Enter a Price: '))

    item = RetailItem()

    item.set_des(desc)
    item.set_units(unit)
    item.set_Price(price)

    RetailItem.retail_list.append(item)
"""

item1 = RetailItem()
item1.set_des('Jacket')
item1.set_units(12)
item1.set_Price(59.95)

item2 = RetailItem()
item2.set_des('Designer Jeans')
item2.set_units(40)
item2.set_Price(34.95)

item3 = RetailItem()
item3.set_des('Shirt')
item3.set_units(20)
item3.set_Price(24.95)

item = [item1,item2,item3]

print('\n')
print('Items for sale: ')
for i in item:
    print (i)

class CashRegister:

    def __init__(self):
        self.__Items = []

    def get_itemlist(self):
        return self.__Items

    def purchase_item(self,item):
        self.__Items.append(item)

    def get_total(self):
        t = 0.0
        for i in self.get_itemlist():
            t = t + i.get_Price()
        return t

    def show_items(self):
        for i in self.get_itemlist():
            print(i)

    def clear(self):
        self.__Items.clear()
        print("Transaction complete. Thank you for shopping with us!!!")

#for main ask for input to determine what will be in the item list.
receipt = CashRegister()

try:
    n = int(input("How many items are you buying? "))

except ValueError:
    print("Please enter a valid number")
    n = int(input("How many items are you buying? "))
else:
    print("\n")

    for i in range(n):

        while True:
            take = input("What item are you buying? ")
            if take == 'item1' or take == 'Jacket':
                receipt.purchase_item(item1)
                break
            elif take == 'item2' or take == 'Designer Jeans':
                receipt.purchase_item(item2)
                break
            elif take == 'item3' or take == 'Shirt':
                receipt.purchase_item(item3)
                break
            else:
                print('Item does not exist. Enter it again')

    receipt.show_items()

    print('Total: $' + "{:.2f}".format(receipt.get_total()))

    receipt.clear()
