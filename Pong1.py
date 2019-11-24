import turtle
import os

# create a screen
wn = turtle.Screen()
wn.title("Pong by Ahmad Zayan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
    # tracer stops the window from updating manually which helps us speed up the game 
wn.tracer(0)







# Score
score_a = 0
score_b = 0








# Paddle A
paddle_a = turtle.Turtle()
    # Speed of animation: sets the speed to maxumum possible speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
    # Makes the paddle 5 times more wide and 1 time more tall
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    # Turtles draw a line as they're moving but we do not want that so we do penup
paddle_a.penup()
    # The paddles starting point on the screen is -350, 0. Think of the screen as a coordinate plane
paddle_a.goto(-350, 0)








# Paddle B
paddle_b = turtle.Turtle()
    # Speed of animation: sets the speed to maxumum possible speed
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
    # Makes the paddle 5 times more wide and 1 time more tall
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    # Turtles draw a line as they're moving but we do not want that so we do penup
paddle_b.penup()
    # The paddles starting point on the screen is -350, 0. Think of the screen as a coordinate plane
paddle_b.goto(350, 0)

















# Ball
ball = turtle.Turtle()
    # Speed of animation: sets the speed to maxumum possible speed
ball.speed(0)
ball.shape("square")
ball.color("white")
    # Turtles draw a line as they're moving but we do not want that so we do penup
ball.penup()
    # The paddles starting point on the screen is -350, 0. Think of the screen as a coordinate plane
ball.goto(0, 0)
#   Every time the ball moves, it moves by 2 px
ball.dx = 2
ball.dy = -2








# Pen (Just a turtle)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))




















# Functions
def paddle_a_up():
    #built in function that returns the y coordinate
    y = paddle_a.ycor()
    #adds 20px to y
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    #built in function that returns the y coordinate
    y = paddle_a.ycor()
    #subtracts 20px to y
    y -= 30
    paddle_a.sety(y)



def paddle_b_up():
    #built in function that returns the y coordinate
    y = paddle_b.ycor()
    #adds 20px to y
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    #built in function that returns the y coordinate
    y = paddle_b.ycor()
    #subtracts 20px to y
    y -= 20
    paddle_b.sety(y)
















# Keyboard Binding
    # moves the paddle when "w is pressed"
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")















# Main game Loop

    # Every time the loop runs, it updates the screen
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # What happens when the ball hits the border
        # This if loop makes the ball bounce if it hits the top of the screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay beep.wav&")

        # This if loop makes the ball bounce if it hits the top of the screen
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay beep.wav&")

        # bounce of when hits the right side
    if ball.xcor() > 390:
            #ball back to the center
        ball.goto(0, 0)
            #reverse directions
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        os.system("afplay gamelost.wav&")


            # bounce of when hits the left side
    if ball.xcor() < -400:
            #ball back to the center
        ball.goto(0, 0)
            #reverse directions
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        os.system("afplay gamelost.wav&")

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay beep.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay beep.wav&")



