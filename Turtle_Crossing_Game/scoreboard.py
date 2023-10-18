from turtle import Turtle

FONT = ("Courier", 36, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        """Create a scoreboard"""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.update_scoreboard()

    def increase_level(self):
        """Increase the level on the scoreboard"""
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard"""
        self.clear()
        self.write(arg=f"Level {self.level}", align="left", font=FONT)

    def gameover(self):
        """End the game"""
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)