import turtle

# Встановлюємо чорний фон
turtle.bgcolor("black")

t = turtle.Turtle()

t.color("red", "red")

t.begin_fill()


t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)

t.end_fill()

t.penup()
t.goto(0, 90)  
t.pendown()

t.color("white")

t.hideturtle()
t.write("I love you\n fominvic81", align="center", font=("Courier", 16, "bold"))

turtle.done()