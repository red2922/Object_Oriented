from abc import ABC, abstractmethod
import math
import numpy as np

class Shape(ABC):
    def __init__(self,color):
        self.__color = color

    def get_color(self):
        return self.__color

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_dimensions(self):
        pass


class Square(Shape):
    def __init__(self,color,length):
        super().__init__(color)
        self.__length = length

    def get_length(self):
        return self.__length

    def get_area(self):
        l = self.get_length()
        area = l * l
        return area

    def get_perimeter(self):
        l = self.get_length()
        perimeter = l * 4
        return perimeter

    def get_dimensions(self):
        return 'The length and width of the square is ' + self.get_length()

    def __str__(self):
        return 'The color of the square is: ' + self.get_color() + \
               '. The length of the sides are: ' + str(self.get_length())

    def __repr__(self):
        return "Square(" + str(self.get_length()) + ")"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def get_area(self):
        r = self.get_radius()
        area = math.pi * (r**2)
        return round(area,3)

    def get_perimeter(self):
        r = self.get_radius()
        perimeter = 2 * math.pi * r
        return perimeter


    def get_dimensions(self):
        return 'The radius of the circle is ' + str(self.get_radius())

    def __str__(self):
        return 'The color of the circle is ' + self.get_color() + '. The radius is ' + str(self.get_radius())

    def __repr__(self):
        return "Circle(" + str(self.get_radius()) + ")"

class Triangle(Shape):
    def __init__(self,color,s1,s2,s3):
        super().__init__(color)
        self.__s1 = s1
        self.__s2 = s2
        self.__s3 = s3

        self.__tri_array = np.array([s1,s2,s3])

    def get_s1(self):
        return self.__s1
    def get_s2(self):
        return self.__s2
    def get_s3(self):
        return self.__s3

    def get_dimensions(self):
        return self.__tri_array

    def get_area(self):
        s = (self.get_perimeter()/2)
        area = math.sqrt(s* (s - self.get_s1())*(s - self.get_s2())*(s-self.get_s3()))
        return round(area,3)

    def get_perimeter(self):
        return sum(self.get_dimensions())


    def __str__(self):
        return "The color of the triangle is " + self.get_color() + ". The dimensions of the triangle is " \
               + str(self.get_s1()) + ', ' + str(self.get_s2()) + ', ' + str(self.get_s3())

    def __repr__(self):
        return "Triangle(" + str(self.get_s1()) + ', ' + str(self.get_s2()) + ', ' + str(self.get_s3()) + ')'

a = Square('Blue', 47)
b = Circle('Red', 23.5)

t1 = Triangle('Purple',3,4,5)
t2 = Triangle('Green',19,19,19)
t3 = Triangle('Cyan',4,4,5)


tri_list = [t1,t2,t3]

for i in tri_list:
    print(i)
    print('Area is: ' + str(i.get_area()))
    print('Perimeter is: ' + str(i.get_perimeter()))

    leftover = a.get_area() - b.get_area()
    print(round(leftover, 3))



#print(t2.get_perimeter())
#print (round(t2.get_area(),3))

print(a)
for tri in tri_list:
    count = 0
    for s in tri.get_dimensions():
        if s == tri.get_s1():
            count += 1
        if s == tri.get_s2():
            count += 1
        if s == tri.get_s3():
            count += 1
        break

    if count == 1:
        type = 'Scalene'
    if count == 2:
        type = 'Isoscles'
    if count == 3:
        type = 'Equilateral'

    print(tri.__repr__() + ' is a ' + type + ' triangle')