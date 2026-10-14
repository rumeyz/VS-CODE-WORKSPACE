import math
import turtle

t= turtle.Turtle()
t.speed(100)
t.hideturtle()
turtle.bgcolor("black")
t.color("pink")
t.penup()
t.goto(100,0)
t.pendown()
for i in range(360):
    r= math.radians(i)
    x= 100*math.cos(r)
    y= 100*math.sin(r)
    t.goto(x,y)

turtle.done()


