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
kana_button_text_size = 200
kana_button_text_value = "あ"

kana_button_default_color = DefaultColor("white")
kana_button_hoover_color = DefaultColor("magenta")

kana_button_x_coord = screen_horisontal_center
kana_button_y_coord = screen_vertical_center - vertical_padding

kana_button_area = DefaultRectArea(kana_button_x_coord, kana_button_y_coord, color= kana_button_default_color, border= 10)
kana_button_text = DefaultText(kana_button_text_value,kana_button_text_size, color= kana_button_default_color)
kana_button = DefaultButton(kana_button_area, kana_button_text, hoover_color= kana_button_hoover_color, sound=r"kana_sounds\a.wav")
#endregion

# region RETURN BUTTON INFO
return_button_text_size = 45
return_button_text_value = "戻る"

return_button_default_color = DefaultColor("white")
return_button_hoover_color = DefaultColor("strong_pink")

return_button_x_coord = screen_horisontal_center
return_button_y_coord = screen_vertical_center + 2*vertical_padding

return_button_area = DefaultRectArea(return_button_x_coord, return_button_y_coord, color= return_button_default_color)
return_button_text = DefaultText(return_button_text_value, return_button_text_size, color= return_button_default_color)
return_button = DefaultButton(return_button_area, return_button_text, hoover_color= return_button_hoover_color)
#endregion

# region NEXT BUTTON INFO
next_button_text_size = 45
next_button_text_value = " 進む"

next_button_default_color = DefaultColor("white")
next_button_hoover_color = DefaultColor("aqua_green")

next_button_x_coord = screen_horisontal_center
next_button_y_coord = screen_vertical_center + vertical_padding

next_button_area = DefaultRectArea(next_button_x_coord, next_button_y_coord, color= next_button_default_color)
next_button_text = DefaultText(next_button_text_value, next_button_text_size, color= next_button_default_color)
next_button = DefaultButton(next_button_area, next_button_text, hoover_color= next_button_hoover_color)
# endregion

def hiraganaScreen(screen : pygame.Surface):

    running = True

    hiragana_index = 0
    hiragana_characters = [key for key, _ in Hiragana.getSoundDict().items()]
    hiragana_sounds = [sound for _, sound in Hiragana.getSoundDict().items()]

    kana_button_clicked = False

    while running:

        screen.fill("black")

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if return_button.isClicked(mouse_pos, event):
                running = False

            if kana_button.isClicked(mouse_pos, event):
                kana_button.playSound()
                kana_button_clicked = True
                kana_button_default_color.setColor("red")
                
            if next_button.isClicked(mouse_pos, event):
                hiragana_index += 1
                kana_button_clicked = False
                kana_button_default_color.setColor("white")

        kana_button.drawButton(screen)
        if kana_button_clicked:
            kana_button_area.getColor().rainbow(3)
            #print(kana_button_area.getColor().getTuple())

        return_button.drawButton(screen)
        return_button.changeColorOnHoover(mouse_pos)

        next_button.drawButton(screen)
        next_button.changeColorOnHoover(mouse_pos)
        
        if hiragana_index > len(hiragana_characters)-1: hiragana_index = 0

        if hiragana_characters[hiragana_index] != kana_button_text.getText():
            kana_button_text.setText(hiragana_characters[hiragana_index])
            kana_button.setSound(hiragana_sounds[hiragana_index])
        
        pygame.display.flip()
