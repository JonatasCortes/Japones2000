import pygame
pygame.init()
pygame.mixer.init()
from source.DefaultColor import DefaultColor
from source.DefaultText import DefaultText
from source.DefaultRectArea import DefaultRectArea
from source.DefaultCircArea import DefaultCircArea
from source.DefaultButton import DefaultButton
from source.DecorationGrid import DecorationGrid
from HiraganaMenu import hiraganaScreen

# region SCREEN INFO
screen_width = 640
screen_height = 720
screen_horisontal_center = screen_width//2
screen_vertical_center = screen_height//2
horisontal_padding = screen_width//10
vertical_padding = screen_height//8
# endregion

# region TITLE INFO
title_text = "日本の二千"
title_size = 100
title_x_pos = screen_horisontal_center
title_y_pos = 100
title_color = DefaultColor("black")
title_color_custom = 1
title = DefaultText(title_text, title_size, title_x_pos, title_y_pos)
# endregion

# region HIRAGANA BUTTON INFO
hiragana_button_text_size = 45
hiragana_button_text_value = "ひらがな"

hiragana_button_default_color = DefaultColor("white")
hiragana_button_hoover_color = DefaultColor("sky_blue")

hiragana_button_x_coord = screen_horisontal_center
hiragana_button_y_coord = screen_vertical_center - vertical_padding

hiragana_button_area = DefaultRectArea(hiragana_button_x_coord, hiragana_button_y_coord, color= hiragana_button_default_color)
hiragana_button_text = DefaultText(hiragana_button_text_value,hiragana_button_text_size, color= hiragana_button_default_color)
hiragana_button = DefaultButton(hiragana_button_area, hiragana_button_text, hoover_color= hiragana_button_hoover_color)
#endregion

# region KATAKANA BUTTON INFO
katakana_button_text_size = 45
katakana_button_text_value = "カタカナ"

katakana_button_default_color = DefaultColor("white")
katakana_button_hoover_color = DefaultColor("light_purple")

katakana_button_x_coord = screen_horisontal_center
katakana_button_y_coord = screen_vertical_center

katakana_button_area = DefaultRectArea(katakana_button_x_coord, katakana_button_y_coord, color= katakana_button_default_color)
katakana_button_text = DefaultText(katakana_button_text_value,katakana_button_text_size, color= katakana_button_default_color)
katakana_button = DefaultButton(katakana_button_area, katakana_button_text, hoover_color= katakana_button_hoover_color)
#endregion

# region KANJI BUTTON INFO
kanji_button_text_size = 45
kanji_button_text_value = "漢字"

kanji_button_default_color = DefaultColor("white")
kanji_button_hoover_color = DefaultColor("aqua_green")

kanji_button_x_coord = screen_horisontal_center
kanji_button_y_coord = screen_vertical_center + vertical_padding

kanji_button_area = DefaultRectArea(kanji_button_x_coord, kanji_button_y_coord, color= kanji_button_default_color)
kanji_button_text = DefaultText(kanji_button_text_value, kanji_button_text_size, color= kanji_button_default_color)
kanji_button = DefaultButton(kanji_button_area, kanji_button_text, hoover_color= kanji_button_hoover_color)
#endregion

# region EXIT BUTTON INFO
exit_button_text_size = 45
exit_button_text_value = "終了"

exit_button_default_color = DefaultColor("white")
exit_button_hoover_color = DefaultColor("strong_pink")

exit_button_x_coord = screen_horisontal_center
exit_button_y_coord = screen_vertical_center + 2*vertical_padding

exit_button_area = DefaultRectArea(exit_button_x_coord, exit_button_y_coord, color= exit_button_default_color)
exit_button_text = DefaultText(exit_button_text_value, exit_button_text_size, color= exit_button_default_color)
exit_button = DefaultButton(exit_button_area, exit_button_text, hoover_color= exit_button_hoover_color)
#endregion

# region LEFT DECORATION GRID INFO
left_decoration_grid_area_width = 30
left_decoration_grid_area_height = screen_height
left_decoration_grid_area_x_pos = 0
left_decoration_grid_area_y_pos = 0
left_decoration_grid_color = DefaultColor("black")
left_decoration_grid_area = DefaultRectArea(x_pos=left_decoration_grid_area_x_pos, y_pos=left_decoration_grid_area_y_pos, width= left_decoration_grid_area_width, height= left_decoration_grid_area_height, color= left_decoration_grid_color)

left_decoration_grid_radius = 1
left_decoration_grid_spacement = 0
left_decoration_grid = DecorationGrid(left_decoration_grid_area, left_decoration_grid_radius, left_decoration_grid_spacement)
# endregion

# region RIGHT DECORATION GRID INFO
right_decoration_grid_area_width = 30
right_decoration_grid_area_height = screen_height
right_decoration_grid_area_x_pos = screen_width - right_decoration_grid_area_width
right_decoration_grid_area_y_pos = 0
right_decoration_grid_color = DefaultColor("black")
right_decoration_grid_area = DefaultRectArea(x_pos=right_decoration_grid_area_x_pos, y_pos=right_decoration_grid_area_y_pos, width= right_decoration_grid_area_width, height= right_decoration_grid_area_height, color= right_decoration_grid_color)

right_decoration_grid_radius = 1
right_decoration_grid_spacement = 0
right_decoration_grid = DecorationGrid(right_decoration_grid_area, right_decoration_grid_radius, right_decoration_grid_spacement)
# endregion

# region CENTER DECORATION GRID INFO
center_decoration_grid_area_width = screen_width - left_decoration_grid_area_width - right_decoration_grid_area_width
center_decoration_grid_area_height = screen_height
center_decoration_grid_area_x_pos = left_decoration_grid_area_x_pos + left_decoration_grid_area_width
center_decoration_grid_area_y_pos = 3
center_decoration_grid_color = DefaultColor("black")
center_decoration_grid_area = DefaultRectArea(x_pos=center_decoration_grid_area_x_pos, y_pos=center_decoration_grid_area_y_pos, width= center_decoration_grid_area_width, height= center_decoration_grid_area_height, color= center_decoration_grid_color)

center_decoration_grid_radius = 10
center_decoration_grid_spacement = 3
center_decoration_grid = DecorationGrid(center_decoration_grid_area, center_decoration_grid_radius, center_decoration_grid_spacement)
# endregion

screen = pygame.display.set_mode((screen_width, screen_height))


def mainLoop():

    running = True

    while running:

        screen.fill("black")

        mouse_pos = pygame.mouse.get_pos()

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if exit_button.isClicked(mouse_pos, event):
                running = False

            if hiragana_button.isClicked(mouse_pos, event):
                hiraganaScreen(screen)

            if katakana_button.isClicked(mouse_pos, event):
                pass

            if kanji_button.isClicked(mouse_pos, event):
                pass

        left_decoration_grid.getColor().rainbow(3)
        left_decoration_grid.drawGrid(screen, dynamic=True)

        right_decoration_grid.getColor().rainbow(3)
        right_decoration_grid.drawGrid(screen, dynamic=True)

        center_decoration_grid.getColor().rainbow(3)
        center_decoration_grid.drawGrid(screen, mouse_pos=mouse_pos, mouse_radius=25)

        title.getColor().rainbow(3)
        title.drawText(screen)

        hiragana_button.drawButton(screen)
        hiragana_button.changeColorOnHoover(mouse_pos)

        katakana_button.drawButton(screen)
        katakana_button.changeColorOnHoover(mouse_pos)

        kanji_button.drawButton(screen)
        kanji_button.changeColorOnHoover(mouse_pos)

        exit_button.drawButton(screen)
        exit_button.changeColorOnHoover(mouse_pos)
        
        pygame.display.flip()

    pygame.quit()

mainLoop()
