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
        t.forward(100)  # Adjust the side length as needed
        t.right(90)

# Function to draw triangle
def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)

# Draws the square
draw_square()
# Draws the triangle
draw_triangle()

# Close the turtle window when clicked
turtle.exitonclick()
