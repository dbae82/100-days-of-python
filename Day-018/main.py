from turtle import Turtle, colormode, Screen
from random import choice

colormode(255)
dan = Turtle()
dan.speed(0)
dan.penup()
dan.hideturtle()
color_list = [
    (176, 48, 79), (42, 98, 146), (205, 161, 94),
    (223, 210, 102), (137, 90, 64), (177, 164, 38),
    (109, 176, 207), (212, 131, 173), (227, 73, 49),
    (201, 75, 117), (88, 105, 192)
]
dan.setheading(225)
dan.forward(300)
dan.setheading(0)
number_of_dots = 100

for dot in range(1, number_of_dots + 1):
    dan.dot(20, choice(color_list))
    dan.forward(50)

    if dot % 10 == 0:
        dan.setheading(90)
        dan.forward(50)
        dan.setheading(180)
        dan.forward(500)
        dan.setheading(0)

screen = Screen()
screen.exitonclick()
