from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt") as file:
            self.hsc = int(file.read())
        self.hideturtle()
        self.goto(0, 270)
        self.pendown()
        self.pencolor("White")
        self.writeScore()

    def writeScore(self):
        self.clear()
        self.write(arg=f"Score:{self.score} High Score:{self.hsc}", move=False, align="center",
                   font=("Times New Roman", 20, "normal"))

    def reset(self):
        if self.score > self.hsc:
            self.hsc = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.hsc}")
        self.score = 0
        self.writeScore()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.clear()
    #     self.write(arg=f"Game over", move=False, align="center", font=("Times New Roman", 20, "normal"))
