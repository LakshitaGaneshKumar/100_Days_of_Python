from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        """Takes in an x and y value and creates a paddle at that location."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)
        self.left(90)
        self.penup()
        self.goto(x, y)

    def up(self):
        """Moves the paddle up by 20 paces"""
        self.forward(40)

    def down(self):
        """Moves the paddle down by 20 paces"""
        self.backward(40)