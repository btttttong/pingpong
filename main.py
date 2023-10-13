import time
from score import Score
from ball import Ball
from paddle import Paddle
from turtle import Screen
from turtle import Turtle

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
game_on = True
score = Score()
ball = Ball()
paddle_L = Paddle(300)
paddle_R = Paddle(-300)
screen_speed = 0.05
screen.listen()
screen.onkeypress(fun=paddle_L.go_up, key="Up")
screen.onkeypress(fun=paddle_L.go_down, key="Down")
screen.onkeypress(fun=paddle_R.go_up, key="w")
screen.onkeypress(fun=paddle_R.go_down, key="s")


while game_on:
    score.set_text()
    score.print_score_L()
    score.print_score_R()
    time.sleep(screen_speed)
    ball.move()
    screen.update()
    print(f'{ball.pos()}')

    # if ball.ycor() < -290:
    #     ball.yspeed *= -1
    # elif ball.ycor() > 290:
    #     ball.yspeed *= -1

    if ball.ycor() < -290 or ball.ycor() > 290:
        ball.bounce_wall()

    if ball.xcor() >= 290 and paddle_L.ycor()-50 <= ball.ycor() <= paddle_L.ycor()+50:
        ball.hit_paddle()
        score.add_score_L()  # update score
        if screen_speed > 0:
            screen_speed -= 0.001

    elif ball.xcor() <= -290 and paddle_R.ycor()-50 <= ball.ycor() <= paddle_R.ycor()+50:
        ball.hit_paddle()
        score.add_score_R()  # update score
        if screen_speed > 0:
            screen_speed -= 0.001
    #
    if ball.xcor() < -400: #left loose ball
        ball.set_center() #place ball in center

    if ball.xcor() > 400: #left loose ball
        ball.set_center() #place ball in center



screen.mainloop()