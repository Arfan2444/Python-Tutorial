# coditional expression : A one line shortcut for the if-else statement. Print or assgin one or two values based on condition 

num = int(input("Enter a number\n"))

result = "Even" if num % 2 == 0 else "Odd"
print(result)

age = int(input('Enter a age\n'))

status = "Adult" if age >= 18 else "Child"
print(status)