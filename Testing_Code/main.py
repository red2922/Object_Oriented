class CellPhone:
    def __init__(self, manufact = '', model_num = '', retail_p = 0):
        self.__manufact = manufact
        self.__model_num = model_num
        self.__retail_p = retail_p

    # Getters
    def get_manufact(self):
        return self.__manufact

    def get_model_num(self):
        return self.__model_num

    def get_retail_p(self):
        return self.__retail_p

    # Setters
    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model_num(self, model_num):
        self.__model_num = model_num

    def set_retail_p(self, retail_p):
        self.__retail_p = retail_p

    def __str__(self):
        phone_str = """
Manufacturer: {manufact}
Model Number: {model_num}
Retail Price: ${retail_p}
        """.format(manufact = self.__manufact, model_num = self.__model_num, retail_p = self.__retail_p)
        return phone_str

phone_list = []

num = int(input('How many phones do want to know about? '))
for n in range(num):
    manu = input('Enter a manufacturer: ')
    model = input('Enter a Model Number: ')
    price = float(input('Enter a Price: '))

    cell = CellPhone()

    cell.set_manufact(manu)
    cell.set_model_num(model)
    cell.set_retail_p(price)

    phone_list.append(cell)

    for n in phone_list:
        print(n)
