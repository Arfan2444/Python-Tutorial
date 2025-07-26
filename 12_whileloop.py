# while loop - executes some code while some condition remains true

game = input("Enter your favourite game\n")

while game=="":
    print("You did not Enter anything")
    game = input("Enter your favourite\n")

print("So you like",game)


food = input("Enter your fav food or press q to quit\n")

while not food == "q":
    print("So you like",food)
    food = input("Enter another fav food or press q\n")

print("bye")