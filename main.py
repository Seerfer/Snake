from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import config



snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=config.SCREEN_WIDTH, height=config.SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.listen()
screen.onkeypress(snake.turnup, "Up")
screen.onkeypress(snake.turndown, "Down")
screen.onkeypress(snake.turnright, "Right")
screen.onkeypress(snake.turnleft, "Left")

speed = config.START_SPEED
counter = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    if snake.segments[0].distance(food) < 20:
        snake.add_segment()
        scoreboard.increaseScore()
        food.relocate()
        counter += 1
    game_is_on = snake.detect_wall_collision() and snake.detect_tail_collision()
    if counter == config.COUNTER_BORDER:
        speed -= speed * config.SPEED_INCREMENT
        counter = 0
scoreboard.gameOver()
screen.exitonclick()
