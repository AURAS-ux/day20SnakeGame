from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.goto(0, 270)
        self.pendown()
        self.pencolor("White")
        self.writeScore()

    def writeScore(self):
        self.clear()
        self.write(arg=f"Score:{self.score} High Score:{self.highscore}", move=False, align="center", font=("Times New Roman", 20, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.writeScore()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.clear()
    #     self.write(arg=f"Game over", move=False, align="center", font=("Times New Roman", 20, "normal"))
