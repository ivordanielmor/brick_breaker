# 2. Téglafal (bricks) lista létrehozása
# Most jön a legizgalmasabb rész: az egész falat listából építjük fel!
# Az üres bricks = [] listába minden egyes téglát (egy téglalap) külön hozzáadunk, egy ciklussal – sőt, két ciklussal: kívül sorokra, belül oszlopokra.
# A row jelenti a sort (fentről lefelé), a col az oszlopot (balról jobbra). Minden tégla pozícióját egy képlet adja, hogy szépen rendezett falat kapjunk.

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Csak téglalistát készítünk")

brick_width = 75
brick_height = 20
brick_gap = 5
rows = 5
cols = 10

wall_width = cols * brick_width + (cols - 1) * brick_gap
start_x = (WIDTH - wall_width) // 2
start_y = 50

bricks = []
for row in range(rows):
    for col in range(cols):
        brick_x = start_x + col * (brick_width + brick_gap)
        brick_y = start_y + row * (brick_height + brick_gap)
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        bricks.append(brick)

print(f"Összesen {len(bricks)} tégla lett létrehozva.")
