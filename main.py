from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.listen()
screen.onkeypress(snake.turnup, "Up")
screen.onkeypress(snake.turndown, "Down")
screen.onkeypress(snake.turnright, "Right")
screen.onkeypress(snake.turnleft, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 20:
        snake.add_segment()
        scoreboard.increaseScore()
        food.relocate()

# Detect collision
    if snake.segments[0].xcor() > 400:
        game_is_on = False
    if snake.segments[0].ycor() > 400:
        game_is_on = False
    if snake.segments[0].xcor() < -400:
        game_is_on = False
    if snake.segments[0].ycor() < -400:
        game_is_on = False
    game_is_on = snake.detect_tail_collision()
scoreboard.gameOver()
screen.exitonclick()
