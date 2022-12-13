from turtle import Turtle, Screen
from player import Player
from driving_cars import Driving_Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.screensize(300,300)
screen.tracer(0)

player = Player()
cars = Driving_Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_on = True

while game_on:
    
    time.sleep(0.1)
    cars.Create_Car()
    cars.move_cars()

    if player.ycor() > 290:
        player.go_to_start()
        cars.level_up()
        scoreboard.level_up()
        scoreboard.update_scoreboard()

    for car in cars.cars_array:
        if player.distance(car) < 30:
            game_on = False
            scoreboard.game_over()

    screen.update()

screen.exitonclick()