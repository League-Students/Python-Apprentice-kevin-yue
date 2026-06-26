 import turtle
import time
import random

# 1. Screen Setup
screen = turtle.Screen()
screen.title("Highway Dash – Village Racer")
screen.bgcolor("gray20")
screen.setup(width=600, height=700)
screen.tracer(0) # Disable auto-update for smooth rendering

# 2. Score & Speed Variables
score = 0
speed = 2
game_over = False

# 3. Create Player Car
player = turtle.Turtle()
player.shape("square")
player.color("cyan")
player.shapesize(stretch_wid=2, stretch_len=1) # FIXED: stretch_len instead of stretch_to
player.penup()
player.goto(0, -250)

# 4. Create Enemy Cars
enemies = []
for _ in range(3):
    enemy = turtle.Turtle()
    enemy.shape("square")
    enemy.color("red")
    enemy.shapesize(stretch_wid=2, stretch_len=1) # FIXED: stretch_len instead of stretch_to
    enemy.penup()
    x = random.randint(-200, 200)
    y = random.randint(300, 600)
    enemy.goto(x, y)
    enemies.append(enemy)

# 5. Create Roads (Lane Dividers)
roads = []
for i in range(-5, 6):
    road = turtle.Turtle()
    road.speed(0)
    road.shape("square")
    road.color("white")
    road.shapesize(stretch_wid=2, stretch_len=0.2) # FIXED: stretch_len instead of stretch_to
    road.penup()
    road.goto(0, i * 100)
    roads.append(road)

# 6. Score Display
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 300)
scoreboard.write("Score: 0", align="center", font=("Courier", 24, "bold"))

# 7. Functions for Movement
def move_left():
    x = player.xcor()
    if x > -220:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 220:
        player.setx(x + 20)

# 8. Keyboard Bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# 9. Main Game Loop
while not game_over:
    screen.update()
    time.sleep(0.01)

    # Move Roads to create "scrolling" effect
    for road in roads:
        road.sety(road.ycor() - speed)
        if road.ycor() < -350:
            road.sety(350)

    # Move Enemies
    for enemy in enemies:
        enemy.sety(enemy.ycor() - (speed + 2)) # Enemies go slightly faster

        # Reset enemy when it goes off screen and increase score
        if enemy.ycor() < -350:
            enemy.goto(random.randint(-220, 220), random.randint(400, 600))
            score += 1
            speed += 0.1 # Gradually increase game difficulty
            
            scoreboard.clear()
            scoreboard.write(f"Score: {score}", align="center", font=("Courier", 24, "bold"))

        # Collision Detection (Check distance)
        if player.distance(enemy) < 22:
            game_over = True
            scoreboard.goto(0, 0)
            scoreboard.write("GAME OVER\nFinal Score: " + str(score), align="center", font=("Courier", 30, "bold"))

turtle.done()
