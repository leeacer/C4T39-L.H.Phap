skill1 = {
    "Name" : "Tackle",
    "Minimum level" : 1,
    "Damage" : 5,
    "Hit rate" : 0.3,
}

skill2 = {
    "Name" : "Quick attack",
    "Minimum level" : 2,
    "Damage" : 3,
    "Hit rate" : 0.5,
}

skill3 = {
    "Name" : "Strong kick",
    "Minimum level" : 4,
    "Damage" : 9,
    "Hit rate" : 0.2,
}

SKills = {

}

SKills["skill 1"] = skill1["Name"]
SKills["skill 2"] = skill2["Name"]
SKills["skill 3"] = skill3["Name"]

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
character["Pocket"] = ["MonsterDex", "Flashlight"]

print("----------------------------------------------------------------------------------------")
print("                            !!MONSTER APPEARS!!                                         ")
print("----------------------------------------------------------------------------------------")

for k,v in SKills.items():
    print(k + ":", v)

print("!!CHOOSE AN ATTACK!!")
attack = input(": ")

if attack.capitalize() == SKills["skill 1"]:
    if skill1["Minimum level"] <= character["Level"]:
        print(skill1["Damage"], "damage has been done")
    else:
        print("Your not high enough level")
elif attack.capitalize() == SKills["skill 2"]:
    if skill2["Minimum level"] <= character["Level"]:
        print(skill2["Damage"], "damage has been done")
    else:
        print("Your not high enough level")
elif attack.capitalize() == SKills["skill 3"]:
    if skill3["Minimum level"] <= character["Level"]:
        print(skill3["Damage"], "damage has been done")
    else:
        print("Your not high enough level")
else:
    print("That's not an attack")
