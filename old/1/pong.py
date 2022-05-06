import turtle

win = turtle.Screen()
win.title("Pong by @rihan_ nnn")
win.bgcolor("#222324")
win.setup(width=800, height=600)
win.tracer(0)

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#fb8d46")
paddle_a.shapesize(stretch_wid=7, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#fb9546")
paddle_b.shapesize(stretch_wid=7, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#ff1e2a")

ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2



#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
#key binding

win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")




#Main Game Loop

while True:
    win.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1






     