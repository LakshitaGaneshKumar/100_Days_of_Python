from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

def play_game():
    # Create game screen
    screen = Screen()
    screen.clearscreen()
    screen.setup(width=800, height=600)
    screen.title("Pong Game")
    screen.bgcolor("black")

    # Create paddles, ball, and scoreboard
    r_paddle = Paddle(x=350, y=0)
    l_paddle = Paddle(x=-350, y=0)
    scoreboard = Score()
    ball = Ball()

    # Listen for key strokes
    screen.listen()
    screen.onkey(key="Up", fun=r_paddle.up)
    screen.onkey(key="Down", fun=r_paddle.down)
    screen.onkey(key="w", fun=l_paddle.up)
    screen.onkey(key="s", fun=l_paddle.down)
    screen.onkey(key="r", fun=play_game)

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        ball.move()

        # Detect collision with top and bottom walls
        if ball.ycor() < -290 or ball.ycor() > 290:
            ball.bounce_y()

        # Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # Detect R paddle miss
        if ball.xcor() > 340:
            ball.reset_position()
            scoreboard.l_point()

        # Detect L paddle miss
        elif ball.xcor() < -340:
            ball.reset_position()
            scoreboard.r_point()

    screen.exitonclick()

play_game()
