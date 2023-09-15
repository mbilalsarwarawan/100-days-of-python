from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.goto(0, 200)
        self.write(f"Score = {self.score} ", False, align="center",
                   font=('Arial', 10, 'normal'))

    def score_update(self):
        self.score += 1
        self.clear()

        self.write(f"Score = {self.score} ", False, align="center",
                   font=('Arial', 10, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game is Over", False, align="center",
                   font=('Arial', 10, 'normal'))
