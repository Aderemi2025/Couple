import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(5)
pen.pensize(3)

# Function to draw a person
def draw_person(x, y, dress=False):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    # Head
    pen.circle(30)

    # Body
    pen.right(90)
    pen.forward(80)

    # Arms
    pen.backward(50)
    pen.left(45)
    pen.forward(40)

    pen.backward(40)
    pen.right(90)
    pen.forward(40)

    pen.backward(40)
    pen.left(45)
    pen.forward(50)

    # Legs or Dress
    if dress:
        pen.left(30)
        pen.forward(50)

        pen.backward(50)
        pen.right(60)
        pen.forward(50)
    else:
        pen.left(45)
        pen.forward(50)

        pen.backward(50)
        pen.right(90)
        pen.forward(50)

    # Reset direction
    pen.setheading(0)

# Draw Husband
draw_person(-100, 100, dress=False)

# Draw Wife
draw_person(100, 100, dress=True)

pen.hideturtle()

turtle.done()