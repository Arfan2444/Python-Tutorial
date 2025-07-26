# 2d list is made of lists - [listt1,list2, list3]

fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]
meats = ["chicken", "beef", "fish"]

grocerylist = [fruits,vegetables,meats]

print(grocerylist[0]) # will give the first list (fruits)
# inorder to access specific item in the list we can use two indicies
print(grocerylist[1][2]) # will give the third item in the second list (spinach)


# we can also use a for loop to iterate through the 2d list
for collection in grocerylist:
    for food in collection:
        print(food, end=" ") # will print all items in the 2d list in one line
    print()