from turtle import Turtle
import random as r

class Ball(Turtle):

    def __init__(self):
        """Creates a ball"""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 20
        self.y_move = 20
        self.move_speed = 0.1

    def move(self):
        """Randomly moves the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounces the ball off of the top and bottom of the screen"""
        self.y_move *= -1

    def bounce_x(self):
        """Bounces the ball off of the left and right sides of the screen"""
        self.x_move *= -1
        self.move_speed *= 1.9
    
    def reset_position(self):
        """Resets the ball's position to (0,0)"""
        self.goto(0, 0)
        self.move_speed = 0.1