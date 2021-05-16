class Shape:
    # initializer
    def __init__(self, name):
        self.name = name
    def getName(self):
        return ("Shape, ")

class Square (Shape):
    def __init__(self):
        Shape.__init__(self, "Square")
        
    def getName(self):  # overriden method
        return super().getName() + (self.name)

class Circle (Shape):
    def __init__(self):
        Shape.__init__(self, "Circle")
        
    def getName(self):  # overriden method
        return super().getName() + (self.name)


circle = Circle();
print (circle.getName())

square = Square();
print (square.getName())

