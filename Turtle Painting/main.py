from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

def random_color():
    """Sets the turtle to a random color"""
    colors = ["royal blue", "slate blue", "medium aquamarine", "cornflower blue", "sea green", "light steel blue"]
    tim.color(random.choice(colors))


def fd(x):
    """Takes in a value x and moves the turtle forward by x paces"""
    tim.forward(x)


def right(x):
    """Takes in a value x and turns the turtle right by x degrees"""
    tim.right(x)


def left(x):
    """Takes in a value x and turns the turtle left by x degrees"""
    tim.left(x)


def pendown(x):
    """Takes in a value True/False. If True, puts the turtle's pen down, else puts the pen up"""
    if x:
        tim.pendown()
    else:
        tim.penup()


def draw_shape(num_sides, side_length):
    """Takes in values num_sides and side_length to draw a shape with the given num_sides and side_length"""
    pendown(True)
    for i in range(num_sides):
        fd(side_length)
        right(360 / num_sides)


def draw_spirograph(size_of_gap):
    """Takes in a value for the size_of_gap in the spirograph and paints a spirograph based on that value"""
    pendown(False)
    tim.setpos(0, 0)
    pendown(True)
    tim.pensize(1)
    for i in range(int(360 / size_of_gap)):
        random_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


# Initialize turtle's starting position, color, and speed
random_color()
tim.speed("fastest")
pendown(False)
tim.setpos(-300, 300)

# Challenge 1: Draw a square
draw_shape(4, 100)

# Challenge 2: Draw a dashed line
for i in range(15):
    pendown(True)
    fd(10)
    pendown(False)
    fd(10)

# Challenge 3: Draw 8 shapes
for i in range(3, 11):
    random_color()
    draw_shape(i, 100)

# Challenge 4: Generate a Random Walk
directions = [0, 90, 180, 270]
tim.pensize(10)
for i in range(200):
    random_color()
    fd(random.randint(1, 50))
    right(random.choice(directions))

# Challenge 5: Draw a Spirograph
draw_spirograph(5)

screen = Screen()
screen.exitonclick()
