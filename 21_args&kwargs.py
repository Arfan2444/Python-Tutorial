# *args - allows you to pass multiple non key arguments
# **kwargs - allows you to pass multiple keyword arguments
#            * unpacking operator


# 1. *args 
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

# print(add(1,2,3,4,5))

def displayname(*args):
    for arg in args:
        print(arg,end="")

# displayname("Dr","Spongebob","SquarePants")


# 2. **kwargs
def printaddress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print(printaddress(street="123 Fake St.", city="Detroit", state="MI", zip="54321"))

