import math
import turtle

t= turtle.Turtle()
t.speed(500)
t.hideturtle()
turtle.bgcolor("black")
t.color("pink")
for i in range(2000):
    a= 0.1*i
    r= math.radians(i)
    x= a*math.cos(r)
    y= a*math.sin(r)
    t.goto(x,y)

turtle.done()


