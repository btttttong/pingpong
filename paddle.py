from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, def_pos):
        super().__init__()
        self.penup()
        self.shape('square')
        self.stretch_w = 5
        self.stretch_h = 1
        self.shape_size(self.stretch_w, self.stretch_h)
        self.default_position(def_pos)

    def shape_size(self, stretch_w, stretch_h):
        self.shapesize(stretch_w,stretch_h)
        # self.paddle.shapesize(stretch_w,stretch_h)

    def default_position(self, pos):
        self.goto(pos, 0)
        # self.paddle.goto(pos, 0)

    def go_up(self):
        if self.ycor() <= 240:
            y = self.ycor()
            y += 20
            self.sety(y)

    def go_down(self):
        if self.ycor() >= -220:
            y = self.ycor()
            y -= 20
            self.sety(y)
