
# 🎮 Micro:bit Python Workshop – Undgå Stenen

[deck.pdf](code/deck.pdf)

## Symboler

- 👨‍🏫 = Vi laver dette sammen i klassen
- 🧑‍💻 = Du prøver selv / mission
- 💡 = Hint hvis du sidder fast
- 👑 = Ekstra svær udfordring

---

# 📟 Micro:bit skærmen

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

# Flyt spilleren

👨‍🏫 Vi laver en spiller der kan flyttes med knapperne.

```python
from microbit import *

x = 2

while True:

    if button_a.was_pressed():
        x -= 1

    if button_b.was_pressed():
        x += 1

    display.clear()
    display.set_pixel(x,4,9)
```

🧑‍💻 **Mission**  
Hvad sker der hvis `x` bliver **-1** eller **5**?

💡 **Hint**

```python
x = max(0,x)
x = min(4,x)
```

---

# Level 2 – Faldende sten

👨‍🏫 Vi laver en sten der falder ned.

```python
from microbit import *
import random

rock_x = random.randint(0,4)
rock_y = 0

while True:

    display.clear()
    display.set_pixel(rock_x,rock_y,9)

    sleep(300)

    rock_y += 1
```

🧑‍💻 **Mission**  
Få stenen til at starte forfra når den rammer bunden.

💡 **Hint**

```python
if rock_y > 4:
    rock_y = 0
    rock_x = random.randint(0,4)
```

---

# Level 3 – Rigtigt spil

👨‍🏫 Nu kombinerer vi spiller og sten.

```python
from microbit import *
import random

player = 2
rock_x = random.randint(0,4)
rock_y = 0

while True:

    if button_a.was_pressed():
        player -= 1

    if button_b.was_pressed():
        player += 1

    player = max(0,min(4,player))

    display.clear()

    display.set_pixel(player,4,9)
    display.set_pixel(rock_x,rock_y,9)

    sleep(300)

    rock_y += 1

    if rock_y > 4:
        rock_y = 0
        rock_x = random.randint(0,4)
```

---

# Level 4 – Game over

👨‍🏫 Hvis stenen rammer spilleren taber man.

```python
if rock_y == 4 and rock_x == player:
    display.show(Image.SKULL)
    sleep(2000)
```

---

# Level 5 – Skyd tilbage! 🚀

👨‍🏫 Nu skal vi kunne skyde stenene!

Vi tilføjer et skud der flyver opad når vi trykker på A+B samtidig.

```python
from microbit import *
import random

player = 2
rock_x = random.randint(0,4)
rock_y = 0

# Skud variabler
bullet_x = 0
bullet_y = 0
bullet_active = False

while True:

    # Bevæg spiller
    if button_a.was_pressed():
        player -= 1

    if button_b.was_pressed():
        player += 1

    player = max(0,min(4,player))

    # Skyd!
    if button_a.is_pressed() and button_b.is_pressed():
        if not bullet_active:
            bullet_x = player
            bullet_y = 4
            bullet_active = True

    # Bevæg skud
    if bullet_active:
        bullet_y -= 1
        if bullet_y < 0:
            bullet_active = False

    # Bevæg sten
    rock_y += 1
    if rock_y > 4:
        rock_y = 0
        rock_x = random.randint(0,4)

    # Game over
    if rock_y == 4 and rock_x == player:
        display.show(Image.SKULL)
        sleep(2000)
        break

    # Tegn alt
    display.clear()
    display.set_pixel(player,4,9)
    display.set_pixel(rock_x,rock_y,9)

    if bullet_active:
        display.set_pixel(bullet_x,bullet_y,5)

    sleep(300)
```

🧑‍💻 **Mission**
Koden virker, men skuddet rammer ikke stenen endnu!

---

# Level 6 – Kollision! 💥

👨‍🏫 Nu skal vi tjekke om skuddet rammer stenen.

Tilføj dette efter "Bevæg skud":

```python
# Tjek om skud rammer sten
# Vi tjekker om bullet_y <= rock_y fordi skuddet kan "hoppe over" stenen!
if bullet_active and bullet_x == rock_x and bullet_y <= rock_y:
    # Ramte!
    display.show(Image.HAPPY)
    sleep(500)

    # Ny sten
    rock_y = 0
    rock_x = random.randint(0,4)

    # Fjern skud
    bullet_active = False
```

🧑‍💻 **Mission**
Prøv at skyde stenene! Virker det?

💡 **Hvorfor `bullet_y <= rock_y`?**
Fordi skuddet bevæger sig hurtigt opad kan det "springe over" stenen mellem frames. Hvis skuddet er samme sted eller allerede passeret stenen på samme x-position, så har det ramt!

---

# Level 7 – Komplet Space Invaders! 🎮

👨‍🏫 Nu laver vi hele spillet med score og game over.

```python
from microbit import *
import random

player = 2
rock_x = random.randint(0,4)
rock_y = 0

bullet_x = 0
bullet_y = 0
bullet_active = False

score = 0

while True:

    # Bevæg spiller
    if button_a.was_pressed() and not button_b.is_pressed():
        player -= 1

    if button_b.was_pressed() and not button_a.is_pressed():
        player += 1

    player = max(0,min(4,player))

    # Skyd!
    if button_a.is_pressed() and button_b.is_pressed():
        if not bullet_active:
            bullet_x = player
            bullet_y = 4
            bullet_active = True

    # Bevæg skud
    if bullet_active:
        bullet_y -= 1
        if bullet_y < 0:
            bullet_active = False

    # Tjek kollision
    if bullet_active and bullet_x == rock_x and bullet_y <= rock_y:
        score += 1
        display.show(Image.HAPPY)
        sleep(300)

        rock_y = 0
        rock_x = random.randint(0,4)
        bullet_active = False

    # Bevæg sten
    rock_y += 1
    if rock_y > 4:
        rock_y = 0
        rock_x = random.randint(0,4)

    # Game over
    if rock_y == 4 and rock_x == player:
        display.show(Image.SKULL)
        sleep(1000)
        display.scroll("Score: " + str(score))
        break

    # Tegn alt
    display.clear()
    display.set_pixel(player,4,9)
    display.set_pixel(rock_x,rock_y,9)

    if bullet_active:
        display.set_pixel(bullet_x,bullet_y,5)

    sleep(300)
```

---

# 🧑‍💻 Missioner (Space Invaders version)

1. Lav **flere skud** – skyd hurtigere!
2. Tilføj **ammunition** – begrænset antal skud
3. Lav **to sten** der falder samtidig
4. Gør stenene **hurtigere** når score stiger
5. Tilføj **3 liv** før spillet slutter
6. Vis **score hele tiden** ved at bruge display.show(score) når ingen sten er der

---

# 👑 Ekstra udfordringer (svære)

## 1. Flere sten med en liste

```python
# Før while loop:
rocks = [
    [random.randint(0,4), 0],
    [random.randint(0,4), 2]
]

# I din while loop (erstat rock_x og rock_y kode):

# Bevæg alle sten
for rock in rocks:
    rock[1] += 1  # y position
    if rock[1] > 4:
        rock[1] = 0
        rock[0] = random.randint(0,4)

# Tjek om nogen sten rammer spilleren
for rock in rocks:
    if rock[1] == 4 and rock[0] == player:
        display.show(Image.SKULL)
        sleep(2000)
        break

# Tegn alle sten
for rock in rocks:
    display.set_pixel(rock[0], rock[1], 9)

# Tjek om skud rammer nogen sten
if bullet_active:
    for rock in rocks:
        if bullet_x == rock[0] and bullet_y <= rock[1]:
            score += 1
            rock[1] = 0
            rock[0] = random.randint(0,4)
            bullet_active = False
            break
```

## 2. Flere skud samtidig

```python
# Før while loop:
bullets = []

# I din while loop (erstat bullet kode):

# Skyd (kan nu skyde flere gange)
if button_a.is_pressed() and button_b.is_pressed():
    if len(bullets) < 3:  # Max 3 skud på skærmen
        bullets.append([player, 4])
    sleep(200)  # Undgå at skyde for hurtigt

# Bevæg alle skud
for bullet in bullets:
    bullet[1] -= 1

# Fjern skud der er ude af skærmen
bullets = [b for b in bullets if b[1] >= 0]

# Tjek om nogen skud rammer stenen
for bullet in bullets:
    if bullet[0] == rock_x and bullet[1] <= rock_y:
        score += 1
        rock_y = 0
        rock_x = random.randint(0,4)
        bullet[1] = -1  # Marker til sletning
        break

bullets = [b for b in bullets if b[1] >= 0]  # Rens igen

# Tegn alle skud
for bullet in bullets:
    display.set_pixel(bullet[0], bullet[1], 5)
```

## 3. Power-ups

Lav en power-up der falder ned og giver ekstra point eller ammunition!

```python
powerup_x = random.randint(0,4)
powerup_y = 0
powerup_active = False

# Hvis spiller samler power-up:
if powerup_y == 4 and powerup_x == player:
    score += 10
    display.show(Image.HEART)
    sleep(500)
```

---

# 🔧 Hvis din kode ikke virker

Tjek:

- Python **indrykninger**
- at `while True:` stadig er der
- at variabelnavne er stavet rigtigt
- prøv små ændringer og test igen

---

# 🚀 Bonus spil

Hvis du bliver færdig kan du prøve:

- 🐍 Snake
- 🐦 Flappy Bird
- 🚀 Space shooter
- 🎲 Terning
- 📡 Radio multiplayer spil

---

💡 **Programmeringshemmelighed:**

De bedste programmører laver fejl hele tiden.  
De prøver bare igen.
