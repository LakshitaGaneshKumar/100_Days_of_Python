from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars
import time

# Set up game screen
screen = Screen()
screen.bgcolor("white smoke")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player, scoreboard, and car objects
player = Player()
scoreboard = Scoreboard()
cars = Cars()

# Listen for Up key
screen.listen()
screen.onkey(key="Up", fun=player.move)

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    # Generate and move new cars every 0.1 seconds
    cars.generate_car()
    cars.move_cars()
    
    # Detect collision with top wall and increase level
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.reset_position()
        cars.level_up()

    # Detect collision with car and end game
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.gameover()

screen.exitonclick()
