# Iterables - An object/collection that can return its element one at a time,
#             allowing it to be iterated over in a loop


numbers = [1,2,3,4,5]

for number in reversed(numbers):
    print(number,end=" ")

# similary tuples can be iterated over with as well
# sets can be iterated but since unordered cannot be reversed
print()

name = "Niko Bellic"

for character in name:
    print(character,end=" ")

print()


mydictionary = {"A": 1, "B":2,"C":3}

for key,value in mydictionary.items():
    print(f"{key}:{value}")