from turtle import Screen
import time
import snake
import food
import scoreboard
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
food = food.Food()
my_snake = snake.Snake()
scoreboard = scoreboard.Scoreboard()
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")

screen.tracer(0)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    my_snake.move()

    if my_snake.head.xcor() > 250 or my_snake.head.xcor() < -250 or my_snake.head.ycor() > 250 or my_snake.head.ycor() < -250:
        game_is_on = False
        scoreboard.game_over()

    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.grow()
        scoreboard.score_update()
    for segment in my_snake.segment:
        if my_snake.head.distance(segment) < 10:
            if my_snake.head == segment:
                pass
            else:
                game_is_on = False
                scoreboard.game_over()


screen.exitonclick()
