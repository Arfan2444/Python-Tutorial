# class variables - shared among all instances of a class
#                   Defined outside of __init__ method
#                   Allows you to share data among all objects created from that class


class Hackers:

    # class variable
    tools = ['Nmap', 'Metasploit', 'Wireshark']
    noofhackers = 0

    def __init__(self,name,age,programming_language):
        # instance variables
        self.name = name
        self.age = age
        self.programming_language = programming_language
        Hackers.noofhackers += 1


hacker1 = Hackers('Page Harris',30,'Python')
hacker2 = Hackers('Avi Schulzman',28,'Javascript')
hacker3 = Hackers('John Doe',25,'C++')

print(f"{hacker1.name} is {hacker1.age} years old and uses {hacker1.programming_language}")
print(f"{hacker2.name} is {hacker2.age} years old and uses {hacker2.programming_language}")

print(f"All hackers use the following tools: {Hackers.tools}")

print(f"Total no of hackers: {Hackers.noofhackers}")