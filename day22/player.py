from turtle import Turtle

STARTING_POSITION = (0, -230)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")

        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(0, self.ycor()+20)

    def starting_place(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() == 230
