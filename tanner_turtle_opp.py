import turtle
import math
import random


t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

t.shape("turtle")
t.pensize(1)
t.pencolor("white")
t.speed(0)
t.penup()
t.goto(x = -407, y = 403)
t.pendown()

f = 1

def side():

    t.fillcolor("white")
    t.begin_fill()
    t.right(45)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.end_fill()
def next():
    t.penup()
    t.right(45)
    t.forward(143)
    t.pendown()
def row1():
    global f
    t.penup()
    t.goto(x = -407, y = 403)
    t.setheading(270)
    t.forward(142*f)
    t.right(270)
    t.pendown()
    f = f+1

def next2():
    t.penup()
    t.right(135)
    t.forward(143)
    t.left(90)
    t.pendown()


def whole():
    range(6)
    for col in range(6):
        for row in range(7):
            side()
            next()
        row1()
    
whole()
t.penup()
t.goto(x = -200, y = 0)
t.pendown()
t.pencolor("red")
t.write("Boom!", font=("Arial", 100, "bold"))
t.penup()
t.goto(-700, 7000)
turtle.done()