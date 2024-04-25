from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("scores.txt") as score:
            self.highscore = int(score.read())
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=('Arial', 20, 'normal'))
        self.hideturtle()

    def scoreplus(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("scores.txt", mode="w") as s:
                s.write(f"{self.highscore}")

        self.score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=('Arial', 20, 'normal'))
