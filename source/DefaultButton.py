from .DefaultColor import DefaultColor
from .DefaultRectArea import DefaultRectArea
from .DefaultText import DefaultText
import pygame

class DefaultButton:
    def __init__(self, area : DefaultRectArea, text : DefaultText, sound : str | None = None, hoover_color : DefaultColor = DefaultColor("white")):
        self.__area = area
        self.__area.setWidth(int(text.getSize()*len(text.getText())*1.2))
        self.__area.setHeight(int(text.getSize()*(1.8 - text.getSize()*0.003)))
        self.__area.setX(self.__area.getX() - self.__area.getWidth()//2)
        self.__area.setY(self.__area.getY() - self.__area.getHeight()//2)
        self.__default_border_color = self.__area.getColorTuple()
        self.__setText(text)
        self.__default_text_color = self.__text.getColorTuple()
        self.setSound(sound)
        self.__hoover_color = hoover_color

    def __setText(self, text : DefaultText):
        self.__text = text

        text_x = self.__area.getX() + (self.__area.getWidth()//2)
        text_y = self.__area.getY() + (self.__area.getHeight()//2)

        self.__text.setX(text_x)
        self.__text.setY(text_y)

    def setSound(self, sound : str | None = None):
        try:
            self.__sound = pygame.mixer.Sound(sound)
        except:
            self.__sound = None

    def playSound(self):
        self.__sound.play()

    def drawButton(self, screen : pygame.Surface, backgrownd_color : DefaultColor = DefaultColor("black")):

        pygame.draw.rect(screen, self.__area.getColorTuple(), self.__area.getRect(), self.__area.getBorder())

        border = self.__area.getBorder()
        button_backgrownd_rect = [self.__area.getX()+border, self.__area.getY()+border, self.__area.getWidth()-2*border, self.__area.getHeight()-2*border]
        pygame.draw.rect(screen, backgrownd_color.getTuple(), button_backgrownd_rect)
        
        self.__text.drawText(screen)

    def changeColorOnHoover(self, mouse_pos : tuple[int, int]):
        if self.__area.pointInArea(mouse_pos):
            self.__area.setColor(self.__hoover_color)
            self.__text.setColor(self.__hoover_color)
        else:
            self.__area.setColor(self.__default_border_color)
            self.__text.setColor(self.__default_text_color)

    def isClicked(self, mouse_pos : tuple[int, int], event : pygame.event.Event) -> DefaultRectArea:
        if event.type == pygame.MOUSEBUTTONDOWN and self.__area.pointInArea(mouse_pos):
            return True
        return False
    
    def getArea(self) -> DefaultRectArea:
        return self.__area
        