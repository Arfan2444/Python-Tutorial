# list comprehension - a concise way to create lists in python
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

doubles = [x*2 for x in range(1,11)]
print(doubles)

gta4chracters = ["Niko Bellic","Michelle","Brucie Kubutz","Dimitri"]
gta4chracters = [gta4character.upper() for gta4character in gta4chracters]
print(gta4chracters)

numbers = [1,-2,3,-4,5,-6]
positivenumbers = [num for num in numbers if num >= 0]
negativenumbers = [num for num in numbers if num <= 0]

print(positivenumbers)
print(negativenumbers)