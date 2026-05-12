import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.speed(5)
pen.pensize(3)

# Function to draw a person
def draw_person(x, y, size=1, dress=False):

    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()

    # Head
    pen.circle(30 * size)

    # Body
    pen.right(90)
    pen.forward(80 * size)

    # Left Arm
    pen.backward(50 * size)
    pen.left(45)
    pen.forward(40 * size)

    # Right Arm
    pen.backward(40 * size)
    pen.right(90)
    pen.forward(40 * size)

    # Back to body
    pen.backward(40 * size)
    pen.left(45)
    pen.forward(50 * size)

    # Dress or legs
    if dress:
        # Dress shape
        pen.left(30)
        pen.forward(50 * size)

        pen.backward(50 * size)
        pen.right(60)
        pen.forward(50 * size)

    else:
        # Legs
        pen.left(45)
        pen.forward(50 * size)

        pen.backward(50 * size)
        pen.right(90)
        pen.forward(50 * size)

    # Reset direction
    pen.setheading(0)

# Draw Husband
draw_person(-150, 100, size=1, dress=False)

# Draw Wife
draw_person(50, 100, size=1, dress=True)

# Draw Son
draw_person(-100, -80, size=0.6, dress=False)

# Draw Daughter
draw_person(20, -80, size=0.6, dress=True)

# Hide turtle
pen.hideturtle()

# Keep window open
turtle.done()