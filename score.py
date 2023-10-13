from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_L = 0
        self.score_R = 0
        self.color('green')



    def add_score_L(self):
        self.score_L += 1
        print(f'your score = {self.score_L}')
        return self.score_L

    def add_score_R(self):
        self.score_R += 1
        print(f'your score = {self.score_R}')
        return self.score_R

    def set_text(self):
        self.clear()
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto(0, 270)
        self.write('PingPong Game ^^', align='center', font=('Tahoma', 10, 'normal'))

    def print_score_L(self):
        self.goto(150, 250)
        self.write(f'Score: {self.score_L}', align='center', font=('Tahoma', 10, 'normal'))

    def print_score_R(self):
        self.goto(-150, 250)
        self.write(f'Score: {self.score_R}', align='center', font=('Tahoma', 10, 'normal'))


