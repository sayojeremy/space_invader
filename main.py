from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from blocks import Block
from scoreboard import Scoreboard
import time

block_positions = [
    # J
    (-350, 200),  (-300, 200) ,(-250, 200),
    (-250, 150),
    (-350, 100), (-250, 100),

    # O
    (-150, 200), (-50, 200),
    (-150, 150), (-50, 150),
    (-150, 100), (-50, 100),

    # H
    (50, 200), (150, 200),
    (50, 150), (150, 150),
    (50, 100), (150, 100),

    # N
    (250, 200), (350, 200),
    (250, 150), (300, 175), (350, 150),
    (250, 100), (350, 100)
]
from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("arrow")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=3)
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
        return self.xcor(), self.ycor() + 10

class Alien(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=1)
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
        return self.xcor(), self.ycor() + 10

    def disapper(self):
        self.goto( 1000, 1000)


class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.setheading(90)  # Point upward

    def move(self):
        self.forward(20)


# Setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Minimal Shooter")
screen.tracer(0)

# Create paddle
paddle = Paddle((0, -280))
alien= Alien((0,220))

# paddle Shooting logic
def fire_bullet():
    x, y = paddle.shoot()
    bullet = Ball(x, y)
    bullets.append(bullet)

# Store bullets
bullets = []
# alien movement & shooting logic
alien_direction = "right"  # Initial movement direction

def alien_move():
    global alien_direction

    if alien_direction == "right":
        alien.right()
        if alien.xcor() > 280:
            alien_direction = "left"  # Change direction at right edge

    elif alien_direction == "left":
        alien.left()
        if alien.xcor() < -280:
            alien_direction = "right"  # Change direction at left edge
# Keyboard bindings
screen.listen()
screen.onkey(paddle.right, "Right")
screen.onkey(paddle.left, "Left")
screen.onkey(fire_bullet, "Up")

# Game loop
def game_loop():
    for bullet in bullets:
        bullet.move()
    alien_move()
    for bullet in bullets:
        if alien.distance(bullet) < 50 :
            alien.disapper()
    screen.update()
    screen.ontimer(game_loop, 50)

game_loop()
screen.mainloop()

