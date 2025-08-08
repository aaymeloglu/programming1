import turtle

# Global variables to maintain game state
screen = None
drawer = None
miss_count = 0


def init_game():
    """Initialize the hangman game board with empty gallows"""
    global screen, drawer, miss_count
    
    # Reset miss count
    miss_count = 0
    
    # Set up the screen
    if screen is None:
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.bgcolor("white")
        screen.title("Hangman")
    
    # Clear the screen
    screen.clear()
    
    # Create turtle for drawing
    drawer = turtle.Turtle()
    drawer.speed(0)
    drawer.pensize(3)
    
    # Draw the gallows
    drawer.pencolor("black")
    drawer.penup()
    drawer.goto(200, -150)
    drawer.pendown()
    drawer.setheading(90)  # Point up
    drawer.forward(300)    # Vertical post
    drawer.left(90)        # Turn left
    drawer.forward(100)    # Horizontal beam
    drawer.left(90)       # Turn down
    drawer.forward(30)     # Noose rope
    
    # Hide the turtle
    drawer.hideturtle()


def add_miss():
    """Add the next body part to the hanging figure"""
    global drawer, miss_count
    
    if drawer is None:
        return
    
    drawer.pensize(2)
    drawer.pencolor("red")
    
    # Draw body parts in order: head, body, left arm, right arm, left leg, right leg
    if miss_count == 0:  # Head
        drawer.penup()
        drawer.goto(80, 100)
        drawer.pendown()
        drawer.circle(20)
    elif miss_count == 1:  # Body
        drawer.penup()
        drawer.goto(100, 80)
        drawer.pendown()
        drawer.setheading(270)  # Point down
        drawer.forward(80)
    elif miss_count == 2:  # Left arm
        drawer.penup()
        drawer.goto(100, 60)
        drawer.pendown()
        drawer.setheading(225)  # Point down-left
        drawer.forward(30)
    elif miss_count == 3:  # Right arm
        drawer.penup()
        drawer.goto(100, 60)
        drawer.pendown()
        drawer.setheading(315)  # Point down-right
        drawer.forward(30)
    elif miss_count == 4:  # Left leg
        drawer.penup()
        drawer.goto(100, 0)
        drawer.pendown()
        drawer.setheading(225)  # Point down-left
        drawer.forward(30)
    elif miss_count == 5:  # Right leg
        drawer.penup()
        drawer.goto(100, 0)
        drawer.pendown()
        drawer.setheading(315)  # Point down-right
        drawer.forward(30)
    
    miss_count += 1


def set_word(word_display: str):
    """Display the word with letters and underscores on the left side"""
    global drawer
    
    if drawer is None:
        return
    
    # Add spacing between letters for better readability
    spaced_display = " ".join(word_display)
    
    # Write the new word
    drawer.pencolor("black")
    drawer.penup()
    drawer.goto(-200, -50)
    drawer.write(spaced_display, align="center", font=("Arial", 32, "normal"))


def set_guesses(guesses_display: str):
    """Display the previous guesses in the upper left"""
    global drawer
    
    if drawer is None:
        return
    
    # Write the guesses
    drawer.pencolor("black")
    drawer.penup()
    drawer.goto(-350, 220)
    drawer.write(f"Guesses: {guesses_display}", align="left", font=("Arial", 16, "normal"))