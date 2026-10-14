import math
import turtle

t= turtle.Turtle()
t.speed(100)
t.hideturtle()
turtle.bgcolor("black")
t.color("pink")
t.penup()
t.goto(200,0)
t.pendown()
for i in range(360):
    r= math.radians(i)
    a=200*math.cos(r*6)
    x= a*math.cos(r)
    y= a*math.sin(r)
    t.goto(x,y)

turtle.done()
