class Rectangle_opts:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area_of_rec(self):
        return self.__length * self.__width

    def perimeter_of_rec(self):
        return (self.__length * 2) + (2 * self.__width)
p1 = Rectangle_opts (4,5)
print (p1.area_of_rec())
print (p1.perimeter_of_rec())