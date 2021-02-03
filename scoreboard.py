from turtle import Turtle
import config

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0, 370)
        self.hideturtle()
        self.updateScore()

    def updateScore(self):
        self.write(f"Score: {self.score}", align="center", font=config.FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScore()

    def gameOver(self):
        self.goto(0,0)
        self.write(f"Gameover", align="center", font=FONT)