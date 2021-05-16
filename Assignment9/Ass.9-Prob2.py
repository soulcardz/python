class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def Animal_details (self):
        print ("Name: " + self.name)
        print ("Sound: " + self.sound)
        
class Dog (Animal):
    def __init__ (self, name, sound, family):
        Animal.__init__(self, name, sound)
        self.family = family
    def Animal_details (self):
        Animal.Animal_details(self)
        print("Family: " + self.family)

class Sheep (Animal):
    def __init__ (self, name, sound, color):
        Animal.__init__(self, name, sound)
        self.color = color
    def Animal_details (self):
        Animal.Animal_details(self)
        print("Color: " + self.color)
        
        
print ("Printing Animal details for dog:")        
Dog = Dog ("Pongo","Woof Woof","Husky")
Dog.Animal_details()
print ("_____________________________________") 
print ("Printing Animal details for sheep:")
sheep = Sheep ("Billy", "Baaa Baaa", "White")
sheep.Animal_details()