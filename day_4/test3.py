from random import randrange
weather = int(randrange(1 ,101))
print(weather)

if weather < 30:
    print("It's gonna be rainy")
elif weather >= 30 and weather < 60:
    print("It's gonna be cloudy")
elif weather >= 60:
    print("It's gonna be sunny")