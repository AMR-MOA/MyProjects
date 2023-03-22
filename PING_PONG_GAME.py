import turtle
from tkinter import *
from pygame import mixer

from PING_PONG_GAME2 import txt1, score

mixer.init()

win = turtle.Screen()
win.title("Ping Pong Game")
win.bgcolor(.1, .1, .1)
win.setup(width=800, height=600)
win.tracer(0)

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.10
txt1.goto(0, -245)
txt1.write("The program was programmed by Ammar Alotaibi", align="center", font=("Courier", 15, "normal"))

txt2 = turtle.Turtle()
txt2.speed(0)
txt2.color("white")
txt2.penup()
txt2.hideturtle()
txt2.goto(0, -275)
txt2.write("By: Ammar Alotaibi", align="center", font=("Courier", 15, "normal"))


txt3 = turtle.Turtle()
txt3.speed(0)
txt3.color("white")
txt3.penup()
txt3.hideturtle()
txt3.goto(-325, -245)
txt3.write("W = UP", align="center", font=("Courier", 15, "normal"))

txt4 = turtle.Turtle()
txt4.speed(0)
txt4.color("white")
txt4.penup()
txt4.hideturtle()
txt4.goto(-313, -275)
txt4.write("S = DOWN", align="center", font=("Courier", 15, "normal"))

txt5 = turtle.Turtle()
txt5.speed(0)
txt5.color("white")
txt5.penup()
txt5.hideturtle()
txt5.goto(288, -245)
txt5.write("UP KEY = UP", align="center", font=("Courier", 15, "normal"))

txt6 = turtle.Turtle()
txt6.speed(0)
txt6.color("white")
txt6.penup()
txt6.hideturtle()
txt6.goto(300, -275)
txt6.write("DOWN KEY = DOWN", align="center", font=("Courier", 15, "normal"))

def paddle1_up():
    if paddle1.ycor() > 240:
        paddle1.sety(-240)
        paddle1.dy *= -1
    else:
        y = paddle1.ycor()
        y += 20
        paddle1.sety(y)


def paddle1_down():
    if paddle1.ycor() < -240:
        paddle1.sety(240)
        paddle1.dy *= -1
    else:
        y = paddle1.ycor()
        y -= 20
        paddle1.sety(y)


def paddle2_up():
    if paddle2.ycor() > 240:
        paddle2.sety(-240)
        paddle2.dy *= 1
    else:
        y = paddle2.ycor()
        y += 20
        paddle2.sety(y)


def paddle2_down():
    if paddle2.ycor() < -240:
        paddle2.sety(240)
        paddle2.dy *= -1
    else:
        y = paddle2.ycor()
        y -= 20
        paddle2.sety(y)


win.onkeypress(paddle1_up, "w")
win.onkeypress(paddle1_down, "s")
win.onkeypress(paddle2_up, "Up")
win.onkeypress(paddle2_down, "Down")

lbl1 = Label(text="BLUE WINNER", font=("Courier", 20, "normal"), bg="black", fg="blue")
lbl2 = Label(text="RED WINNER", font=("Courier", 20, "normal"), bg="black", fg="red")

def aaa():
    lbl1.place(x=-100, y=-100)
    lbl2.place(x=-100, y=-100)
    text = turtle.Turtle()
    text.hideturtle()
    global score1
    global score2
    score1 = 0
    score2 = 0
    paddle1.sety(0)
    paddle2.sety(0)
    score.clear()
    score.write("BLUE: {}   RED: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


    win.listen()


    while True:

        win.update()

        b.place(x=-100, y=-100)

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score1 += 1
            score.clear()
            score.write("BLUE: {}   RED: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
            paddle1.sety(0)
            paddle2.sety(0)

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score.clear()
            score2 += 1
            score.write("BLUE: {}   RED: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
            paddle1.sety(0)
            paddle2.sety(0)

        if (ball.xcor() > 340 and ball.xcor() < 350) and (
                ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            mixer.music.load("ping.mp3")
            mixer.music.play()

        if (ball.xcor() < -340 and ball.xcor() > -350) and (
                ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            mixer.music.load("ping.mp3")
            mixer.music.play()

        if score1 == 5:
            lbl1.place(x=310, y=270)
            b.place(x=345, y=320)
            paddle1.sety(0)
            paddle2.sety(0)
            score1 = 0
            score2 = 0
            break

        elif score2 == 5:
            lbl2.place(x=310, y=270)
            b.place(x=345, y=320)
            paddle1.sety(0)
            paddle2.sety(0)
            score1 = 0
            score2 = 0
            break


b = Button(text="START GAME", width=15, height=3, command=aaa)
b.place(x=345, y=270)

win.mainloop()
