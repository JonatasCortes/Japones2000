import pygame
from source.DefaultColor import DefaultColor
from source.DefaultText import DefaultText
from source.DefaultRectArea import DefaultRectArea
from source.DefaultButton import DefaultButton

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

area = DefaultRectArea(50, 50, 190, 70, 5, "white")
texto = DefaultText("バナナ banana", 25, color="white")
botao = DefaultButton(area, texto)
magenta = DefaultColor("magenta")

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    mouse_pos = pygame.mouse.get_pos()
    botao.changeColorOnHoover(mouse_pos, magenta)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    botao.drawButton(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

