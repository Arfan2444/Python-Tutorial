# Decorator - A function that extends the behavior of another function without explicitly modifying it.
# eg: @addSprinkles
#     geticeCream()


def addSprinkles(func): # This is the function will be called directly if wrapper is not implemented
    def wrapper(*args,**kwargs):  # This is the wrapper function that will be called instead of the original function
        print("Adding sprinkles...")
        func(*args, **kwargs) 
    return wrapper  # Return the wrapper function


def addfudge(func):
    def wrapper(*args, **kwargs): 
        print("Adding fudge...")
        func(*args, **kwargs)
    return wrapper

@addfudge
@addSprinkles  # This is the decorator syntax that applies the addSprinkles function to getIceCream
def getIceCream(flavor):
    print(f"Here is your {flavor} ice cream!")

getIceCream("Chocolate")  # Call the decorated function