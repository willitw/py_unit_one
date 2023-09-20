#twig williams
#drawing_houses.py
#9/20/23
#draws 4 houses for picky little rats who need all diffrnt sized houses each with a differnt color combo


import turtle

# Function to draw a square
def draw_square(size, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

# Function to draw a triangle on top of a square(to make a house)
def draw_house(size, square_color, triangle_color):
    draw_square(size, square_color)

    # Move to the starting position for the triangle
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor() + size)
    turtle.pendown()

    # Draw the triangle
    turtle.begin_fill()
    turtle.fillcolor(triangle_color)
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

# turtle settings
turtle.speed(0)
turtle.bgcolor("skyblue")

# Draw the 1st house
turtle.penup()
turtle.goto(-150, -150)
turtle.pendown()
draw_house(100, "red", "orange")

# Draw the 2nd house
turtle.penup()
turtle.goto(-50, -150)
turtle.pendown()
draw_house(80, "green", "yellow")

# Draw the 3rd house
turtle.penup()
turtle.goto(30, -150)
turtle.pendown()
draw_house(60, "blue", "purple")

# Draw the 4th house
turtle.penup()
turtle.goto(90, -150)
turtle.pendown()
draw_house(120, "hotpink", "white")

# Close the turtle window when clicked
turtle.exitonclick()
