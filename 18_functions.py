# functions - a block of reusable code
#             place () after the function name to invoke it


def HappyBirthday(name,age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} old!")
    print("Happy birthday to you!")

# HappyBirthday() will give error as two arguments are required 
HappyBirthday("Bro",28)
HappyBirthday("Steven",30)

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Arfan",42.50,"02/06/25")


# return - statement used to end a function
#          send a result back to caller

def createusername(firstname,lastname):
    firstname = firstname.capitalize()
    lastname = lastname.capitalize()
    return firstname+" "+lastname+" 232"

print("Output:",createusername("bro","code"))