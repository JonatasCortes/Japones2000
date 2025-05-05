from .DefaultColor import DefaultColor
import pygame

class DefaultText:
    
    def __init__(self, text : str, size : int, x_pos : int | None = None, y_pos : int | None = None, color : DefaultColor | str | tuple[int, int, int] | None = None):
        self.__text = text
        self.__size = size
        self.setX(x_pos)
        self.setY(y_pos)
        self.setColor(color)

    def drawText(self, screen : pygame.Surface):

        font = pygame.font.SysFont("MS Gothic", self.__size)

        text_surface = font.render(self.__text, True, self.__color.getTuple())
        text_rect = text_surface.get_rect(center=(self.__x_pos, self.__y_pos))

        screen.blit(text_surface, text_rect)

    def setColor(self, color : DefaultColor | str | tuple[int, int, int] | None = None):
        if isinstance(color, DefaultColor):
            self.__color = color
        else:
            self.__color = DefaultColor(color)

    def getColorName(self) -> str:
        return self.__color.getName()
    
    def getColorTuple(self) -> tuple[int, int, int]:
        return self.__color.getTuple()
    
    def getText(self) -> str:
        return self.__text
    
    def setX(self, x_pos : int | None = None):
        if x_pos is None:
            self.__x_pos = 0
        elif isinstance(x_pos, int):
            self.__x_pos = x_pos
        else:
            raise ValueError("O valor da coordenada x de um DefaultText deve ser inteiro ou nulo")
    
    def setY(self, y_pos : int | None = None):
        if y_pos is None:
            self.__y_pos = 0
        elif isinstance(y_pos, int):
            self.__y_pos = y_pos
        else:
            raise ValueError("O valor da coordenada y de um DefaultText deve ser inteiro ou nulo")

    def getX(self) -> int:
        return self.__x_pos
    
    def getY(self) -> int:
        return self.__y_pos
    
    def getSize(self) -> int:
        return self.__size