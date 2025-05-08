from .DefaultColor import DefaultColor
import pygame

class DefaultCircArea:
    
    def __init__(self, center : tuple[int, int], radius : float, color : str | tuple[int, int, int] | DefaultColor = DefaultColor("white")):
        self.setCenter(center)
        self.setX(center[0])
        self.setY(center[1])
        self.setRadius(radius)
        self.setDiameter(radius)
        self.setColor(color)

    def setColor(self, color : str | tuple[int, int, int] | DefaultColor = DefaultColor("white")):
        if isinstance(color, DefaultColor):
            self.__color = color
        else:
            self.__color = DefaultColor(color)
    
    def getColor(self) -> DefaultColor:
        return self.__color
    
    def setCenter(self, center : tuple[int, int]):
        self.__center = center
        self.setX(center[0])
        self.setY(center[1])
    
    def getCenter(self) -> tuple[int, int]:
        return self.__center
    
    def setX(self, x_coord : int):
        self.__x_coord = x_coord

    def getX(self) -> int:
        return self.__x_coord
    
    def incrementX(self, increment : int = 1):
        self.__x_coord += increment
    
    def setY(self, y_coord : int):
        self.__y_coord = y_coord

    def getY(self) -> int:
        return self.__y_coord
    
    def incrementY(self, increment : int = 1):
        self.__y_coord += increment
    
    def setRadius(self, radius : float):
        self.__radius = radius

    def getRadius(self) -> float:
        return self.__radius
    
    def incrementRadius(self, increment : float = 1):
        self.__radius += increment
    
    def setDiameter(self, radius : float):
        self.__diameter = 2*radius
    
    def getDiameter(self) -> float:
        return self.__diameter

    def draw(self, screen : pygame.Surface):
        pygame.draw.circle(screen, self.__color.getTuple(), self.__center, self.__radius)

    def pointInArea(self, coord : tuple[int, int]) -> bool:
        if (self.__x_coord - coord[0])**2 + (self.__y_coord - coord[1])**2 < self.__radius**2:
            return True
        return False
    
    def distanceToPoint(self, coord : tuple[int, int]) -> float:
        return ((self.__x_coord - coord[0])**2 + (self.__y_coord - coord[1])**2)**(1/2)