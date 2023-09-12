from turtle import Turtle, Screen
import random
screen = Screen()

user_bet = screen.textinput(title="Enter your color", prompt="A color to bet")
screen.setup(500, 400)
colors = ["red", "brown", "blue", "black", "purple"]
Y_position = [-70, -40, -10, 20, 50]
all_turtle = []
for turtle_index in range(5):
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=Y_position[turtle_index])
    all_turtle.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning = turtle.pencolor()
            is_race_on = False
            if winning == user_bet:
                print(f"You win")
            else:
                print("you lose")

screen.exitonclick()
