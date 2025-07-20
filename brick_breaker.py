# 3. Ütközés az ütővel
# Ha a labda eltalálja az ütőt (paddle):

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falütközés teszt")

brick_width = 75
brick_height = 20
brick_gap = 5
rows = 5
cols = 10

wall_width = cols * brick_width + (cols - 1) * brick_gap
start_x = (WIDTH - wall_width) // 2
start_y = 50

def get_random_row_colors():
    return [tuple(random.randint(50, 255) for _ in range(3)) for _ in range(rows)]

def generate_bricks():
    bricks = []
    row_colors = get_random_row_colors()
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * (brick_width + brick_gap)
            y = start_y + row * (brick_height + brick_gap)
            brick = pygame.Rect(x, y, brick_width, brick_height)
            bricks.append((brick, row_colors[row]))
    return bricks

bricks = generate_bricks()

paddle = pygame.Rect(350, 550, 100, 10)
paddle_speed = 5

ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
dx, dy = 4, -4

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            bricks = generate_bricks()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= paddle_speed
        paddle.x = max(paddle.x, 0)
    if keys[pygame.K_RIGHT]:
        paddle.x += paddle_speed
        paddle.x = min(paddle.x, WIDTH - paddle.width)

    ball.x += dx
    ball.y += dy

    if ball.left <= 0 or ball.right >= WIDTH:
        dx *= -1
    if ball.top <= 0:
        dy *= -1
    if ball.bottom >= HEIGHT:
        ball.x = WIDTH // 2
        ball.y = HEIGHT // 2
        dx, dy = 4, -4

    if ball.colliderect(paddle):
        dy *= -1

    screen.fill((0, 0, 0))

    for brick, color in bricks:
        pygame.draw.rect(screen, color, brick)
        pygame.draw.rect(screen, (255, 255, 255), brick, 2)

    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
