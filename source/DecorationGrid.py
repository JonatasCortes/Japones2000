from .DefaultColor import DefaultColor
from .DefaultRectArea import DefaultRectArea
from .DefaultCircArea import DefaultCircArea
import pygame

class DecorationGrid:
    def __init__(self, area : DefaultRectArea, radius : float, spacement : int):
        self.__step = 0
        self.__chanel = 0
        self.__area = area
        self.__radius = radius
        self.__spacement = spacement
        self.__color = area.getColor()
        self.setGrid()

    def getColor(self) -> DefaultColor:
        return self.__color

    def setGrid(self):

        self.__dots_per_row = 0
        self.__dots_per_column = 0

        center = [self.__area.getX(), self.__area.getY()]
        self.__grid = []

        while center[1] < self.__area.getY() + self.__area.getHeight():

            center[0] = self.__area.getX()
            self.__dots_per_column+=1

            while center[0] < self.__area.getX() + self.__area.getWidth():

                center_tuple = tuple(center[:])
                circle = DefaultCircArea(center_tuple, self.__radius, self.__color.getTuple())

                self.__grid.append(circle)
                center[0] += 2*self.__radius + self.__spacement

                self.__dots_per_row += 1

            center[1] += 2*self.__radius + self.__spacement

        self.__dots_per_row //= self.__dots_per_column
    
    def drawGrid(self, screen : pygame.Surface, dynamic : bool = False, mouse_pos : tuple[int, int] = (-1, -1), mouse_radius : float = 20):
        if dynamic:
            start = 0 if self.__chanel == 0 else self.__step
            end = self.__step if self.__chanel == 0 else len(self.__grid)

            for color in self.__grid[start:end]:
                color.setColor(self.__color)
                color.draw(screen)

            if self.__step < len(self.__grid):
                self.__step += self.__dots_per_row
            else:
                self.__chanel = 1 - self.__chanel  # Alterna entre 0 e 1
                self.__step = 0

        if mouse_pos != (-1, -1):
            for color in self.__grid:
                if color.distanceToPoint(mouse_pos) < mouse_radius:
                    color.setColor(self.__color)
                    color.draw(screen)