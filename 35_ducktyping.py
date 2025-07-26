# Duck typing - another way to achieve polymorphism besides inheritance
#               Objects must have the minimum necessary attributes and methods
#               if it looks like a duck and quacks like a duck, it is a duck


class Animal:
    isalive = True

class Duck(Animal):
    def speak(self):
        print("Quack")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:
    # Car doesnt inherit from Animal, but it has the necessary method and attributes
    isalive  = False
    def speak(self):
        print("Vroom")

animals = [Duck(), Cat(), Car()]

for animal in animals:
# If we try to add an object that does not have the speak method, it will raise an AttributeError
    animal.speak()  # This will work because all objects have a speak method
    print(f"Is the animal alive? {animal.isalive}")  # This will work because all objects have the isalive attribute
