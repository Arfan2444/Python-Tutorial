# Membership operator - used to test whether a value or variable is found in a sequence
#                       (string,tuple,set,dictionary,list)
#                       1. in  2. not in


word  = "Apple Iphone"

letter = input("Enter a letter that can be in the word\n")

if letter in word:
    print(f"{letter} is present")
else:
    print(f"{letter} is not present")


# not in - will work exactly opposite of (in), it will check whether the given element is not in the object (true)