# 3. Kirajzolás
# Minden frame-ben iteráld végig a bricks listát, és a dict-ből használd a "color" mezőt a
# pygame.draw.rect()-hez.

import pygame
import random
import time

WIDTH, HEIGHT = 800, 600
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICK_GAP = 5
ROWS = 5
COLS = 10
PADDLE_SPEED = 5
BALL_SIZE = 15
FLASH_DURATION = 100
WHITE = (255, 255, 255)
SQUASH_DURATION = 100
SQUASH_SCALE = 0.7
COLOR_RED = "red"
COLOR_BLUE = "blue"
COLOR_GREEN = "green"
COLOR_YELLOW = "yellow"
POINT_LOW = 10
POINT_MEDIUM = 20
POINT_HIGH = 50

COLOR_MAP = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0)
}

def create_level(num_bricks, color, points, y_start):
    bricks = []
    total_width = num_bricks * BRICK_WIDTH + (num_bricks - 1) * BRICK_GAP
    start_x = (WIDTH - total_width) // 2
    for i in range(num_bricks):
        x = start_x + i * (BRICK_WIDTH + BRICK_GAP)
        bricks.append({"pozíció": (x, y_start), "szín": color, "pont": points})
    return bricks

levels = [
    create_level(10, COLOR_RED, POINT_LOW, 50),
    create_level(10, COLOR_RED, POINT_LOW, 50) + create_level(10, COLOR_YELLOW, POINT_MEDIUM, 80),
    create_level(10, COLOR_GREEN, POINT_LOW, 50) + create_level(10, COLOR_YELLOW, POINT_HIGH, 80) + create_level(10, COLOR_BLUE, POINT_MEDIUM, 110)
]

def generate_bricks(level_index):
    bricks = []
    for brick_data in levels[level_index]:
        pos = brick_data["pozíció"]
        color = brick_data["szín"]
        points = brick_data["pont"]
        rect = pygame.Rect(pos[0], pos[1], BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append({
            "rect": rect,
            "color": COLOR_MAP[color],
            "points": points
        })
    return bricks

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brickbreaker")
clock = pygame.time.Clock()

brick_sound = pygame.mixer.Sound('brick.mp3')
paddle_sound = pygame.mixer.Sound('paddlesound.mp3')
lose_sound = pygame.mixer.Sound('lose.mp3')
pygame.mixer.music.load('backgroundsound.mp3')
pygame.mixer.music.play(-1)

volume = 0.5
pygame.mixer.music.set_volume(volume)
brick_sound.set_volume(volume)
paddle_sound.set_volume(volume)
lose_sound.set_volume(volume)

paddle = pygame.Rect(350, 550, 100, 10)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
dx, dy = 4, -4
score = 0
level = 1
game_won = False
paused_music = False
ball_trail = []
TRAIL_LENGTH = 10
squash_start_time = 0
is_squashing = False
popup_start_time = 0
popup_duration = 500
show_popup = False
flash_bricks = []
particle_effects = []
bricks = generate_bricks(level - 1)
running = True

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                paused_music = not paused_music
                if paused_music:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_r:
                bricks = generate_bricks(level - 1)
                flash_bricks = []
                particle_effects = []
                score = 0
                dx, dy = 4, -4
                game_won = False
                ball.x, ball.y = WIDTH // 2, HEIGHT // 2
                ball_trail = []
            if event.key == pygame.K_n and game_won:
                level += 1
                bricks = generate_bricks((level - 1) % len(levels))
                flash_bricks = []
                particle_effects = []
                score = 0
                dx *= 1.2
                dy *= 1.2
                ball.x, ball.y = WIDTH // 2, HEIGHT // 2
                game_won = False
                ball_trail = []
            if event.key in [pygame.K_EQUALS, pygame.K_KP_PLUS]:
                volume = min(volume + 0.1, 1.0)
            if event.key in [pygame.K_MINUS, pygame.K_KP_MINUS]:
                volume = max(volume - 0.1, 0.0)
            pygame.mixer.music.set_volume(volume)
            brick_sound.set_volume(volume)
            paddle_sound.set_volume(volume)
            lose_sound.set_volume(volume)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x = max(paddle.x - PADDLE_SPEED, 0)
    if keys[pygame.K_RIGHT]:
        paddle.x = min(paddle.x + PADDLE_SPEED, WIDTH - paddle.width)

    if not game_won:
        ball.x += dx
        ball.y += dy
        ball_trail.append((ball.centerx, ball.centery))
        if len(ball_trail) > TRAIL_LENGTH:
            ball_trail.pop(0)

    if ball.left <= 0 or ball.right >= WIDTH:
        dx *= -1
    if ball.top <= 0:
        dy *= -1
    if ball.bottom >= HEIGHT:
        lose_sound.play()
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        dx, dy = 4 * level, -4 * level
        ball_trail = []

    if ball.colliderect(paddle):
        dy *= -1
        paddle_sound.play()
        squash_start_time = current_time
        is_squashing = True

    for brick in bricks[:]:
        rect = brick["rect"]
        if ball.colliderect(rect):
            dy *= -1
            brick_sound.play()
            bricks.remove(brick)
            flash_bricks.append((rect, brick["color"], current_time))
            score += 1
            popup_start_time = current_time
            show_popup = True
            break

    flash_bricks = [(rect, color, start_time) for rect, color, start_time in flash_bricks if current_time - start_time < FLASH_DURATION]
    if len(bricks) == 0:
        game_won = True

    screen.fill((0, 0, 0))

    for brick in bricks:
        rect = brick["rect"]
        color = brick["color"]
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, WHITE, rect, 2)

    for rect, color, _ in flash_bricks:
        pygame.draw.rect(screen, color, rect)

    for i, (x, y) in enumerate(ball_trail):
        alpha = int(255 * (i + 1) / TRAIL_LENGTH)
        trail_color = (alpha, alpha, alpha)
        pygame.draw.circle(screen, trail_color, (x, y), BALL_SIZE // 2)

    if is_squashing and current_time - squash_start_time < SQUASH_DURATION:
        squash_width = paddle.width * 1.1
        squash_height = paddle.height * SQUASH_SCALE
        squash_rect = pygame.Rect(
            paddle.centerx - squash_width // 2,
            paddle.centery - squash_height // 2,
            squash_width,
            squash_height
        )
        pygame.draw.rect(screen, WHITE, squash_rect)
    else:
        is_squashing = False
        pygame.draw.rect(screen, WHITE, paddle)

    pygame.draw.ellipse(screen, WHITE, ball)

    font = pygame.font.SysFont(None, 36)
    screen.blit(font.render(f"Pontszám: {score}   Szint: {level}", True, WHITE), (10, 10))

    if show_popup and current_time - popup_start_time < popup_duration:
        popup_font = pygame.font.SysFont(None, 100)
        popup_surface = popup_font.render("+1", True, (255, 255, 255))
        popup_surface.set_alpha(200 - int(200 * (current_time - popup_start_time) / popup_duration))
        popup_rect = popup_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(popup_surface, popup_rect)
    else:
        show_popup = False

    if game_won:
        win_font = pygame.font.SysFont(None, 72)
        screen.blit(win_font.render("YOU WIN!", True, (255, 255, 0)), (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        screen.blit(font.render("Nyomj N-t az új szinthez", True, WHITE), (WIDTH // 2 - 150, HEIGHT // 2 + 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
