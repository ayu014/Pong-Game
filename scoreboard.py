from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update()
        

    def update(self):
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Courier",80,"normal"))
        
    def l_point(self):
        self.l_score +=1
        self.clear()
        self.update()
    def r_point(self):
        self.r_score +=1
        self.clear()
        self.update()
    

