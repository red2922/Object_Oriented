class Employee:
    def __init__(self,name,number):
        self.__name = name
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def set_name(self,new_name):
        self.__name = new_name

    def set_number(self,new_number):
        self.__number = new_number

    def __str__(self):
        return 'The employee name is:' + self.get_name() + ' The employee number is ' + self.get_number()

class ProductionWorker(Employee):
    def __init__(self,name,number,shift_num = 0,hourly_pay = 0):
        super().__init__(name,number)
        self.__shift_num = shift_num
        self.__hourly_pay = hourly_pay
        self.bonus = 0

    def get_shiftnum(self):
        return self.__shift_num

    def get_hourly_pay(self):
        return self.__hourly_pay

    def set_shiftnum(self,new_shift):
        self.__shift_num = new_shift

    def set_hourly_pay(self,new_pay):
        self.__hourly_pay = new_pay

    def __str__(self):
        return 'The employee name is: ' + self.get_name() + ' ,The employee number is ' + str(self.get_number()) + ' ,The shift num is ' + str(self.get_shiftnum()) + ' , and The hourly pay is ' + str(self.get_hourly_pay())

emp1_name = input('Enter the employee name: ')
emp1_emp_num = input('Enter the employee number: ')
emp1_shift_num = input('Enter 1 for day and 2 for night: ')
emp1_hourly_pay = input('Enter hourly pay: ')

emp1 = ProductionWorker(emp1_name,emp1_emp_num,emp1_shift_num,emp1_hourly_pay)

print(emp1)


hours_per_week = 40

if emp1.get_shiftnum() == 1:
    emp1.bonus = 700
if emp1.get_shiftnum() == 2:
    emp1.bonus = 500

annual_pay = ((hours_per_week * int(emp1.get_hourly_pay())) * 52) + emp1.bonus

print('Annual Pay for ' + emp1.get_name() + ' is ' + str(annual_pay))