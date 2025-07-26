# exception - An event that interrupts the flow of a program
#            (ZeroDivisionError, ValueError, TypeError, FileNotFoundError, etc.)
#            1. try 2.except 3. finally

try:
    number = int(input("Enter a number: "))
    print(1/number)  # This will raise ZeroDivisionError if number is 0
except ZeroDivisionError:
    print("You cannot divide by zero idiot! ")
except ValueError:
    print("You must enter a number idiot! ")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("No exceptions were raised, so this is executed.")
finally:
    print("This block is always executed, regardless of exceptions.Cleaning up resources or finalizing tasks.")
