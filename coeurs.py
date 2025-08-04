# heart code 
import turtle
import math

t =  turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("pink")

def coeur(n):
    x = 16 * math.sin(n)**3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

t.penup()
for i in range (15):
    t.goto(0,0)
    t.pendown()
    for n in range(0, 628, 1):
        x, y = coeur(n / 20)
        t.goto(x * 10, y * 10)
    t.penup()

turtle.done()

