import random
from turtle import Turtle

class Block(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(random.choice(["red", "green", "blue", "yellow", "orange", "purple", "cyan"]))
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)

    def disappear(self):
        self.hideturtle()
        self.goto(1000, 1000)


