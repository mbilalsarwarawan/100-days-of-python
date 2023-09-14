from turtle import Screen
import time
import snake
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
my_snake = snake.Snake()
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.setup(width=500, height=500)
screen.tracer(0)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    my_snake.move()

screen.exitonclick()
