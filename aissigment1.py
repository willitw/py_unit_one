#twig williams
#aissigment1.py
#9/20/23
#draws 4 octagons arranged in a square formation each with a different color

import turtle


# Function to draw fillled octogon with a color
def draw_filled_octagon(color):
   turtle.fillcolor(color)
   turtle.begin_fill()
   for _ in range(8):
       turtle.forward(70)
       turtle.right(45)
   turtle.end_fill()


# turtle settings
turtle.speed(0)
turtle.bgcolor("#d3d3d3")

#fun neon colors for the octogon
colors = ["#74ee15", "#f000ff", "#4deeea", "#ffe700"]


# spacing for the octagons
spacing = 190


# Draw the topleft octaon
draw_filled_octagon(colors[0])


# Move to the topright
turtle.penup()
turtle.goto(spacing, 0)
turtle.pendown()
# Draw the topright ocotagon
draw_filled_octagon(colors[1])


# Move to the bottomright
turtle.penup()
turtle.goto(spacing, -spacing)
turtle.pendown()
# Draw the bottomright octagon
draw_filled_octagon(colors[2])


# Move to the bottomleft
turtle.penup()
turtle.goto(0, -spacing)
turtle.pendown()
# Draw the bottomleft octagon
draw_filled_octagon(colors[3])


# Close the turtle window when clicked
turtle.exitonclick()
