# # 1. Ütő kirajzolása és mozgatása
# Először hozzuk létre az ütőt: ez egy téglalap, amit mozgatni tudsz balra-jobbra a képernyő alján.
# A pygame.Rect(350, 550, 100, 10) azt jelenti: bal felső sarka (350, 550), 100 pixel széles, 10 pixel magas. A paddle.x-et növelve/csökkentve mozgatod balra-jobbra.
# A bal/jobb nyíl leütésekor növeld vagy csökkentsd az x-et, DE mindig ellenőrizd, hogy ne menjen ki a képernyőről!

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ütő mozgatása sys nélkül")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

paddle = pygame.Rect(350, 550, 100, 10)
paddle_speed = 5

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= paddle_speed
        if paddle.x < 0:
            paddle.x = 0
    if keys[pygame.K_RIGHT]:
        paddle.x += paddle_speed
        if paddle.x > WIDTH - paddle.width:
            paddle.x = WIDTH - paddle.width

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()