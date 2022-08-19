import turtle
import random
turtle.bgcolor('black')
turtle.colormode(255)
turtle.speed(0)
turtle.width(1)
for x in range(1000):
    r, b, g = random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)
    turtle.pencolor(r, g, b)
    turtle.fd(x+50)
    turtle.rt(91)
turtle.exitonclick()
