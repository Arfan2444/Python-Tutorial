# nested loop - a loop within another loop
#  outer loop:
#        inner loop:


rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol: ")

for j in range(rows):
    for i in range(columns):
        print(symbol,end="")
    print()


