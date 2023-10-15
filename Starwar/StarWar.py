import os
from playsound import playsound
import turtle


screen=turtle.Screen()
screen.bgpic("space.gif")
turtle.shape("triangle")
turtle.color('red')
move_speed = 10
turn_speed = 10
def forward():
    turtle.forward(move_speed)
def backward():
    turtle.backward(move_speed)
def left():
    turtle.left(turn_speed)
def right():
    turtle.right(turn_speed)
def pen():
    turtle.pendown()
def up():
    turtle.penup()
def tamgiac():
    turtle.shape("triangle")
def rua():
    turtle.shape("turtle")

turtle.penup()
screen.onkey(forward,"w")
screen.onkey(backward, "s")
screen.onkey(left,"d")
screen.onkey(right, "a")


if screen.onkey(tamgiac,"t"):
    playsound("over.wav")
elif screen.onkey(rua,"h"):
    playsound("over.wav")
elif screen.onkey(pen,"space"):
    playsound("over.wav")
elif screen.onkey(up,"r"):
    playsound("over.wav")

screen.listen()
turtle.done()
