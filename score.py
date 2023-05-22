from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=0, y=260)
        self.update()
    
    def update(self):
        self.write(f"Score : {self.score} ",align="center",font=("Arial",18,"bold"))
    
    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Arial",18,"bold"))