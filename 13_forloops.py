# for loops - executes a block of code for a fixed number of times
# You can iterate over a range, string, list, tuple, set, or dictionary

for counter in reversed(range(1, 11)):
    print("You are on iteration",counter)
print("Happy New Year")

creditcardno = "1234-5678-9012-3456"

for digit in creditcardno:
    print("The digit is",digit)


for numbers in range(1,20):
    if numbers == 13:
        print("Skipping number 13")
        continue
    else:
        print("you are on",numbers)