import turtle
import random

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("lightgreen")

player1 = turtle.Turtle()
player1.shape("turtle")
player1.color("darkgreen")
player1.penup()
player1.goto(-100, 0)

player2 = turtle.Turtle()
player2.shape("turtle")
player2.color("blue")
player2.penup()
player2.goto(100, 0)

apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-240, 220)

score1 = 0
score2 = 0
STEP = 20
TURN = 15

def new_apple():
    apple.goto(random.randint(-230, 230), random.randint(-230, 230))

def show_scores():
    writer.clear()
    writer.write("P1: " + str(score1) + "   P2: " + str(score2), font=("Arial", 16, "bold"))

def check_apple1():
    global score1
    if player1.distance(apple) < 20:
        score1 += 1
        new_apple()
        show_scores()

def check_apple2():
    global score2
    if player2.distance(apple) < 20:
        score2 += 1
        new_apple()
        show_scores()

def p1_forward():
    player1.forward(STEP)
    check_apple1()

def p1_back():
    player1.forward(-STEP)
    check_apple1()

def p1_turn_left():
    player1.right(-TURN)

def p1_turn_right():
    player1.right(TURN)

def p2_forward():
    player2.forward(STEP)
    check_apple2()

def p2_back():
    player2.forward(-STEP)
    check_apple2()

def p2_turn_left():
    player2.right(-TURN)

def p2_turn_right():
    player2.right(TURN)

new_apple()
show_scores()

screen.listen()
screen.onkey(p1_forward, "Up")
screen.onkey(p1_back, "Down")
screen.onkey(p1_turn_left, "Left")
screen.onkey(p1_turn_right, "Right")
screen.onkey(p2_forward, "w")
screen.onkey(p2_back, "s")
screen.onkey(p2_turn_left, "a")
screen.onkey(p2_turn_right, "d")

turtle.mainloop()
