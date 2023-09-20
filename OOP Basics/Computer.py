class Computer:
    def __init__(self,p1,g1,r1,s1):
        self.processor = p1
        self.graphics_card = g1
        self.ram = r1
        self.storage = s1


#instance = object
hp = Computer('r7','1660ti','16gb','512gb') #How to define objects


macbook = Computer('M1','Integrated','8gb','1tb')

acer = Computer('i5','Integrated','8gb','256gb')

print(hp.__dict__)
#print(type(comp1))

