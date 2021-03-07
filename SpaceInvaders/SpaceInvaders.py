# Space Invaders -- Part 1


import turtle
import math
import os

# Set up Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Create enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)
enemyspeed = 2


# Create player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20
#Define bullet state
#ready - ready to fire
#fire - firing

bulletstate = "ready"

# Move player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    # Declare bulletstate as global if needs to change
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move bullet to just above player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Create Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


# Main game loop
while True:

    # Move enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #Move enemy other way and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    # Move bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check bullet to see if it reached top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    # Check for a collision between enemy and bullet
    if isCollision(bullet, enemy):
        # Reset bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # Reset the enemy
        enemy.setposition(-200, 250)


    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break

# Prevent from closing immediately
delay = input("Press enter to finish.")
