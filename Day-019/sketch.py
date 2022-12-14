from turtle import Turtle, Screen

dan = Turtle()
screen = Screen()


def move_forward():
    dan.forward(10)


def move_backwards():
    dan.backward(10)


def turn_left():
    new_heading = dan.heading() + 10
    dan.setheading(new_heading)


def turn_right():
    new_heading = dan.heading() - 10
    dan.setheading(new_heading)


def clear():
    dan.clear()
    dan.penup()
    dan.home()
    dan.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
