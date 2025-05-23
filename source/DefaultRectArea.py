from .DefaultColor import DefaultColor

class DefaultRectArea:

    def __init__(self, x_pos : int, y_pos : int, width : int = 0, height : int = 0, border : int = 5, color : DefaultColor | str | tuple[int, int, int] | None = None):
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.setWidth(width)
        self.setHeight(height)
        self.__border = border
        self.setColor(color)

    def setWidth(self, width : int):
        self.__width = width

    def setHeight(self, height : int):
        self.__height = height

    def setX(self, x_pos : int):
        self.__x_pos = x_pos

    def setY(self, y_pos : int):
        self.__y_pos = y_pos

    def setColor(self, color : DefaultColor | str | tuple[int, int, int] | None = None):
        if isinstance(color, DefaultColor):
            self.__color = color
        else:
            self.__color = DefaultColor(color)
    
    def getColor(self) -> DefaultColor:
        return self.__color

    def getColorName(self) -> str:
        return self.__color.getName()

    def getColorTuple(self) -> tuple[int, int, int]:
        return self.__color.getTuple()
    
    def getX(self) -> int:
        return self.__x_pos
    
    def getY(self) -> int:
        return self.__y_pos
    
    def getWidth(self) -> int:
        return self.__width
    
    def getHeight(self) -> int:
        return self.__height
    
    def getRect(self) -> tuple[int, int, int, int]:
        return (self.__x_pos, self.__y_pos, self.__width, self.__height)
    
    def getBorder(self) -> int | None:
        return self.__border
    
    def pointInArea(self, coord : tuple[int, int]) -> bool:
        if self.__x_pos <= coord[0] <= (self.__x_pos + self.__width) and self.__y_pos <= coord[1] <= (self.__y_pos + self.__height):
            return True
        return False