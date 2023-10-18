from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        """Create a new player object"""
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.reset_position()

    def move(self):
        """Moves player turtle forward"""
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Resets the turtle to the bottom of the screen"""
        self.goto(STARTING_POSITION)