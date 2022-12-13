from turtle import Turtle
import random

colors = ["red", "blue", "yellow", "pink"]
moving_speed = 10

class Driving_Cars(Turtle):
    
    def __init__(self):
        self.cars_array = []
        self.level = 1

    def Create_Car(self):
        if random.randint(1,6) == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(colors))
            starting_x = 400
            random_y = random.randint(-250, 250)
            car.goto(starting_x, random_y)
            self.cars_array.append(car)

    def move_cars(self):
        for car in self.cars_array:
            car.backward(moving_speed)

    def level_up(self):
        self.level += 1
        global moving_speed
        moving_speed += 10