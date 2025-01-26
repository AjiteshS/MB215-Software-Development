import turtle

# Set up parameters
ITERATIONS = 36  
ANGLE = 10       
SIZE = 100      

# Set up the Turtle screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black for better contrast
pattern_turtle = turtle.Turtle()
pattern_turtle.speed(0)  # Set the turtle speed to the fastest
pattern_turtle.pensize(2)  # Set the pen size

# Colors for the pattern
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Loop to draw the pattern
for i in range(ITERATIONS):
    # Change the color for each iteration
    pattern_turtle.pencolor(colors[i % len(colors)])
    
    # Draw a square
    for _ in range(4):
        pattern_turtle.forward(SIZE)
        pattern_turtle.right(90)  # Right angle for a square

    # Rotate the turtle 
    pattern_turtle.right(ANGLE)


