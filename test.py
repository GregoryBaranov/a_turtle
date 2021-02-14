# Подключи нужные модули
from turtle import *
from random import randint
from time import sleep
w = 200
h = 200
t = Turtle()
t.shape("turtle")
t.color("red")
t.penup()
t.points = 0
def rand_move():
    t.goto(randint(-w,w), randint(-h,h))

def catch(x,y):
    t.write("Больно!", font=("Arial", 14, "normal"))
    t.points +=1

t.onclick(catch)

while t.points < 3:
    sleep(1.5)
    rand_move()

t.write("Ты выиграл!", font=("Arial", 16, "normal"))
t.hideturtle()
