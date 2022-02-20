import turtle
import time
from src import snake
from src import food
from src import scoreboard

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

onGame = True
while onGame:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.changePos()
        snake.growSnake()
        scoreboard.score+=1
        scoreboard.writeScore()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for snakeSegments in snake.snakebody[1:]:
        if snake.head.distance(snakeSegments) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
