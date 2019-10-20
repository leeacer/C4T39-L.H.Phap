job = {}
name = ['Huy', 'Tung', 'M.Duc']
role = ['waiter', 'cook', 'manager']
hours = ['12', '24', '20']
pay = ['0.8', '1.5', '2']

job["name"] = name
job["role"] = role
job["hours"] = hours
job["pay"] = pay

for a in job:
    print(a + ": " + ', '.join(job[a]))