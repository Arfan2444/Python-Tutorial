# script 1
#  if __name__ == __main__ - (this script can be imported or run standalone)
#                            Function and classes in this module can be reused
#                            without the main block of code executing
#  if not used then script 1 code will get run in script 2 even if only a functionality is imported from script1

def favouritefood(food):
    print(f"Your favourite food is {food}")

def main():
    # Your code goes her
    print("Script1")
    favouritefood("pizza")
    print("Goodbye")


if __name__ == "__main__":
    main()