from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake():

    def __init__(self):
        self.turks = []
        self.create_snake()
        self.head = self.turks[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turk = Turtle(shape="square")
        turk.penup()
        turk.color("white")
        turk.goto(position)
        self.turks.append(turk)

    def extent(self):
        self.add_segment(self.turks[-1].position())

    def reset_snake(self):
        for turk in self.turks:
            turk.goto(1000, 1000)
        self.turks.clear()
        self.create_snake()
        self.head = self.turks[0]

    def move(self):
        for turk_num in range(len(self.turks) - 1, 0, -1):
            x_cord = self.turks[turk_num - 1].xcor()
            y_cord = self.turks[turk_num - 1].ycor()
            self.turks[turk_num].goto(x_cord, y_cord)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
