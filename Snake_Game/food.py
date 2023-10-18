from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        """Initializes a new food object"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        """Places the food object at a random location on the screen"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)