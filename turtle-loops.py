import turtle

t= turtle.Turtle()
turtle.bgcolor("black")
t.hideturtle()
t.color("green")
t.speed(10)

for i in range(90):
    t.forward(i*5)
    t.right(90)

turtle.done()

