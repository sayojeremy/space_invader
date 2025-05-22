from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.score, align="center", font=("courier", 50, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        self.clear()
        self.score = 0



