# Polymorphism - Greek word that means to "have many forms or faces"

#       Two ways to implement polymorphism in Python:
#       Inheritance - An object can be treated of the same type as its parent class
#       Duck typing - Object must have necessary attributes and methods

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod # Abstract class - need to implement this method in subclasses inheriting from this class
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        print( 3.14 * self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        print( self.side ** 2)

class Triangle(Shape):
    def __init__(self,base, height):
        self.base = base
        self.height = height
    
    def area(self):
        print( 0.5 * self.base * self.height)
    
class Pizza(Circle):
    def __init__(self,toppings,radius):
        super().__init__(radius)
        self.toppings = toppings
        

shapes = [Circle(5), Square(4), Triangle(3, 6),Pizza("pepperoni", 3)]

for shape in shapes:
    shape.area()