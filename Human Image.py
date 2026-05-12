import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(3)

# Head
pen.penup()
pen.goto(0, 100)
pen.pendown()
pen.circle(40)

# Body
pen.right(90)
pen.forward(120)

# Left Arm
pen.backward(80)
pen.left(45)
pen.forward(60)

# Right Arm
pen.backward(60)
pen.right(90)
pen.forward(60)

# Back to body
pen.backward(60)
pen.left(45)
pen.forward(80)

# Left Leg
pen.left(45)
pen.forward(70)

# Right Leg
pen.backward(70)
pen.right(90)
pen.forward(70)

# Hide turtle
pen.hideturtle()

# Keep window open
turtle.done()
