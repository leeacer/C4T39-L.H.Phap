restaurant = []

p1 = {
    "name" : "huyen", 
    "role" : "waitress", 
    "hours" : 14, 
    "pay" : 1
    }
p2 = {
    "name" : "tung",
    "role" : "cook", 
    "hours" : 24, 
    "pay" : 1.5}
p3 = {
    "name" : "m.duc", 
    "role" : "manager", 
    "hours" : 20, 
    "pay" : 2
    }     
p4 = {
    "name" : "don", 
    "role" : "waiter", 
    "hours" : 12, 
    "pay" : 0.9
    } 
p5 = {
    "name" : "h.duc", 
    "role" : "waiter", 
    "hours" : 14, 
    "pay" : 0.7
    }            

restaurant.append(p1)
restaurant.append(p2)
restaurant.append(p3)
restaurant.append(p4)
restaurant.append(p5)

for i in restaurant:
    print(i)

print("----------------------------------------------------------")

restaurant.pop(4)

for i in restaurant:
    print(i)