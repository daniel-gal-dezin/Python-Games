import turtle
from turtle import Turtle, Screen

import pandas
import pandas as pd

screen = Screen()
screen.title("U.S. State Game")
path = "./blank_states_img.gif"
screen.setup(height=491, width=725)
screen.addshape(path)
image = Turtle()
image.shape(path)

df = pandas.read_csv("./50_states.csv")
gameison = True
numberofguesses = 0



def get_mouse_click_cor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_cor)
df['state'] = df['state'].str.lower()

while gameison:


    answer = screen.textinput(title=f"{numberofguesses}/50", prompt="insert name of country")

    if answer == "Exit":
        break

    turtle.hideturtle()
    answer = answer.lower()
    df2 = df[df['state'] == answer]



    if (len(df2) == 1):
        turtle.penup()
        turtle.goto(int(df2['x']), int(df2['y']))
        turtle.write(answer.title())
        numberofguesses += 1
        df = df.drop(df[df["state"]==answer].index)



    if(numberofguesses == 50):
        gameison = False

df.to_csv("states to study")