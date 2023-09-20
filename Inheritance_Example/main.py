class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, hrpay = 15.0):
        self.first = first
        self.last = last
        self.hrpay = hrpay
        self.email = last + first + '@lopers.unk.edu'

    def full_name(self):
        return'{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.hrpay = int(self.hrpay * self.raise_amt)

class Developer(Employee):
    raise_amt = 2.5 #This overwrites the raise_amt in the Employee. This overide does not effect other classes

    def __init__(self ,first, last,prog_lang, hrpay = 15.0):
        super().__init__(first, last, hrpay) #MAKES SURE THAT IT TAKES DIRECTLY FROM THE PARENT CLASS. More common
        self.prog_lang = prog_lang

        #can also do Employee.__init__(self,first,last,hrpay). The same as the super() constructor.

class Manager(Employee):

    def __init__(self, first, last, employees, hrpay = 15.0): #constructor method
        super().__init__(first, last, hrpay)
        self.employees = employees

    def add_emp(self,dev):                                  #instance method
        if dev not in self.employees:
            self.employees.append(dev)

    def remove_emp(self,dev):
        if dev in self.employees:
            self.employees.remove(dev)

    def print_emps(self):
        for dev in self.employees:
            print('Name: ' + dev.full_name())


dev1 = Developer('Rose', 'Kamiyama','C++', 123.0)

print(dev1.full_name())
print(dev1.email)
dev1.apply_raise()
print(float(dev1.hrpay))

mngr1 = Manager('Red', ' Kamiyama', [dev1], 500.0)

mngr1.print_emps()
