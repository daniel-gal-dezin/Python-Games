from turtle import Screen
from paddle import Paddle
from ball import Ball
from gamebord import GameBoard
import time


screen = Screen()
screen.tracer(0)

screen.bgcolor("black")
screen.title("Pong-Game")
screen.setup(width=800 , height=600)


screen.listen()
rightpaddle = Paddle(350,0)
leftpaddle = Paddle(-350,0)
screen.onkeypress(rightpaddle.up, "Up")
screen.onkeypress(rightpaddle.down, "Down")
screen.onkeypress(leftpaddle.up, "w")
screen.onkeypress(leftpaddle.down, "s")
ball = Ball()
score = GameBoard()





game_is_on = True

while game_is_on:

    time.sleep(0.1)
    ball.move()

    #detect collision with up wall
    if ball.ycor() >= 280:
        ball.ybounceup()

    #detec collision with right paddle
    if ball.distance(rightpaddle) < 50 and ball.xcor() > 320:
        ball.xbouncerigh()

    #detect colliision with left paddle
    if ball.distance(leftpaddle) < 50  and ball.xcor() <-320:
        ball.xbounceleft()

    #detect collision with floor
    if ball.ycor() <= -280:
        ball.ybouncedown()


    if ball.xcor() > 400:
        ball.setx(0)
        ball.sety(0)
        score.left_score()
        ball.xmove *= -1

    if ball.xcor() < -400:
        ball.setx(0)
        ball.sety(0)
        score.right_score()
        ball.xmove *= -1




    screen.update()





























screen.exitonclick()