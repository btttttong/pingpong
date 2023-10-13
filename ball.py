import random
from turtle import Turtle
from random import Random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('pink')
        self.shape('circle')
        self.yspeed = -10
        self.xspeed = 10

        # self.move()

    def move(self):
        self.goto(self.xcor() + self.xspeed, self.ycor() + self.yspeed)

    def bounce_wall(self):
        self.yspeed *= -1

    def hit_paddle(self):
        self.xspeed *= -1

    def set_center(self):
        self.goto(0, 0)


