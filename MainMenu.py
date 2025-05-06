import pygame
from source.DefaultColor import DefaultColor
from source.DefaultText import DefaultText
from source.DefaultRectArea import DefaultRectArea
from source.DefaultButton import DefaultButton

# region SCREEN INFO

screen_width = 640
screen_height = 720
screen_horisontal_center = screen_width//2
screen_vertical_center = screen_height//2

# endregion

# region TITLE INFO

title_text = "日本の二千"
title_size = 100
title_x_pos = screen_horisontal_center
title_y_pos = 100
title_color = DefaultColor((0, 0, 0))
title_color_custom = 1
title = DefaultText(title_text, title_size, title_x_pos, title_y_pos)

# endregion

# region HIRAGANA BUTTON INFO
hiragana_button_text_size = 46
hiragana_button_text_value = "ひらがな"

hiragana_button_default_color = DefaultColor("white")
hiragana_button_hoover_color = DefaultColor("cyan")

hiragana_button_x_coord = screen_horisontal_center
hiragana_button_y_coord = screen_vertical_center

hiragana_button_area = DefaultRectArea(hiragana_button_x_coord, hiragana_button_y_coord, color= hiragana_button_default_color)
hiragana_button_text = DefaultText(hiragana_button_text_value,hiragana_button_text_size, color= hiragana_button_default_color)
hiragana_button = DefaultButton(hiragana_button_area, hiragana_button_text, hiragana_button_default_color)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


def mainLoop():

    running = True
    dt = 0

    while running:

        screen.fill("black")

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        title.getColor().rainbow(3)
        title.drawText(screen)

        hiragana_button.drawButton(screen)
        hiragana_button.changeColorOnHoover(mouse_pos, "cyan")
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()

mainLoop()
