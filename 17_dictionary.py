# dictionary = a collection of {key:value} pairs
#              ordererd, changeable and non duplicate values

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

print(capitals)
print(capitals.get("India"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital dosen't exists")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Detroit"})

capitals.pop("China")
capitals.popitem()
print(capitals)

keys = capitals.keys()

for key in capitals.keys(): # get keys
    print(key)

# values = capitals.values()

for value in capitals.values(): # get values
    print(value)


# returns a 2dlist of tuples - [(),(),()]
items = capitals.items() # get key and values

for key,value in capitals.items():
    print(f"{key}:{value}")
