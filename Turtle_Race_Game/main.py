from turtle import Turtle, Screen
import random

race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

def create_turtle(x):
    """Takes in a value x and creates x many turtle objects"""
    for i in range(x):
        turt = Turtle(shape="turtle")
        turt.penup()
        turt.color(colors[i])
        turt.goto(x=-230, y=((i * 30) - 90))
        turtles.append(turt)

create_turtle(6)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
