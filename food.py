from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        x_pos = random.randint(-300, 300)
        y_pos = random.randint(-300, 300)
        self.goto(x_pos, y_pos)

    def relocate(self):
        pos_x_rell = random.randint(-280, 280)
        pos_y_rell = random.randint(-280, 280)
        self.goto(pos_x_rell, pos_y_rell)
