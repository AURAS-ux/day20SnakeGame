import turtle

dir_up = 90
dir_down = 270
dir_left = 180
dir_right = 0

startPos = [[0, 0], [-20, 0], [-40, 0]]


class Snake:

    def __init__(self):
        self.snakebody = []
        self.createSnake()
        self.head = self.snakebody[0]

    def createSnake(self):
        for pos in startPos:
            self.addPart(pos)

    def addPart(self, pos):
        snakePart = turtle.Turtle(shape="square")
        snakePart.color("white")
        snakePart.penup()
        snakePart.goto(pos)
        self.snakebody.append(snakePart)

    def growSnake(self):
        self.addPart(self.snakebody[-1].position())

    def move(self):
        for parts in range(len(self.snakebody) - 1, 0, -1):
            new_x = self.snakebody[parts - 1].xcor()
            new_y = self.snakebody[parts - 1].ycor()
            self.snakebody[parts].goto(new_x, new_y)
        self.head.forward(20)
        # self.snakebody[0].seth(self.snakebody[0].heading() + 90)

    def up(self):
        if self.head.heading() != dir_down:
            self.head.setheading(dir_up)

    def down(self):
        if self.head.heading() != dir_up:
            self.head.setheading(dir_down)

    def left(self):
        if self.head.heading() != dir_right:
            self.head.setheading(dir_left)

    def right(self):
        if self.head.heading() != dir_left:
            self.head.setheading(dir_right)

    def reset(self):
        for seg in self.snakebody:
            seg.goto(1000,1000)
        self.snakebody.clear()
        self.createSnake()
        self.head = self.snakebody[0]
