yob = int(input("What year were you born in: "))
age = 2019 - yob
print(age)

if age < 10:
    print("baby")
elif age < 18:
    print("teenager")
else:
    print("adult")