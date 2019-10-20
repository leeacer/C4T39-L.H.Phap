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

restaurant.append(p1)
restaurant.append(p2)
restaurant.append(p3)
restaurant.append(p4)

budget = p1["hours"] * 730 * p1["pay"] + p2["hours"] * 730 * p2["pay"] + p3["hours"] * 730 * p3["pay"] + p4["hours"] * 730 * p4["pay"]

print("$", budget)