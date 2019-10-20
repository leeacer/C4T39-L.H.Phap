character = {
    "Age" : 17,
    "Strength" : 8,
    "Defence" : 10,
    "HP" : 100,
    "Backpack" : ["Shield", "Bread loaf"],
    "Gold" : 100,
    "Level" : 2,
}

character["Gold"] = character["Gold"] + 50
character["Backpack"].append("Flintstone")

for k,v in character.items():
    print(k + ":", v)