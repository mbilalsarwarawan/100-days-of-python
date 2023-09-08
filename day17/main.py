from turtle import *

turtle = Turtle()
screen = Screen()


def draw_shape(num_of_angles):
    angle = 360/num_of_angles
    for _ in range(num_of_angles):
        turtle.forward(100)
        turtle.right(angle)


for shape in range(3, 11):
    draw_shape(shape)


# for _ in range(4):
#     turtle.forward(100)
#     turtle.left(90)


# screen.exitonclick()
# for _ in range(4):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

screen.exitonclick()
