# Simple Python code to demonstrate various Turtle functions

import turtle
import tkinter.simpledialog as simpledialog

# Set up the window
window = turtle.Screen()
window.title("Turtle Graphics Demo")
window.bgcolor("white")

# Create a turtle
t = turtle.Turtle()

# Set pen size to 3
t.pensize(3)

# Set drawing color to blue
t.color("blue")

# Move the turtle forward by 100 units
t.forward(100)

# Turn the turtle right by 90 degrees
t.right(90)

# Move the turtle forward by 50 units
t.forward(50)

# Turn the turtle left by 90 degrees
t.left(90)

# Lift the pen up – no drawing when moving
t.penup()

# Move the turtle to a specific location
t.goto(0, 0)

# Put the pen down – drawing when moving
t.pendown()

# Draw a circle with radius of 25
t.circle(25)

# Draw a dot with diameter 10
t.dot(10)

# Set the turtle heading to 0 (East)
t.setheading(0)

# Change the turtle color
t.color("red")

# Draw a filled shape
t.begin_fill()
t.circle(50)
t.end_fill()

# Clear the drawing
t.clear()

# Reset the turtle's state
t.reset()

# Hide the turtle
t.hideturtle()

# Display the turtle
t.showturtle()

# Set the animation speed (0:fastest, 1:slowest, 10:normal)
t.speed(5)

# Display text
t.penup()
t.goto(-50, 50)
t.pendown()
t.write("Hello, Turtle!", font=("Arial", 16, "normal"))

# Get input with a dialog box
user_input = simpledialog.askstring("Input", "What shape would you like to draw?")

# Respond to user input
if user_input and user_input.lower() == "triangle":
    for _ in range(3):
        t.forward(100)
        t.left(120)

# Filling a shape with color
t.color("green", "yellow")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# Close the window on a click
window.mainloop()
