from turtle import Turtle
import random

COLORS = ["lavender", "light sky blue", "steel blue", "medium turquoise", "cadet blue", "aquamarine", "DeepSkyBlue4", "RoyalBlue1"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Cars():

    def __init__(self):
        """Create a list of all cars"""
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        """Generate a new car"""
        random_num = random.randint(0, 6)
        if random_num == 1:
            car = Turtle("square")
            car.shapesize(stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            new_y = random.randint(-240, 250)
            car.goto(300, new_y)
            self.all_cars.append(car)
    
    def move_cars(self):
        """Move all cars"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increase the speed of cars"""
        self.car_speed += MOVE_INCREMENT