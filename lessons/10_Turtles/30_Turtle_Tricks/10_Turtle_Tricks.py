import turtle
import time
import random

# Game Configuration
delay = 0.1
score = 0
high_score = 0

# Screen Setup
win = turtle.Screen()
win.title("Classic Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)  # Turns off screen updates for manual control

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Segments for Snake Body
segments = []

# Scoreboard Display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to Control Direction
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def reset_game():
    global score, delay
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide segments off-screen and clear list
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    # Reset score and update scoreboard
    score = 0
    delay = 0.1
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Keyboard Bindings
win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")

# Main Game Loop
while True:
    win.update()

    # 1. Check Border Collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game()

    # 2. Check Food Collision
    if head.distance(food) < 20:
        # Move food to a random spot on the grid
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        # Add a new segment to the snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten delay to speed up the game slightly
        delay -= 0.002

        # Increase score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # 3. Move Body Segments in Reverse Order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head was
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # 4. Check Self-Collisions
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    time.sleep(delay)

win.mainloop()
turtle.exitonclick()                    # Close the window when we click on it