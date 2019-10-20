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

for k,v in skill1.items():
    print(k + ":", v)

for k,v in skill2.items():
    print(k + ":", v)

for k,v in skill3.items():
    print(k + ":", v)