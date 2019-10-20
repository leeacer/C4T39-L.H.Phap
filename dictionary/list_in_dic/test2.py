job = {}
name = ['Huy', 'Tung', 'M.Duc']
role = ['waiter', 'cook', 'manager']
hours = [12, 24, 20]
pay = [0.8, 1.5, 2]

job["name"] = name
job["role"] = role
job["hours"] = hours
job["pay"] = pay

name.append("Don")
name.append("H.Duc")
role.append("waiter")
role.append("waiter")
hours.append(12)
hours.append(14)
pay.append(0.9)
pay.append(0.7)

print(pay[3] * hours[3])