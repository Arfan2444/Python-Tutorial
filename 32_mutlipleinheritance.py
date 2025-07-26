# multiple inheritance -  inherit from more than one parent class
#                         C(A, B)


# multilevel inheritance - inherit from a parent which itslef inherits from another parent class
#                         C(B) <- B(A) <- A

class Animal:
    def __init__(self,name):
        self.name = name
        self.isalive = True

    def eat(self):
        print(f"{self.name} is eating ")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal): # inherits from Animal
    def flee(self):
        print(f"{self.name} is fleeing!")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting!")

class Rabbit(Prey):
    pass

class Lion(Predator):
    pass

class Wolf(Predator, Prey): # inherits from both Predator and Prey (multiple inheritance)
    pass

rabbit = Rabbit("Bunny")
lion = Lion("Mufasa")
wolf = Wolf("Wolfie")

print(f"{rabbit.name} is a prey and is alive: {rabbit.isalive}")
print(f"{lion.name} is a predator and is alive: {lion.isalive}")


rabbit.sleep()  
rabbit.flee()  
wolf.hunt()   
lion.hunt()    
wolf.flee()  
lion.eat()    
lion.sleep()