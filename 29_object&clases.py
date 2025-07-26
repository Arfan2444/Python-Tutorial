# object - A bundle of related attributes (variables) and methods (function)
#          eg - phone, cup, book
#          You need a class to create many objects

# class -  (blueprint) used to design the stucture and layout of the object


class Car: # class
    def __init__(self,model,year ,color,forsale): # constructor (invoked when object is created) 
        self.model = model # self is a reference to the current object and set the attributes
        self.year = year
        self.color = color
        self.forsale = forsale
    
    def accelerate(self):
        print(f"{self.color} {self.model} is accelerating")
    
    def stop(self):
        print(f"{self.color} {self.model} is stopping")
    



car1 = Car("BMW M3 GTR", 2020, "Black", True) # object
car2 = Car("Corvette", 2021,"Black",False)
car3 = Car("Mustang",2022,"Red",True)

print(car1.model,car1.year,car1.color,car1.forsale) # accessing the attributes of the object
print(car2.model,car2.year,car2.color,car2.forsale)
car2.accelerate()
car2.stop()
car3.accelerate()
car3.stop()