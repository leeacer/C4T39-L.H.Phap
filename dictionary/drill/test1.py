dick = {
    "name" : "lucio",
    "animal" : "frog",
    "color" : "green",
}
def checkKey(dick, key): 
	if key in dick: 
		print("Name exists in the dicc")
	else: 
		print("W doesn't exists in the dicc") 
key = 'name'
checkKey(dick, key) 
key = 'w'
checkKey(dick, key) 
