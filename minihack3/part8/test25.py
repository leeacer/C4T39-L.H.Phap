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

for k,v in SKills.items():
    print(k + ":", v)