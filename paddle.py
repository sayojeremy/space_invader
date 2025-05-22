from turtle import Turtle
import math
import random

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("arrow")
        self.color("white")
        self.shapesize(stretch_wid=1 , stretch_len= 3)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def shoot(self):
        return self.xcor() , self.ycor() + 10

class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def move(self):
        self.forward(20)
