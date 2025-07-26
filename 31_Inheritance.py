# Inheritance - allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent):

# Parent class
class Animal:
    def __init__(self,name):
        self.name = name
        self.isalive = True
    
    def eat(self):
        print(f"{self.name} is eating ")
    
    def sleep(self):
        print(f"{self.name} is sleeping")


# Child classes inheriting from Parent class Animal
class Dog(Animal): # Inherits from Animal
    def bark(self):
        print(f"{self.name}:Woof! Woof!")

class Cat(Animal): # Inherits from Animal
    def meow(self):
        print(f"{self.name}:Meow! Meow!")

class Mouse(Animal): # Inherits from Animal
    def squeak(self):
        print(f"{self.name}:Squeak! Squeak!")


dog = Dog("Snoopy")
cat = Cat("Beluga")
mouse = Mouse("Geronimo")

print(f"{dog.name} is a dog and is alive: {dog.isalive}")
print(f"{cat.name} is a cat and is alive: {cat.isalive}")
print(f"{mouse.name} is a mouse and is alive: {mouse.isalive}")

dog.eat()
cat.sleep()
dog.bark()
cat.meow()
mouse.squeak()