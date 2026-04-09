# 🐍 Micro:bit Python Workshop – Snake (5×5)

[deck.pdf](code/deck.pdf)

## Symboler

- 👨‍🏫 = Vi laver dette sammen i klassen
- 🧑‍💻 = Du prøver selv / mission
- 💡 = Hint hvis du sidder fast
- 👑 = Ekstra svær udfordring

---

# 📟 Micro:bit skærmen (5 × 5)

Micro:bit har et **5 × 5 gitter**.

```
x →
0 1 2 3 4
---------
|       | 0
|       | 1
|       | 2
|       | 3
|       | 4
---------
        ↑
        y
```

Eksempel:

```python
display.set_pixel(2,4,9)
```

---

# 🎮 Hvad er Snake på 5×5?

- Du styrer en slange med et **hoved**.
- Du spiser **mad** (et pixel).
- Når du spiser, bliver du **længere**.
- Du taber hvis du rammer din **egen krop**.

I dag bruger vi:

- **A** = drej venstre
- **B** = drej højre
- **Væg** = stopper dig (ingen game over)

---

# Level 1 – Tegn et hoved

👨‍🏫 Vi starter med ét pixel som “slangens hoved”.

```python
from microbit import *

x = 2
y = 2

while True:
    display.clear()
    display.set_pixel(x, y, 9)
    sleep(200)
```

🧑‍💻 **Mission**  
Flyt `x` og `y` manuelt (fx `x = 0`, `y = 4`) og se hvor pixlen ender.

---

# Level 2 – Retning (op/højre/ned/venstre)

👨‍🏫 Vi giver retningerne navne (konstanter), så vi slipper for “magiske tal”.

```python
from microbit import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

x = 2
y = 2
direction = UP  # start med at kigge op

while True:
    display.clear()
    display.set_pixel(x, y, 9)
    sleep(400)

    if direction == UP:
        y -= 1
    elif direction == RIGHT:
        x += 1
    elif direction == DOWN:
        y += 1
    elif direction == LEFT:
        x -= 1
```

🧑‍💻 **Mission**  
Skift `direction` til `UP`, `RIGHT`, `DOWN`, `LEFT` og se hvad der sker.

---

# Level 3 – Drej med knapperne

👨‍🏫 A drejer venstre, B drejer højre.

```python
from microbit import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

x = 2
y = 2
direction = UP

while True:
    if button_a.was_pressed():
        direction -= 1
        if direction < UP:
            direction = LEFT

    if button_b.was_pressed():
        direction += 1
        if direction > LEFT:
            direction = UP

    display.clear()
    display.set_pixel(x, y, 9)
    sleep(400)

    if direction == UP:
        y -= 1
    elif direction == RIGHT:
        x += 1
    elif direction == DOWN:
        y += 1
    elif direction == LEFT:
        x -= 1
```

🧑‍💻 **Mission**  
Prøv at dreje hurtigt. Føles det som Snake?

---

# 💡 Wrap rundt med `if` (nemmest)

👨‍🏫 Vi har **4** retninger (0,1,2,3).  
Når vi drejer, skal vi “wrappe” så vi altid ender i **0–3** igen.

Tænk på det som et “ur” med 4 tal:

```
0 → 1 → 2 → 3 → (tilbage til 0)
```

Sådan gør vi i koden:

```python
direction += 1
if direction > LEFT:
    direction = UP
```

Og når vi drejer den anden vej:

```python
direction -= 1
if direction < UP:
    direction = LEFT
```

🧑‍💻 **Mini-mission**  
Hvis `direction = LEFT` og du trykker B, hvad bliver den så?  
Hvis `direction = UP` og du trykker A, hvad bliver den så?

💡 **Mere avanceret (senere)**  
Man kan også skrive det kort med “modulo” (fx `% 4`), men `if`-versionen er nemmest at forstå.

---

# 👑 Optimering: samme idé med `% 4` (kortere)

👨‍🏫 Når man bliver mere øvet, kan man skrive wrap-koden kortere med **modulo**.

Idéen er den samme: vi vil altid ende i en af de **4** retninger.

```python
# Drej højre
direction = (direction + 1) % 4

# Drej venstre
direction = (direction - 1) % 4
```

💡 **Husk**  
Det er bare en “smart genvej” til den `if`-wrap vi lige har lært.

---

# Level 4 – Væg stopper (ingen crash)

👨‍🏫 Hvis næste felt er udenfor skærmen, så bliver vi stående.

```python
from microbit import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

x = 2
y = 2
direction = UP

while True:
    if button_a.was_pressed():
        direction -= 1
        if direction < UP:
            direction = LEFT

    if button_b.was_pressed():
        direction += 1
        if direction > LEFT:
            direction = UP

    # Beregn næste position uden at flytte endnu
    nx = x
    ny = y

    if direction == UP:
        ny -= 1
    elif direction == RIGHT:
        nx += 1
    elif direction == DOWN:
        ny += 1
    elif direction == LEFT:
        nx -= 1

    # Flyt kun hvis inde i 0..4
    if 0 <= nx <= 4 and 0 <= ny <= 4:
        x = nx
        y = ny

    display.clear()
    display.set_pixel(x, y, 9)
    sleep(350)
```

🧑‍💻 **Mission**  
Hvad sker der når du prøver at gå ud over kanten?

---

# Level 5 – Kroppen (en liste!)

👨‍🏫 Slangen er en liste af punkter. Første element er hovedet.

```python
from microbit import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = [(2, 2)]  # [(x,y), (x,y), ...]
direction = UP

while True:
    if button_a.was_pressed():
        direction -= 1
        if direction < UP:
            direction = LEFT
    if button_b.was_pressed():
        direction += 1
        if direction > LEFT:
            direction = UP

    head_x, head_y = snake[0]
    nx = head_x
    ny = head_y

    if direction == UP:
        ny -= 1
    elif direction == RIGHT:
        nx += 1
    elif direction == DOWN:
        ny += 1
    elif direction == LEFT:
        nx -= 1

    # Væg stopper
    if 0 <= nx <= 4 and 0 <= ny <= 4:
        # Nytt hoved forrest
        snake.insert(0, (nx, ny))
        # Fjern hale (så længden er den samme)
        snake.pop()

    # Tegn
    display.clear()
    hx, hy = snake[0]
    display.set_pixel(hx, hy, 9)
    sleep(350)
```

🧑‍💻 **Mission**  
Gør slangen længere: prøv at ændre `snake = [(2,2)]` til fx `[(2,2),(2,3),(2,4)]`.

💡 **Hint**  
Husk: første punkt er hovedet.

---

# Level 6 – Tegn hele slangen

👨‍🏫 Nu tegner vi alle segmenter.

```python
from microbit import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = [(2, 2), (2, 3), (2, 4)]
direction = UP

while True:
    if button_a.was_pressed():
        direction -= 1
        if direction < UP:
            direction = LEFT
    if button_b.was_pressed():
        direction += 1
        if direction > LEFT:
            direction = UP

    head_x, head_y = snake[0]
    nx = head_x
    ny = head_y

    if direction == UP:
        ny -= 1
    elif direction == RIGHT:
        nx += 1
    elif direction == DOWN:
        ny += 1
    elif direction == LEFT:
        nx -= 1

    if 0 <= nx <= 4 and 0 <= ny <= 4:
        snake.insert(0, (nx, ny))
        snake.pop()

    display.clear()

    # krop
    for x, y in snake[1:]:
        display.set_pixel(x, y, 4)

    # hoved
    hx, hy = snake[0]
    display.set_pixel(hx, hy, 9)

    sleep(350)
```

🧑‍💻 **Mission**  
Prøv at ændre lysstyrken på kroppen (0–9). Hvad ser bedst ud?

---

# Level 7 – Mad 🍎 (spawn et tomt sted)

👨‍🏫 Vi laver “food” som spawner et sted hvor slangen ikke er.

```python
from microbit import *
import random

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = [(2, 2), (2, 3)]
direction = UP

food = (random.randint(0, 4), random.randint(0, 4))

def spawn_food():
    while True:
        f = (random.randint(0, 4), random.randint(0, 4))
        if f not in snake:
            return f

food = spawn_food()

while True:
    if button_a.was_pressed():
        direction -= 1
        if direction < UP:
            direction = LEFT
    if button_b.was_pressed():
        direction += 1
        if direction > LEFT:
            direction = UP

    head_x, head_y = snake[0]
    nx = head_x
    ny = head_y

    if direction == UP:
        ny -= 1
    elif direction == RIGHT:
        nx += 1
    elif direction == DOWN:
        ny += 1
    elif direction == LEFT:
        nx -= 1

    ate = False

    if 0 <= nx <= 4 and 0 <= ny <= 4:
        snake.insert(0, (nx, ny))

        if (nx, ny) == food:
            ate = True
            food = spawn_food()
        else:
            snake.pop()

    display.clear()

    # food
    fx, fy = food
    display.set_pixel(fx, fy, 6)

    # snake
    for x, y in snake[1:]:
        display.set_pixel(x, y, 4)
    hx, hy = snake[0]
    display.set_pixel(hx, hy, 9)

    sleep(350)
```

🧑‍💻 **Mission**  
Når du spiser, vokser slangen. Virker det altid?

💡 **Hint**  
Det er forskellen på `snake.pop()` (ikke spist) og “ingen pop” (spist).

---

# Level 8 – Kollision med dig selv 💥

👨‍🏫 Hvis det nye hoved rammer kroppen → game over.

Tilføj denne tjek lige efter du har beregnet `(nx, ny)` og før du flytter:

```python
if 0 <= nx <= 4 and 0 <= ny <= 4 and (nx, ny) in snake:
    display.show(Image.SKULL)
    sleep(1000)
    break
```

🧑‍💻 **Mission**  
Kan du få game over med vilje?

---

# Level 9 – Komplet Snake 🎮

👨‍🏫 Her er hele spillet samlet (med score = længde).

```python
from microbit import *
import random

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = [(2, 2), (2, 3)]
direction = UP
speed_ms = 350

def spawn_food():
    while True:
        f = (random.randint(0, 4), random.randint(0, 4))
        if f not in snake:
            return f

food = spawn_food()

while True:
    if button_a.was_pressed():
        direction -= 1
        if direction < UP:
            direction = LEFT
    if button_b.was_pressed():
        direction += 1
        if direction > LEFT:
            direction = UP

    head_x, head_y = snake[0]
    nx = head_x
    ny = head_y

    if direction == UP:
        ny -= 1
    elif direction == RIGHT:
        nx += 1
    elif direction == DOWN:
        ny += 1
    elif direction == LEFT:
        nx -= 1

    # Væg stopper
    if not (0 <= nx <= 4 and 0 <= ny <= 4):
        nx, ny = head_x, head_y

    # Kollision (kun hvis vi faktisk flytter)
    if (nx, ny) != (head_x, head_y) and (nx, ny) in snake:
        display.show(Image.SKULL)
        sleep(800)
        display.scroll("Len:" + str(len(snake)))
        break

    # Flyt
    ate = False
    if (nx, ny) != (head_x, head_y):
        snake.insert(0, (nx, ny))

        if (nx, ny) == food:
            ate = True
            food = spawn_food()
        else:
            snake.pop()

    # Tegn
    display.clear()

    fx, fy = food
    display.set_pixel(fx, fy, 6)

    for x, y in snake[1:]:
        display.set_pixel(x, y, 4)
    hx, hy = snake[0]
    display.set_pixel(hx, hy, 9)

    # Bonus: blink når du spiser
    if ate:
        sleep(120)

    sleep(speed_ms)
```

---

# 🧑‍💻 Missioner (Snake)

1. Gør slangen **hurtigere** hver gang du spiser (men ikke for hurtigt!)
2. Vis **score** (længde) ind imellem ved at scrolle den
3. Lav en “**pause**” med A+B (tryk begge for at pause/fortsætte)
4. Gør mad **sjældnere** (fx kun spawn ny mad hver 2. gang du spiser)
5. Skift til **wrap rundt** i kanten i stedet for væg-stop

---

# 👑 Ekstra udfordringer (svære)

## 1. Wrap rundt i kanten

Hvis du vil wrappe:

```python
nx = (nx + 5) % 5
ny = (ny + 5) % 5
```

## 2. Mad som ikke spawner “for tæt på”

Gør det sværere ved at undgå food lige ved siden af hovedet.

## 3. Forhindringer

Lav en liste af faste blokke (walls). Spawner aldrig mad på dem.

---

# 🔧 Hvis din kode ikke virker

Tjek:

- Python **indrykninger**
- at `while True:` stadig er der
- at variabelnavne er stavet rigtigt
- prøv små ændringer og test igen

---

💡 **Programmeringshemmelighed:**

De bedste programmører laver fejl hele tiden.  
De prøver bare igen.
