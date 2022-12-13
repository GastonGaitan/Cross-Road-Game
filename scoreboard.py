from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-300, 300)
        self.update_scoreboard()

    def level_up(self):
        self.level += 1
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="Center", font="Arial")
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="Center", font="Arial")
        