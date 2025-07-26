# if - do some code only IF some condition is true
#      Else do something else

age = int(input("Enter your age\n"))

if age>= 100:
    print("you are too old man")
elif age>= 18:
    print("You are eligible to signup")
elif age<0:
    print("You haven't even born yet")
else:
    print("You must be 18+ to signup")


response = input("Would you like some food (Y/N)\n")
if response == "Y":
    print("Here Have Some food")
else:
    print("No food for you!")