import pygame
from source.DefaultColor import DefaultColor
from source.DefaultText import DefaultText
from source.DefaultRectArea import DefaultRectArea
from source.DefaultCircArea import DefaultCircArea
from source.DefaultButton import DefaultButton
from source.DecorationGrid import DecorationGrid
from kana_classes.Hiragana import Hiragana

# region SCREEN INFO
screen_width = 640
screen_height = 720
screen_horisontal_center = screen_width//2
screen_vertical_center = screen_height//2
horisontal_padding = screen_width//10
vertical_padding = screen_height//8
# endregion

# region KANA BUTTON INFO
kana_button_text_size = 100
kana_button_text_value = "bah"

kana_button_default_color = DefaultColor("white")
kana_button_hoover_color = DefaultColor("magenta")

kana_button_x_coord = screen_horisontal_center
kana_button_y_coord = screen_vertical_center

kana_button_area = DefaultRectArea(kana_button_x_coord, kana_button_y_coord, color= kana_button_default_color)
kana_button_text = DefaultText(kana_button_text_value,kana_button_text_size, color= kana_button_default_color)
kana_button = DefaultButton(kana_button_area, kana_button_text, hoover_color= kana_button_hoover_color, sound=r"kana_sounds\ru.wav")
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

def hiraganaScreen(screen : pygame.Surface):

    running = True

    while running:

        screen.fill("black")

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or exit_button.isClicked(mouse_pos, event):
                running = False
            if kana_button.isClicked(mouse_pos, event):
                kana_button.playSound()

        kana_button.drawButton(screen, mouse_pos)
        exit_button.drawButton(screen, mouse_pos)
        
        pygame.display.flip()
