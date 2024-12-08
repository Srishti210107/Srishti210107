from turtle import Turtle,Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen=Screen()
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")


    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def is_finish(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
            