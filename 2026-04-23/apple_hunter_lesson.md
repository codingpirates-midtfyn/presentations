# Apple Hunter — Build a Two-Player Turtle Game

A Trinket Python turtle game built in five stages. By the end, two players race to grab apples with the keyboard.

**Controls (final game):**
- Player 1 (green): arrow keys
- Player 2 (blue): `W` `A` `S` `D`

**Tip:** click the black canvas once after you press Run, so the keys have focus.

---

## Stage 1 — A Turtle on the Screen

**Goal:** open a green window with one turtle in the middle.

**New things:**
- `import` — bringing in code someone else wrote
- `turtle.Screen()` — the drawing window
- `turtle.Turtle()` — our character
- `.shape()`, `.color()`, `.penup()` — change how the turtle looks and acts

We call it `player1` already — later we'll add `player2`.

```python
import turtle

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("lightgreen")

player1 = turtle.Turtle()
player1.shape("turtle")
player1.color("darkgreen")
player1.penup()

turtle.mainloop()
```

**Try it:**
- Change `"lightgreen"` to another color.
- Change `"turtle"` to `"circle"`, `"square"`, or `"arrow"`.
- What happens if you remove `player1.penup()`?

---

## Stage 2 — Move With Arrow Keys

**Goal:** up/down move forward and backward, left/right rotate the turtle.

**New things:**
- **Functions** with `def` — a recipe with a name
- `player1.forward(STEP)` / `player1.forward(-STEP)` — move; negative goes backward
- `player1.right(TURN)` / `player1.right(-TURN)` — rotate; negative turns left
- `screen.listen()` + `screen.onkey(...)` — "when this key is pressed, run this function"
- **Constants** in CAPS like `STEP` and `TURN` — easy to change one place

Function names start with `p1_` so we can later add `p2_` versions without renaming.

```python
import turtle

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("lightgreen")

player1 = turtle.Turtle()
player1.shape("turtle")
player1.color("darkgreen")
player1.penup()

STEP = 20
TURN = 15

def p1_forward():
    player1.forward(STEP)

def p1_back():
    player1.forward(-STEP)

def p1_turn_left():
    player1.right(-TURN)

def p1_turn_right():
    player1.right(TURN)

screen.listen()
screen.onkey(p1_forward, "Up")
screen.onkey(p1_back, "Down")
screen.onkey(p1_turn_left, "Left")
screen.onkey(p1_turn_right, "Right")

turtle.mainloop()
```

**Try it:**
- Make the turtle faster by changing `STEP`.
- What does `TURN = 90` feel like? `TURN = 5`?
- Remove `player1.penup()` and drive around — now you are drawing!

---

## Stage 3 — An Apple Appears

**Goal:** a red apple shows up somewhere random on the screen.

**New things:**
- `import random` — for surprise numbers
- `random.randint(a, b)` — a whole number between `a` and `b`
- A second turtle used as a decoration (no movement code)

Add at the top:

```python
import random
```

Add after the player code, before the key bindings:

```python
apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(random.randint(-230, 230), random.randint(-230, 230))
```

**Try it:**
- Run it a few times — the apple lands in a different spot each run.
- Change the numbers `-230, 230` to something smaller. What happens?

---

## Stage 4 — Catch the Apple, Score Points

**Goal:** when the turtle touches the apple, score goes up and the apple respawns.

**New things:**
- `player1.distance(apple)` — how far apart two turtles are
- `if` — do something only when a condition is true
- `global score1` — let a function change a variable outside it
- A "writer" turtle just for drawing text with `writer.write(...)`
- Calling `check_apple1()` after every move

Replace the whole file with this:

```python
import turtle
import random

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("lightgreen")

player1 = turtle.Turtle()
player1.shape("turtle")
player1.color("darkgreen")
player1.penup()

apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-240, 220)

score1 = 0
STEP = 20
TURN = 15

def new_apple():
    apple.goto(random.randint(-230, 230), random.randint(-230, 230))

def show_scores():
    writer.clear()
    writer.write("P1: " + str(score1), font=("Arial", 16, "bold"))

def check_apple1():
    global score1
    if player1.distance(apple) < 20:
        score1 += 1
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

new_apple()
show_scores()

screen.listen()
screen.onkey(p1_forward, "Up")
screen.onkey(p1_back, "Down")
screen.onkey(p1_turn_left, "Left")
screen.onkey(p1_turn_right, "Right")

turtle.mainloop()
```

**Discuss:**
- Why do we call `check_apple1()` inside `p1_forward` and `p1_back`, but not in the turn functions?
- What would happen if we changed `< 20` to `< 5`? To `< 100`?
- Why does `score1` need `global` in `check_apple1`?

---

## Stage 5 — Two Players, One Apple

**Goal:** add a blue turtle controlled with WASD. Both players race for the apple. Each has their own score.

Because we already used the names `player1`, `score1`, `check_apple1`, and `p1_*`, it is now easy to add `player2`, `score2`, `check_apple2`, and `p2_*` — no renaming needed.

Replace the whole file with the final version:

```python
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
```

**Discuss:**
- Why do we need two separate `check_apple` functions? (They change different scores.)
- Notice how similar `p1_forward` and `p2_forward` are. Is there a way to write it only once? (Good topic for a future class.)

---

## Stretch Challenges

Pick one and try it:

1. **First to 5 wins** — when a score reaches 5, show `writer.write("P1 wins!")` and stop the game.
2. **Shrinking map** — after each apple, shrink the allowed area by 10 pixels.
3. **Poison apple** — add a purple dot that subtracts a point.
4. **Speed power-up** — a yellow dot that temporarily raises `STEP` for the player who grabs it.
5. **Walls** — draw a rectangle border; stop the turtle if it hits the edge.
6. **Timer** — use `screen.ontimer(...)` so the apple moves every 2 seconds.
