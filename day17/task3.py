from turtle import *
import random
tim = Turtle()
screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
for _ in range(int(360/5)):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading()+5)

screen.exitonclick()
