class Bread:  
    def __str__(self):
        return "piece of bread"

# Class to create toast
class Toast:
    def __str__(self):
        return "piece of toast"

# Class to create a bagel
class Bagel:
    def __str__(self):
        return "bagel"

class Household_Application:
    def __init__(self,purchase_price):
        self.__purchase_price = purchase_price

    def get_purchase_price(self):
        return self.__purchase_price

    def do_job(self,object):
        print('The ' + str(object) + ' is done')

class Microwave(Household_Application):
    def do_job(self,object):
        print('The ' + str(object) + ' has been warmed')


class Refrigerator(Household_Application):
    def do_job(self,object):
        print('The ' + str(object) + ' has been cooled')


class Toaster(Household_Application):
    def do_job(self,object):
        if isinstance(object,Bread):
            print(str(object) + ' has been made')
            object = Toast()
            return object

        elif isinstance(object,Bagel):
            print(str(object) + ' has been toasted')

        else:
            print('This ' + str(object) + ' cannot be toasted')

Bad = Bagel()
Good = Bread()

Blender = Household_Application(25)
LG = Microwave(30)
Samsung = Refrigerator(300)
Garbage = Toaster(27)

Blender.do_job(Bad)
LG.do_job(Good)
Samsung.do_job(Bad)
print('The price is ' + str(LG.get_purchase_price()))
print('The price is ' + str(Samsung.get_purchase_price()))

Household_Application(Refrigerator).do_job(Bad)

print(Garbage.do_job(Good))
Garbage.do_job(Bad)






