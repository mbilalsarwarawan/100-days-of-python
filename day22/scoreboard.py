from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(-290, 210)
        self.write(f"Level = {self.score}", font=FONT)

    def updateScore(self):
        self.score += 1
        self.clear()
        self.goto(-290, 210)
        self.write(f"Level = {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font=FONT)
