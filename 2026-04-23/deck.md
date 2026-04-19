# Æblejæger — Byg et to-spiller turtle-spil

Et Trinket Python turtle-spil bygget i fem trin. Til sidst kapper to spillere om at fange æbler med tastaturet.

**Styring (færdigt spil):**
- Spiller 1 (grøn): piletasterne
- Spiller 2 (blå): `W` `A` `S` `D`

**Tip:** klik én gang på det sorte lærred efter du har trykket Run, så tasterne har fokus.

---

## Trin 1 — En skildpadde på skærmen

**Mål:** åbn et grønt vindue med én skildpadde i midten.

**Nye ting:**
- `import` — henter kode som en anden har skrevet
- `turtle.Screen()` — tegnevinduet
- `turtle.Turtle()` — vores figur
- `.shape()`, `.color()`, `.penup()` — ændrer hvordan skildpadden ser ud og opfører sig

---

## Trin 1 — kode

Vi kalder den `player1` allerede nu — senere får vi en `player2`.

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

**Prøv:**
- Skift `"lightgreen"` ud med en anden farve.
- Skift `"turtle"` til `"circle"`, `"square"` eller `"arrow"`.
- Hvad sker der, hvis du fjerner `player1.penup()`?

---

## Trin 2 — Bevæg dig med piletasterne

**Mål:** op/ned kører frem og tilbage, venstre/højre drejer skildpadden.

**Nye ting:**
- **Funktioner** med `def` — en opskrift med et navn
- `player1.forward(STEP)` / `player1.forward(-STEP)` — bevæg; negativ går baglæns
- `player1.right(TURN)` / `player1.right(-TURN)` — drej; negativ drejer til venstre
- `screen.listen()` + `screen.onkey(...)` — "når denne tast trykkes, kør denne funktion"
- **Konstanter** med STORE BOGSTAVER som `STEP` og `TURN` — nemme at ændre ét sted

---

## Trin 2 — opsætning

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
```

---

## Trin 2 — funktioner

Funktionsnavnene starter med `p1_`, så vi senere let kan tilføje `p2_`-versioner.

```python
def p1_forward():
    player1.forward(STEP)

def p1_back():
    player1.forward(-STEP)

def p1_turn_left():
    player1.right(-TURN)

def p1_turn_right():
    player1.right(TURN)
```

---

## Trin 2 — tastebindinger

```python
screen.listen()
screen.onkey(p1_forward, "Up")
screen.onkey(p1_back, "Down")
screen.onkey(p1_turn_left, "Left")
screen.onkey(p1_turn_right, "Right")

turtle.mainloop()
```

**Prøv:**
- Gør skildpadden hurtigere ved at ændre `STEP`.
- Hvordan føles `TURN = 90`? `TURN = 5`?
- Fjern `player1.penup()` og kør rundt — nu tegner du!

---

## Trin 3 — Et æble dukker op

**Mål:** et rødt æble dukker op et tilfældigt sted på skærmen.

**Nye ting:**
- `import random` — til overraskelses-tal
- `random.randint(a, b)` — et helt tal mellem `a` og `b`
- En ekstra skildpadde brugt som pynt (ingen bevægelseskode)

---

## Trin 3 — kode

Tilføj øverst:

```python
import random
```

Tilføj efter spiller-koden, før tastebindingerne:

```python
apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(random.randint(-230, 230), random.randint(-230, 230))
```

**Prøv:**
- Kør programmet et par gange — æblet lander et nyt sted hver gang.
- Skift tallene `-230, 230` til noget mindre. Hvad sker der?

---

## Trin 4 — Fang æblet, få point

**Mål:** når skildpadden rører æblet, stiger scoren og æblet kommer tilbage et nyt sted.

**Nye ting:**
- `player1.distance(apple)` — afstanden mellem to skildpadder
- `if` — gør kun noget, når en betingelse er sand
- `global score1` — lader en funktion ændre en variabel udenfor sig selv
- En "writer"-skildpadde, der kun bruges til at skrive tekst
- At kalde `check_apple1()` efter hvert træk

Erstat hele filen. Vi bygger den i stykker over de næste slides.

---

## Trin 4 — opsætning

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
```

---

## Trin 4 — writer og variable

```python
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-240, 220)

score1 = 0
STEP = 20
TURN = 15
```

---

## Trin 4 — hjælpefunktioner

```python
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
```

---

## Trin 4 — bevægelse

```python
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
```

---

## Trin 4 — start spillet

```python
new_apple()
show_scores()

screen.listen()
screen.onkey(p1_forward, "Up")
screen.onkey(p1_back, "Down")
screen.onkey(p1_turn_left, "Left")
screen.onkey(p1_turn_right, "Right")

turtle.mainloop()
```

---

## Trin 4 — diskutér

- Hvorfor kalder vi `check_apple1()` inde i `p1_forward` og `p1_back`, men ikke i drejefunktionerne?
- Hvad ville der ske, hvis vi ændrede `< 20` til `< 5`? Til `< 100`?
- Hvorfor skal `score1` have `global` i `check_apple1`?

---

## Trin 5 — To spillere, ét æble

**Mål:** tilføj en blå skildpadde, der styres med WASD. Begge spillere jagter æblet. Hver har sin egen score.

Fordi vi allerede har brugt navnene `player1`, `score1`, `check_apple1` og `p1_*`, er det nu let at tilføje `player2`, `score2`, `check_apple2` og `p2_*` — uden at omdøbe noget.

Erstat hele filen. Vi bygger den i stykker.

---

## Trin 5 — to spillere

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
```

---

## Trin 5 — æble og writer

```python
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
```

---

## Trin 5 — æble og score-tekst

```python
def new_apple():
    apple.goto(random.randint(-230, 230), random.randint(-230, 230))

def show_scores():
    writer.clear()
    writer.write("P1: " + str(score1) + "   P2: " + str(score2), font=("Arial", 16, "bold"))
```

---

## Trin 5 — tjek for begge spillere

```python
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
```

---

## Trin 5 — spiller 1 bevægelse

```python
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
```

---

## Trin 5 — spiller 2 bevægelse

```python
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
```

---

## Trin 5 — start spillet

```python
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

---

## Trin 5 — diskutér

- Hvorfor har vi brug for to separate `check_apple`-funktioner? (De ændrer hver sin score.)
- Bemærk hvor ens `p1_forward` og `p2_forward` er. Kan man skrive det kun én gang? (Et godt emne til en fremtidig lektion.)

---

## Ekstra udfordringer

Vælg én og prøv:

1. **Først til 5 vinder** — når en score når 5, vis `writer.write("P1 vinder!")` og stop spillet.
2. **Skrumpende bane** — efter hvert æble, gør det tilladte område 10 pixels mindre.
3. **Giftigt æble** — tilføj en lilla prik, der trækker et point fra.
4. **Fart-powerup** — en gul prik, der midlertidigt øger `STEP` for den spiller, der fanger den.
5. **Mure** — tegn en rektangulær kant; stop skildpadden, hvis den rammer kanten.
6. **Timer** — brug `screen.ontimer(...)`, så æblet flytter sig hvert 2. sekund.
