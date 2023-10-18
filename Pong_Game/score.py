from turtle import Turtle

FONT = ("Courier", 80, "normal")
ALIGNMENT = "center"

class Score(Turtle):

    def __init__(self):
        """Creates a scoreboard"""
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_screen()

    def update_screen(self):
        """Updates the scoreboard"""
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(arg=self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """Increases the left side score by 1"""
        self.l_score += 1
        self.update_screen()
    
    def r_point(self):
        """Increases the right side score by 1"""
        self.r_score += 1
        self.update_screen()