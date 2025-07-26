# Static methods - A method that belongs to the class rather than any object from that class (instance)
#                  Used for general utility functions

# Instance methods - Best for operations on instances of the class
# Static methods - Best for utility functions that don't need access to instance or class data

class Employee:
    def  __init__(self,name, position):
        self.name = name
        self.position = position
    
    def display_info(self):
        print(f"Emplyee Name: {self.name}, Position: {self.position}")
    
    @staticmethod # Static method to validate position
    def is_valid_positon(position):
        valid_positions = ["Manager", "Developer", "Designer", "Tester"]
        return position in valid_positions
    
print(Employee.is_valid_positon("Manager")) # True
print(Employee.is_valid_positon("Intern")) # False

employee1 = Employee("Alice", "Developer")
employee2 = Employee("Bob", "Manager")

employee1.display_info()  # Employee Name: Alice, Position: Developer
employee2.display_info() # Employee Name: Bob, Position: Manager