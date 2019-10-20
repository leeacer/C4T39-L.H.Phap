restaurant = []

p1 = {
    "name" : "huy", 
    "role" : "waiter", 
    "hours" : 12, 
    "pay" : 0.8
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

print("-------------------------------------")

p1["name"] = "huyen"
p1["role"] = "waitress"
p1["hours"] = 14
p1["pay"] = 1

for i in restaurant:
    print(i)