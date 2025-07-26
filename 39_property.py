# @property - Decorator used to defind a method as a property (it can be accessed like an attribute)
#             Benefit: add additional logic when getting or setting an attribute
#             Gives you getter, setter and deleter methods


class Rectangle:
    def __init__(self, width, height):
        self._width = width  # Use underscore to indicate private attribute
        self._height = height 
    
    @property # Getter method for width
    def width(self):
        return f"width: {self._width}"

    @property # Getter method for height
    def height(self):
        return f"height: {self._height}"
    
    @width.setter # Setter method for width
    def width(self, newwidth):
        if newwidth > 0 :
            self._width = newwidth
        else:
            print("Width must be positive")

    @height.setter # Setter method for height
    def height(self, newheight):
        if newheight > 0:
            self._height = newheight
        else:
            print("Height must be positive")


    @width.deleter # Deleter method for width
    def width(self):
        del self._width
        print("Width deleted")
    
    @height.deleter # Deleter method for height
    def height(self):
        del self._height
        print("Height deleted")

rectangle = Rectangle(10, 20)

# print(rectangle._width) # Accessing the private attribute directly (not recommended)


rectangle.width = 15  # Using the setter to change width
print(rectangle.width)  # Accessing the property like an attribute

rectangle.height = -5  # Trying to set a negative height (will print an error message)
print(rectangle.height)  # Accessing the property like an attribute

del rectangle.width  # Deleting the width property
del rectangle.height  # Deleting the height property