import pygame
from source.DefaultColor import DefaultColor
from source.DefaultText import DefaultText
from source.DefaultRectArea import DefaultRectArea
from source.DefaultButton import DefaultButton

# region SCREEN INFO

screen_width = 640
screen_height = 720

# endregion

# region TITLE INFO

title_text = "日本の二千"
title_size = 100
title_x_pos = screen_width//2
title_y_pos = 100
title_color = DefaultColor((0, 0, 0))
title_color_custom = 1
title = DefaultText(title_text, title_size, title_x_pos, title_y_pos)

# endregion

# region HIRAGANA BUTTON INFO
hiragana_button_width = 160
hiragana_button_height = 65
hiragana_button_x_coord = screen_width//2 - hiragana_button_width//2
hiragana_button_y_coord = screen_height//2
hiragana_button_color = DefaultColor("white")
hiragana_button_area = DefaultRectArea(hiragana_button_x_coord, hiragana_button_y_coord, hiragana_button_width, hiragana_button_height, color= hiragana_button_color)
hiragana_button_text = DefaultText("ひらがな", 16, color= hiragana_button_color)
hiragana_button = DefaultButton(hiragana_button_area, hiragana_button_text, hiragana_button_color)

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

        title_color.rainbow(3)
        title.setColor(title_color)
        title.drawText(screen)
        '''
        hiragana_button_color.rainbow(3)
        hiragana_button_text.setColor(hiragana_button_color)
        hiragana_button_area.setColor(hiragana_button_color)
        '''
        hiragana_button.drawButton(screen)
        hiragana_button.changeColorOnHoover(mouse_pos, "cyan")
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()

mainLoop()
