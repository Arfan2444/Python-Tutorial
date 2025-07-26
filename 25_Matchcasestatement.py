# Match case statement (switch) - An alternative to using many 'elif' statements
#                                 executes some code if a value matches a 'case'
#                                 Benefits: cleaner and more readable syntax


def dayofweek():
    day = int(input("Enter a day no(1-7)\n"))
    match day:
        case 1:
            return "It's Sunday"
        case 2:
            return "It's Monday"
        case 3:
            return "It's Tuesday"
        case 4:
            return "It's Wednesday"
        case 5:
            return "It's Thursday"
        case 6:
            return "It's Friday"
        case 7:
            return "It's Saturday"
        case _:
            return "Not a valid day"

# print(dayofweek())

def isweekend():
    day = input("Enter a day to check if its weekend or not:")
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" | "Saturday":
            return False
        case _:
            return False

print(isweekend())