from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
LEFT = 180
UP = 90
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segment.append(new_segment)

    def move(self):

        for seg_num in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg_num-1].xcor()
            new_y = self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def grow(self):
        new_x = self.head.xcor()
        new_y = self.head.ycor()
        if self.head.heading() == UP or self.head.heading() == DOWN:
            new_y -= 20
        else:
            new_x -= 20

        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(new_x, new_y)
        self.segment.append(new_segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
