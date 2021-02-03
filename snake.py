from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.creat()
        self.current_way = 'right'

    def creat(self):
        starting_segment = Turtle()
        starting_segment.shape('square')
        starting_segment.penup()
        starting_segment.color('white')
        starting_segment.goto((0, 0))
        self.segments.append(starting_segment)

    def move(self):
        if len(self.segments) > 1:
            for seg_n in range(len(self.segments) - 1, 0, -1):
                x_pos = self.segments[seg_n - 1].xcor()
                y_pos = self.segments[seg_n - 1].ycor()
                self.segments[seg_n].goto(x_pos, y_pos)
        self.segments[0].forward(20)

    def turnup(self):
        if self.current_way == "right":
            self.current_way = "up"
            self.segments[0].left(90)
        elif self.current_way == "left":
            self.current_way = "up"
            self.segments[0].right(90)

    def turndown(self):
        if self.current_way == "right":
            self.current_way = "down"
            self.segments[0].right(90)
        elif self.current_way == "left":
            self.current_way = "down"
            self.segments[0].left(90)

    def turnright(self):
        if self.current_way == "up":
            self.current_way = "right"
            self.segments[0].right(90)
        elif self.current_way == "down":
            self.current_way = "right"
            self.segments[0].left(90)

    def turnleft(self):
        if self.current_way == "up":
            self.current_way = "left"
            self.segments[0].left(90)
        elif self.current_way == "down":
            self.current_way = "left"
            self.segments[0].right(90)

    def add_segment(self):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()

        if self.current_way == 'right':
            pos_x = self.segments[-1].xcor() - 20
            pos_y = self.segments[-1].ycor()
        elif self.current_way == 'left':
            pos_x = self.segments[-1].xcor() + 20
            pos_y = self.segments[-1].ycor()
        elif self.current_way == 'up':
            pos_x = self.segments[-1].xcor()
            pos_y = self.segments[-1].ycor() - 20
        elif self.current_way == 'down':
            pos_x = self.segments[-1].xcor()
            pos_y = self.segments[-1].ycor() + 20
        new_segment.goto(pos_x, pos_y)
        self.segments.append(new_segment)

    def detect_tail_collision(self):
        positions = [position.pos() for position in self.segments]
        if positions[0] in positions[1:]:
            return False
        else:
            return True

    def detect_wall_collision(self):
        if self.segments[0].xcor() > 390:
            return False
        elif self.segments[0].ycor() > 390:
            return False
        elif self.segments[0].xcor() < -390:
            return False
        elif self.segments[0].ycor() < -390:
            return False
        else:
            return True