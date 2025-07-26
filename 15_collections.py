# collection - single "variable" that can store multiple values
# List - [] ordered ,mutable, allows duplicates
# Set - {} unordered, immutable, but can be modified, no duplicates
# Tuple - () ordered and unchangeable, allows duplicates


# 1. List
Pcgames = ["Dota 2", "CS:GO", "PUBG", "Valorant"]
# print("Valorant" in Pcgames)  # Check if "Valorant" is in the list
# print("Valorant" not in Pcgames)  # Check if "Valorant" is not in the list

# Modifying the element in the list
Pcgames[0] = "Apex Legends"  # Change the first element

Pcgames.append("Doom Eternal") # Add a new game to the end of the list
Pcgames.remove("PUBG")  # Remove "PUBG" from the list

Pcgames.insert(3, "Fortnite")  # Insert "Fortnite" at index 3
Pcgames.sort()  # Sort the list in alphabetical order

Pcgames.reverse()  # Reverse the order of the list
# print(Pcgames.pop())  # Remove the last element from the list
# Pcgames.clear()  # Clear the list

print(Pcgames)

# for game in Pcgames:
#     print(game,end=" ")


# 2. Set
Gta4characters = {"Niko Bellic","Michelle","Roman Bellic","Dimitri Rascalov"}

# print(Gta4characters[0])  # This will raise an error because sets are unordered and do not support indexing
Gta4characters.add("Brucie Kibbutz") # Add a new character to the set
Gta4characters.remove("Michelle")  # Remove "Michelle" from the set
Gta4characters.discard("Roman Bellic")  # Remove "Roman Bellic" from the set, does not raise an error if not found

print(Gta4characters)


# 3. Tuple

Gta5characters = ("Franklin Clinton", "Trevor Philips", "Michael De Santa", "Lamar Davis")
print(Gta5characters)
print(Gta5characters[0])  # Accessing the first element of the tuple
# Gta5characters[0] = "Franklin"  # This will raise an error because tuples are immutable

print(Gta5characters.index("Lamar Davis"))  # Find the index of "Lamar Davis" in the tuple
print(Gta5characters.count("Michael De Santa"))  # Count how many times "Michael De Santa" appears in the tuples