#twig williams
#assignment_one.py
#9/20/23
#draws 4 octagons arranged in a square formation each with a different color

import turtle


# Function to draw filled octagon with a color
def draw_filled_octagon(color):
   turtle.fillcolor(color)
   turtle.begin_fill()
   for _ in range(8):
       turtle.forward(70)
       turtle.right(45)
   turtle.end_fill()

# Function to move the turtle
def movepen(xcoord,ycoord):
    turtle.penup()
    turtle.goto(xcoord,ycoord)
    turtle.pendown()


# turtle settings
turtle.speed(0)
turtle.bgcolor("#d3d3d3")


# fun neon colors for the octogon
colors = ["#74ee15", "#f000ff", "#4deeea", "#ffe700"]


# move to start position and draw top left octagon
movepen(-130, 170)
draw_filled_octagon(colors[0])

# move to the top right and draw top right octagon
movepen(60, 170)
draw_filled_octagon(colors[1])

# move to the bottom right and draw the bottom right octagon
movepen(-130, -20)
draw_filled_octagon(colors[2])

# move to the bottom left and draw the bottom left octagon
movepen(60, -20)
draw_filled_octagon(colors[3])


# Close the turtle window when clicked
turtle.exitonclick()
