# super() = Function used in a child class to call methods from a parent class
#           Allows you to extend the functionality of the parent class method

class Shape:
    def __init__(self,color,isfilled):
        self.color = color
        self.isfilled = isfilled
    def describe(self):
        print(f"This shape is {self.color} and {'filled' if self.isfilled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, isfilled, radius):
        # Call the parent class constructor
        super().__init__(color,isfilled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, isfilled, side):
        # Call the parent class constructor
        super().__init__(color,isfilled)
        self.side = side

class Rectangle(Shape):
    def __init__(self,color, isfilled, width, height):
        # Call the parent class constructor
        super().__init__(color,isfilled)
        self.width = width
        self.height = height
    
    # Method overriding - allows you to change the behavior of a parent class method
    def describe(self):
        super().describe()  # Call the parent class describe method
        print(f"The area of the rectangle is {self.width * self.height}")
        


circle = Circle("Blue",False,3)
square = Square("Green", True, 5)
rectangle = Rectangle("Red", True, 10,20)

print(circle.isfilled)
print(rectangle.color)
print(square.side)
print(circle.radius)



circle.describe()
square.describe()
rectangle.describe()