from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=0, y=260)
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}",align="center",font=("Arial",18,"bold"))
    
    def increase(self):
        self.score += 1
        self.update()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()
