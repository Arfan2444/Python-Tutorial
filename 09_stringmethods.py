# String methods help in string operations and string manupulation

name = input("Enter your name\n")
phone = input("Enter your phone no\n")
lengthofstr = len(name)
print("The length of the string is",lengthofstr)

findletter = name.find(" ")
print("Space is on position no",findletter)

lastoccurence = name.rfind("n")
print("Last Occurence of n is on position",lastoccurence)

uppercase = name.upper()
print(uppercase)

lowercase = name.lower()
print(lowercase)

count = phone.count("-")
print("Your phone no contains no of dashes",count)

newphone = phone.replace("-"," ")
print("Your formatted phone no is",newphone)