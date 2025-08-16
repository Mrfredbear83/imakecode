import turtle
import time
import random

# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

# Left paddle (AI)
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# Right paddle (Player)
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Ball
hit_ball = turtle.Turtle()
hit_ball.speed(0)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = random.choice([-4, 4])   # slightly slower to help collisions
hit_ball.dy = random.choice([-4, 4])

# Scores
left_player = 0
right_player = 0

# Scoreboard
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))

# Player paddle controls (Right paddle only)
def paddlebup():
    y = right_pad.ycor()
    if y < 250:
        right_pad.sety(y + 20)

def paddlebdown():
    y = right_pad.ycor()
    if y > -240:
        right_pad.sety(y - 20)

sc.listen()
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

# Reset ball
def reset_ball():
    hit_ball.goto(0, 0)
    hit_ball.dx = random.choice([-4, 4])
    hit_ball.dy = random.choice([-4, 4])

# Main game loop
while True:
    sc.update()
    time.sleep(0.01)

    # Move ball
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # --- AI for left paddle ---
    if left_pad.ycor() < hit_ball.ycor() and abs(left_pad.ycor() - hit_ball.ycor()) > 10:
        left_pad.sety(left_pad.ycor() + 12)
    elif left_pad.ycor() > hit_ball.ycor() and abs(left_pad.ycor() - hit_ball.ycor()) > 10:
        left_pad.sety(left_pad.ycor() - 12)

    if random.randint(0, 40) == 1:
        left_pad.sety(left_pad.ycor() + random.choice([-20, 20]))

    # Border collisions
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    # Right wall (AI scores)
    if hit_ball.xcor() > 500:
        reset_ball()
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    # Left wall (Player scores)
    if hit_ball.xcor() < -500:
        reset_ball()
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    # Paddle collisions with buffer zone
    # Right paddle
    if (hit_ball.xcor() > 350 and hit_ball.xcor() < 370) and \
       (right_pad.ycor() - 60 < hit_ball.ycor() < right_pad.ycor() + 60):
        hit_ball.setx(350)  # push outside paddle
        hit_ball.dx *= -1

    # Left paddle (AI)
    if (hit_ball.xcor() < -350 and hit_ball.xcor() > -370) and \
       (left_pad.ycor() - 60 < hit_ball.ycor() < left_pad.ycor() + 60):
        hit_ball.setx(-350)
        hit_ball.dx *= -1