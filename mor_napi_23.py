# # 1. Ütő kirajzolása és mozgatása
# Először hozzuk létre az ütőt: ez egy téglalap, amit mozgatni tudsz balra-jobbra a képernyő alján.
# A pygame.Rect(350, 550, 100, 10) azt jelenti: bal felső sarka (350, 550), 100 pixel széles, 10 pixel magas. A paddle.x-et növelve/csökkentve mozgatod balra-jobbra.
# A bal/jobb nyíl leütésekor növeld vagy csökkentsd az x-et, DE mindig ellenőrizd, hogy ne menjen ki a képernyőről!

# import pygame

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Ütő mozgatása sys nélkül")

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# paddle = pygame.Rect(350, 550, 100, 10)
# paddle_speed = 5

# clock = pygame.time.Clock()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         paddle.x -= paddle_speed
#         if paddle.x < 0:
#             paddle.x = 0
#     if keys[pygame.K_RIGHT]:
#         paddle.x += paddle_speed
#         if paddle.x > WIDTH - paddle.width:
#             paddle.x = WIDTH - paddle.width

#     screen.fill(BLACK)
#     pygame.draw.rect(screen, WHITE, paddle)
#     pygame.display.flip()

#     clock.tick(60)

# pygame.quit()

# 2. Téglafal (bricks) lista létrehozása
# Most jön a legizgalmasabb rész: az egész falat listából építjük fel!
# Az üres bricks = [] listába minden egyes téglát (egy téglalap) külön hozzáadunk, egy ciklussal – sőt, két ciklussal: kívül sorokra, belül oszlopokra.
# A row jelenti a sort (fentről lefelé), a col az oszlopot (balról jobbra). Minden tégla pozícióját egy képlet adja, hogy szépen rendezett falat kapjunk.

# import pygame

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Csak téglalistát készítünk")

# brick_width = 75
# brick_height = 20
# brick_gap = 5
# rows = 5
# cols = 10

# wall_width = cols * brick_width + (cols - 1) * brick_gap
# start_x = (WIDTH - wall_width) // 2
# start_y = 50

# bricks = []
# for row in range(rows):
#     for col in range(cols):
#         brick_x = start_x + col * (brick_width + brick_gap)
#         brick_y = start_y + row * (brick_height + brick_gap)
#         brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
#         bricks.append(brick)

# print(f"Összesen {len(bricks)} tégla lett létrehozva.")

# # 3. Téglafal kirajzolása
# # Most már csak minden frame-ben végig kell menni a bricks listán, és minden téglát kirajzolni:
# # A szín minden sorban más (így lesz látványos), és vékony kerettel is megjelenítjük.

# import pygame

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Téglafal és ütő")

# brick_width = 75
# brick_height = 20
# brick_gap = 5
# rows = 5
# cols = 10

# wall_width = cols * brick_width + (cols - 1) * brick_gap
# start_x = (WIDTH - wall_width) // 2
# start_y = 50

# row_colors = [
#     (255, 0, 0),
#     (255, 165, 0),
#     (255, 255, 0),
#     (0, 128, 0),
#     (0, 0, 255)
# ]

# bricks = []
# for row in range(rows):
#     for col in range(cols):
#         brick_x = start_x + col * (brick_width + brick_gap)
#         brick_y = start_y + row * (brick_height + brick_gap)
#         brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
#         bricks.append((brick, row_colors[row]))

# paddle = pygame.Rect(350, 550, 100, 10)
# paddle_speed = 5

# clock = pygame.time.Clock()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         paddle.x -= paddle_speed
#         if paddle.x < 0:
#             paddle.x = 0
#     if keys[pygame.K_RIGHT]:
#         paddle.x += paddle_speed
#         if paddle.x > WIDTH - paddle.width:
#             paddle.x = WIDTH - paddle.width

#     screen.fill((0, 0, 0))

#     for brick, color in bricks:
#         pygame.draw.rect(screen, color, brick)
#         pygame.draw.rect(screen, (255, 255, 255), brick, 2)

#     pygame.draw.rect(screen, (255, 255, 255), paddle)

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()

# HÁZI FELADAT
# • Színezd minden sort más színnel (pl. első sor piros, második sárga…).
# • Adj hozzá egy R billentyűt, ami újragenerálja az egész téglafalat, ha lenyomod! (Tipp: ehhez elég újra lefuttatni ugyanazt a brick-generáló ciklust.)

# import pygame
# import random

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Téglafal és ütő újragenerálás")

# brick_width = 75
# brick_height = 20
# brick_gap = 5
# rows = 5
# cols = 10

# wall_width = cols * brick_width + (cols - 1) * brick_gap
# start_x = (WIDTH - wall_width) // 2
# start_y = 50

# row_colors = [
#     (255, 0, 0),
#     (255, 165, 0),
#     (255, 255, 0),
#     (0, 128, 0),
#     (0, 0, 255)
# ]

# def generate_bricks():
#     bricks = []
#     row_colors = get_random_row_colors()
#     for row in range(rows):
#         for col in range(cols):
#             brick_x = start_x + col * (brick_width + brick_gap)
#             brick_y = start_y + row * (brick_height + brick_gap)
#             brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
#             bricks.append((brick, row_colors[row]))
#     return bricks

# def get_random_row_colors():
#     return [tuple(random.randint(50, 255) for _ in range(3)) for _ in range(rows)]

# bricks = generate_bricks()

# paddle = pygame.Rect(350, 550, 100, 10)
# paddle_speed = 5

# clock = pygame.time.Clock()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_r:
#                 bricks = generate_bricks()

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         paddle.x -= paddle_speed
#         if paddle.x < 0:
#             paddle.x = 0
#     if keys[pygame.K_RIGHT]:
#         paddle.x += paddle_speed
#         if paddle.x > WIDTH - paddle.width:
#             paddle.x = WIDTH - paddle.width

#     screen.fill((0, 0, 0))

#     for brick, color in bricks:
#         pygame.draw.rect(screen, color, brick)
#         pygame.draw.rect(screen, (255, 255, 255), brick, 2)

#     pygame.draw.rect(screen, (255, 255, 255), paddle)

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()
