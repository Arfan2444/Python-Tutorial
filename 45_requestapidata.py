# How to connect to an API using Python

import requests

baseurl = "https://pokeapi.co/api/v2/"

def getpokemoninfo(name):
    url = f"{baseurl}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to Retrieve data: {response.status_code}")


pokemon_name = "arceus"
pokemon_info=getpokemoninfo(pokemon_name)

if pokemon_info:
    print(f"pokemon name:{pokemon_info["name"].captialize()}")
    print(f"pokemon id:{pokemon_info["id"]}")
    print(f"pokemon height:{pokemon_info["height"]}")
    print(f"pokemon weight:{pokemon_info["weight"]}")
    # print(f"pokemon name:{pokemon_info["moves"]}")