from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


def move_back():
    tim.back(10)


screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Down", fun=move_back)
screen.exitonclick()
