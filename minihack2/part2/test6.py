from turtle import *
import random

lists = ["magenta", "blue", "red", "purple"]
elsa = Turtle()

for i in range(len(lists)):
    elsa.color(lists[i])
    elsa.left(90)
    elsa.forward(100)

mainloop()