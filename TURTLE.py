import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(0)

# Set the background color
turtle.bgcolor("light green")

# Function to draw a petal
def draw_petal():
    t.color("red")  # Set the color of the petal
    t.begin_fill()  # Begin filling the shape
    t.circle(50, 60)  # Draw a partial circle for the petal
    t.left(120)  # Turn the turtle to the left
    t.circle(50, 60)  # Draw another partial circle for the petal
    t.end_fill()  # End filling the shape

# Draw the flower
for _ in range(6):
    draw_petal()  # Draw a petal
    t.left(60)    # Turn the turtle to the left

# Hide the turtle
t.hideturtle()

# Keep the window open until it's closed manually
turtle.mainloop()
