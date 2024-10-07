from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        

    def create_ball(self):
        self.color("white")
        self.shape("circle")
        self.speed("normal")
        self.penup()
    



    
    def move(self):
        new_x = self.xcor() +self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def collison(self):
        if self.ycor() > 280 or self.ycor() < -280:
            return True
    
    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *=0.9
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *=0.9
    

    
    def reset(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1
    
  




        
