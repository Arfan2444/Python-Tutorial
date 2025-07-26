# script 2
from ifname_main2 import *

def favouritedrink(drink):
    print(f"Your favourite drink is {drink}")

print("This is script 2")
favouritefood("burger")
favouritedrink("fanta")

# imported favuritefood() will run script 1 code if script 1 doesnt contain 'if __name__ == "__main__":' 