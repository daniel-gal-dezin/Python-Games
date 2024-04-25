
from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score_bord import ScoreBoard
from end_game import End


screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

score = ScoreBoard()
snake = Snake()
food = Food()


screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if food.distance(snake.segments[0]) < 15:
        snake.add_body()
        score.scoreplus()
        food.change_position()
        screen.update()

    xcor = snake.head.xcor()
    ycor = snake.head.ycor()

    if xcor > 280 or xcor < -280 or ycor > 280 or ycor < -280:
        score.reset()
        snake.reset()


    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()















screen.exitonclick()