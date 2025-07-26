# format specifier = {value:flags} format a value based on what flags are inserted

price1 = 3.14159
price2 = 9.452
price3 = 7.923

print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:>10}")