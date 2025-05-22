
from turtle import Turtle

class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.forward(20)

   # if ball.distance(paddle) < 50 and ball.ycor() < -255 and ball.dy < 0 or ball.ycor() > 280:
        #     ball.bounce_y()

        # for block in blocks:
        #     if ball.distance(block) < 40:
        #         ball.bounce_y()
        #         block.disappear()
        #         blocks.remove(block)
        #         del block
        #         scoreboard.point()
        #         break

# # Recreate all blocks
# for block in blocks:
#     block.hideturtle()
#     block.clear()
# blocks.clear()
# for pos in block_positions:
#     new_block = Block(pos)
#     blocks.append(new_block)