from .DefaultColor import DefaultColor
from .DefaultRectArea import DefaultRectArea
from .DefaultText import DefaultText
import pygame

class DefaultButton:
    def __init__(self, area : DefaultRectArea, text : DefaultText, sound : str | None = None):
        self.__area = area
        self.__default_border_color = self.__area.getColorTuple()
        self.__setText(text)
        self.__default_text_color = self.__text.getColorTuple()
        self.__setSound(sound)

    def __setText(self, text : DefaultText):
        self.__text = text

        text_x = self.__area.getX() + (self.__area.getWidth()//2)
        text_y = self.__area.getY() + (self.__area.getHeight()//2)

        self.__text.setX(text_x)
        self.__text.setY(text_y)

    def __setSound(self, sound : str | None = None):
        try:
            self.__sound = pygame.mixer.Sound(sound)
        except:
            self.__sound = None

    def playSoundOnMouseClick(self, mouse_pos : tuple[int, int]):
        if self.__sound is not None and self.__area.pointInArea(mouse_pos):
            self.__sound.play()

    def drawButton(self, screen : pygame.Surface):
        pygame.draw.rect(screen, self.__area.getColorTuple(), self.__area.getRect(), self.__area.getBorder())
        self.__text.drawText(screen)

    def changeColorOnHoover(self, mouse_pos : tuple[int, int], hoover_color : DefaultColor):
        if self.__area.pointInArea(mouse_pos):
            self.__area.setColor(hoover_color)
            self.__text.setColor(hoover_color)
        else:
            self.__area.setColor(self.__default_border_color)
            self.__text.setColor(self.__default_text_color)
        