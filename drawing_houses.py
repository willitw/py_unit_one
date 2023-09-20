#twig williams
#drawing_houses.py
#9/20/23
#draws a simple house using turtle(so cute :] )

import turtle

# Create a turtle screen and set up the turtle
t = turtle.Screen()
t.bgcolor("white")



t = turtle.Turtle()
t.speed(0)  # Sets the turtles speed


# Function to draw square
def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)


# Function to draw triangle
def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)

for _ in range(4):
    t.penup()
    t.forward(100)
    t.pendown()
    #picks color for sqaure
    t.fillcolor("hotpink")

    t.begin_fill()
    # Draws the square
    draw_square()
    t.end_fill()

    #piuks color for triangle
    t.fillcolor("lightblue")

    t.begin_fill()
    # Draws the triangle
    draw_triangle()
    t.end_fill()

# Close the turtle window when clicked
turtle.exitonclick()