from turtle import Turtle

starting_position = (0, -290)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.left(90)
        self.penup()
        self.go_to_start()

    def move(self):
        self.forward(10)
    
    def go_to_start(self):
        self.goto(starting_position)