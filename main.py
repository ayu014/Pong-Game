from turtle import Screen
from paddle import Paddle
from ball import Ball  # Assuming this is correctly defined
from scoreboard import ScoreBoard
import time

# Setup the Screen
screen = Screen()
screen.bgcolor("black")
screen.title("The Pong Game")
screen.setup(height=600, width=800)
screen.tracer(0)  # Disable automatic updates

# Create Paddles
l_paddle = Paddle(-378, 0)
r_paddle = Paddle(370, 0)

ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move() 
    time.sleep(ball.move_speed)

    #Detect collison with Wall
    if  ball.collison():
        ball.bounce_y()

    #Detect collision with Paddle
    if ball.distance(r_paddle) <70 and ball.xcor() > 340 or ball.distance(l_paddle) <70 and ball.xcor() <-340 :
        ball.bounce_x()


    #Detect right paddle miss
    if ball.xcor() > 400:
        ball.reset()
        time.sleep(0.5)
        scoreboard.l_point()
    #detct left paddle miss
    if ball.xcor() <-400:
        ball.reset()
        scoreboard.r_point()
        time.sleep(0.5)


    


    


# Keep the window open until a click
screen.exitonclick()
