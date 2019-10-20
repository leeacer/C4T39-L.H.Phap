n = int(input("Enter the number of sides: "))
exterior = 360 / n
from turtle import *
shape("turtle")
speed(0)
forward(100)
for i in range(n-1):
    left(exterior)
    forward(100)

mainloop()