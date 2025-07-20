# 1. Labda mozgása
# A labdát a sebességvektorával mozgatod minden frame-ben:

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

# ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
# dx, dy = 4, -4

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

#     ball.x += dx
#     ball.y += dy

#     screen.fill((0, 0, 0))

#     for brick, color in bricks:
#         pygame.draw.rect(screen, color, brick)
#         pygame.draw.rect(screen, (255, 255, 255), brick, 2)

#     pygame.draw.rect(screen, (255, 255, 255), paddle)
#     pygame.draw.ellipse(screen, (255, 255, 255), ball)

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()

# 2. Falütközés
# Ha a labda eléri a pálya szélét (bal/jobb vagy feklső/alsó)

# import pygame
# import random

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Falütközés teszt")

# brick_width = 75
# brick_height = 20
# brick_gap = 5
# rows = 5
# cols = 10

# # Fal szélesség kiszámítása, hogy középre tudd igazítani
# wall_width = cols * brick_width + (cols - 1) * brick_gap
# start_x = (WIDTH - wall_width) // 2
# start_y = 50

# def get_random_row_colors():
#     return [tuple(random.randint(50, 255) for _ in range(3)) for _ in range(rows)]

# def generate_bricks():
#     bricks = []
#     row_colors = get_random_row_colors()
#     for row in range(rows):
#         for col in range(cols):
#             x = start_x + col * (brick_width + brick_gap)
#             y = start_y + row * (brick_height + brick_gap)
#             brick = pygame.Rect(x, y, brick_width, brick_height)
#             bricks.append((brick, row_colors[row]))
#     return bricks

# bricks = generate_bricks()

# paddle = pygame.Rect(350, 550, 100, 10)
# paddle_speed = 5

# ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
# dx, dy = 4, -4

# clock = pygame.time.Clock()
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
#             bricks = generate_bricks()

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         paddle.x -= paddle_speed
#         paddle.x = max(paddle.x, 0)
#     if keys[pygame.K_RIGHT]:
#         paddle.x += paddle_speed
#         paddle.x = min(paddle.x, WIDTH - paddle.width)

#     ball.x += dx
#     ball.y += dy

#     if ball.left <= 0 or ball.right >= WIDTH:
#         dx *= -1
#     if ball.top <= 0:
#         dy *= -1
#     if ball.bottom >= HEIGHT:
#         ball.x = WIDTH // 2
#         ball.y = HEIGHT // 2
#         dx, dy = 4, -4

#     screen.fill((0, 0, 0))

#     for brick, color in bricks:
#         pygame.draw.rect(screen, color, brick)
#         pygame.draw.rect(screen, (255, 255, 255), brick, 2)

#     pygame.draw.rect(screen, (255, 255, 255), paddle)
#     pygame.draw.ellipse(screen, (255, 255, 255), ball)

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()

# 3. Ütközés az ütővel
# Ha a labda eltalálja az ütőt (paddle):

# import pygame
# import random

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Falütközés teszt")

# brick_width = 75
# brick_height = 20
# brick_gap = 5
# rows = 5
# cols = 10

# wall_width = cols * brick_width + (cols - 1) * brick_gap
# start_x = (WIDTH - wall_width) // 2
# start_y = 50

# def get_random_row_colors():
#     return [tuple(random.randint(50, 255) for _ in range(3)) for _ in range(rows)]

# def generate_bricks():
#     bricks = []
#     row_colors = get_random_row_colors()
#     for row in range(rows):
#         for col in range(cols):
#             x = start_x + col * (brick_width + brick_gap)
#             y = start_y + row * (brick_height + brick_gap)
#             brick = pygame.Rect(x, y, brick_width, brick_height)
#             bricks.append((brick, row_colors[row]))
#     return bricks

# bricks = generate_bricks()

# paddle = pygame.Rect(350, 550, 100, 10)
# paddle_speed = 5

# ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
# dx, dy = 4, -4

# clock = pygame.time.Clock()
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
#             bricks = generate_bricks()

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         paddle.x -= paddle_speed
#         paddle.x = max(paddle.x, 0)
#     if keys[pygame.K_RIGHT]:
#         paddle.x += paddle_speed
#         paddle.x = min(paddle.x, WIDTH - paddle.width)

#     ball.x += dx
#     ball.y += dy

#     if ball.left <= 0 or ball.right >= WIDTH:
#         dx *= -1
#     if ball.top <= 0:
#         dy *= -1
#     if ball.bottom >= HEIGHT:
#         ball.x = WIDTH // 2
#         ball.y = HEIGHT // 2
#         dx, dy = 4, -4

#     if ball.colliderect(paddle):
#         dy *= -1

#     screen.fill((0, 0, 0))

#     for brick, color in bricks:
#         pygame.draw.rect(screen, color, brick)
#         pygame.draw.rect(screen, (255, 255, 255), brick, 2)

#     pygame.draw.rect(screen, (255, 255, 255), paddle)
#     pygame.draw.ellipse(screen, (255, 255, 255), ball)

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()

# 4. Tégla-ütközés és törlés
# Végig kell menni minden téglán, és megnézni, hogy a labda ütközik-e vele. Ha igen:
# – fordítsd meg a dy irányt (pattanás)
# – töröld a téglát a listából (így eltűnik)
# – növeld a pontszámot

# import pygame
# import random

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Falütközés teszt")

# brick_width = 75
# brick_height = 20
# brick_gap = 5
# rows = 5
# cols = 10

# wall_width = cols * brick_width + (cols - 1) * brick_gap
# start_x = (WIDTH - wall_width) // 2
# start_y = 50

# def get_random_row_colors():
#     return [tuple(random.randint(50, 255) for _ in range(3)) for _ in range(rows)]

# def generate_bricks():
#     bricks = []
#     row_colors = get_random_row_colors()
#     for row in range(rows):
#         for col in range(cols):
#             x = start_x + col * (brick_width + brick_gap)
#             y = start_y + row * (brick_height + brick_gap)
#             brick = pygame.Rect(x, y, brick_width, brick_height)
#             bricks.append((brick, row_colors[row]))
#     return bricks

# bricks = generate_bricks()

# paddle = pygame.Rect(350, 550, 100, 10)
# paddle_speed = 5

# ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
# dx, dy = 4, -4

# score = 0

# clock = pygame.time.Clock()
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
#             bricks = generate_bricks()
#             score = 0

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         paddle.x -= paddle_speed
#         paddle.x = max(paddle.x, 0)
#     if keys[pygame.K_RIGHT]:
#         paddle.x += paddle_speed
#         paddle.x = min(paddle.x, WIDTH - paddle.width)

#     ball.x += dx
#     ball.y += dy

#     if ball.left <= 0 or ball.right >= WIDTH:
#         dx *= -1
#     if ball.top <= 0:
#         dy *= -1
#     if ball.bottom >= HEIGHT:
#         ball.x = WIDTH // 2
#         ball.y = HEIGHT // 2
#         dx, dy = 4, -4

#     if ball.colliderect(paddle):
#         dy *= -1

#     for brick in bricks[:]:
#         rect, color = brick
#         if ball.colliderect(rect):
#             dy *= -1
#             bricks.remove(brick)
#             score += 1
#             break

#     screen.fill((0, 0, 0))

#     for brick, color in bricks:
#         pygame.draw.rect(screen, color, brick)
#         pygame.draw.rect(screen, (255, 255, 255), brick, 2)

#     pygame.draw.rect(screen, (255, 255, 255), paddle)
#     pygame.draw.ellipse(screen, (255, 255, 255), ball)

#     font = pygame.font.SysFont(None, 36)
#     score_text = font.render(f"Pontszám: {score}", True, (255, 255, 255))
#     screen.blit(score_text, (10, 10))

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()

# HÁZI FELADAT
# • Valósítsd meg a “level up” funkciót: Ha elfogynak a téglák, írj ki “You Win!” üzenetet, és az N billentyűvel indíts új szintet (rakj ki új falat, legyen gyorsabb a labda)!
# • Adj hozzá hangot a téglákhoz: minden törésnél szólaljon meg egy hangeffekt (pl. pygame.mixer.Sound('brick.wav').play()).

# import pygame
# import random

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Breakout - Level Up és Hang")

# brick_sound = pygame.mixer.Sound('brick.mp3')

# brick_width = 75
# brick_height = 20
# brick_gap = 5
# rows = 5
# cols = 10

# wall_width = cols * brick_width + (cols - 1) * brick_gap
# start_x = (WIDTH - wall_width) // 2
# start_y = 50

# def get_random_row_colors():
#     return [tuple(random.randint(50, 255) for _ in range(3)) for _ in range(rows)]

# def generate_bricks():
#     bricks = []
#     row_colors = get_random_row_colors()
#     for row in range(rows):
#         for col in range(cols):
#             x = start_x + col * (brick_width + brick_gap)
#             y = start_y + row * (brick_height + brick_gap)
#             brick = pygame.Rect(x, y, brick_width, brick_height)
#             bricks.append((brick, row_colors[row]))
#     return bricks

# bricks = generate_bricks()

# paddle = pygame.Rect(350, 550, 100, 10)
# paddle_speed = 5

# ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
# dx, dy = 4, -4

# score = 0
# level = 1
# game_won = False

# clock = pygame.time.Clock()
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_r:
#                 bricks = generate_bricks()
#                 score = 0
#                 level = 1
#                 dx, dy = 4, -4
#                 game_won = False
#             if event.key == pygame.K_n and game_won:
#                 bricks = generate_bricks()
#                 score = 0
#                 level += 1
#                 dx *= 1.2
#                 dy *= 1.2
#                 ball.x = WIDTH // 2
#                 ball.y = HEIGHT // 2
#                 game_won = False

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         paddle.x -= paddle_speed
#         paddle.x = max(paddle.x, 0)
#     if keys[pygame.K_RIGHT]:
#         paddle.x += paddle_speed
#         paddle.x = min(paddle.x, WIDTH - paddle.width)

#     if not game_won:
#         ball.x += dx
#         ball.y += dy

#     if ball.left <= 0 or ball.right >= WIDTH:
#         dx *= -1
#     if ball.top <= 0:
#         dy *= -1
#     if ball.bottom >= HEIGHT:
#         ball.x = WIDTH // 2
#         ball.y = HEIGHT // 2
#         dx, dy = 4 * level, -4 * level

#     if ball.colliderect(paddle):
#         dy *= -1

#     for brick in bricks[:]:
#         rect, color = brick
#         if ball.colliderect(rect):
#             dy *= -1
#             bricks.remove(brick)
#             brick_sound.play()
#             score += 1
#             break

#     if len(bricks) == 0:
#         game_won = True

#     screen.fill((0, 0, 0))

#     for brick, color in bricks:
#         pygame.draw.rect(screen, color, brick)
#         pygame.draw.rect(screen, (255, 255, 255), brick, 2)

#     pygame.draw.rect(screen, (255, 255, 255), paddle)
#     pygame.draw.ellipse(screen, (255, 255, 255), ball)

#     font = pygame.font.SysFont(None, 36)
#     score_text = font.render(f"Pontszám: {score}   Szint: {level}", True, (255, 255, 255))
#     screen.blit(score_text, (10, 10))

#     if game_won:
#         win_font = pygame.font.SysFont(None, 72)
#         win_text = win_font.render("YOU WIN!", True, (255, 255, 0))
#         screen.blit(win_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
#         info_text = font.render("Nyomj N-t az új szinthez", True, (255, 255, 255))
#         screen.blit(info_text, (WIDTH // 2 - 150, HEIGHT // 2 + 20))

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()
