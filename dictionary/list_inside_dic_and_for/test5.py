supersentai = {
    "name" : "lupinranger vs patranger",
    "release" : 2018,
    "characters" : ["lupin red", "lupin blue", "lupin yellow", "lupin/patren X", "patren 1gou", "patren 2gou", "patren 3gou"],
}

for k,v in supersentai.items():
    print(k + ":", v)
print("--------------------------------------------------------")

supersentai["characters"].append("kogure")

for k,v in supersentai.items():
    print(k + ":", v)