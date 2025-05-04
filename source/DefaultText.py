from .DefaultColor import DefaultColor

class DefaultText:
    
    def __init__(self, text : str, size : int, x_pos : int, y_pos : int, color : DefaultColor | str | tuple[int, int, int] | None = None):
        self.__text = text
        self.__size = size
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.setColor(color)

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
    
    def getX(self) -> int:
        return self.__x_pos
    
    def getY(self) -> int:
        return self.__y_pos
    
    def getSize(self) -> int:
        return self.__size