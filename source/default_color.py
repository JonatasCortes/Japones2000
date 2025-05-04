class DefaultColor:

    color_dict = {
        "WHITE": (255, 255, 255),
        "NOT_TOO_WHITE": (220, 220, 220),
        "DRAWING_COLOR": (250, 250, 250),
        "BLACK": (0, 0, 0),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
        "YELLOW": (255, 255, 0),
        "CYAN": (0, 255, 255),
        "MAGENTA": (200, 0, 100),
        "GRAY": (128, 128, 128),
        "DARK_GRAY": (64, 64, 64),
        "LIGHT_GRAY": (192, 192, 192),
        "ORANGE": (255, 165, 0),
        "PINK": (255, 192, 203),
        "PURPLE": (128, 0, 128),
        "BROWN": (165, 42, 42),
        "GOLD": (255, 215, 0),
        "SILVER": (192, 192, 192),
        "NAVY": (0, 0, 128),
        "LIME": (0, 255, 0),
        "OLIVE": (128, 128, 0),
        "MAROON": (128, 0, 0),
        "TEAL": (0, 128, 128),
        "INDIGO": (75, 0, 130),
        "VIOLET": (238, 130, 238),
        "TURQUOISE": (64, 224, 208)
    }

    def tupleOfColor(self, color_name : str) -> tuple:
        for color_key in self.color_dict.keys():
            if color_name.upper() == color_key:
                return self.color_dict[color_key]
        raise ValueError("Cor ausente na classe DefaultColor não pode ser atribuida")
            
    def nameOfColor(self, color_tuple : tuple[int, int, int]) -> str:
        for color_key, color_value in self.color_dict.items():
            if color_tuple == color_value:
                return color_key
        raise ValueError("Cor ausente na classe DefaultColor não pode ser atribuida")
            
    def setColor(self, color : str | tuple[int, int, int] | None = None):
        if type(color) == str:
            self.__name = color.upper()
            self.__tuple = self.tupleOfColor(color)
        elif type(color) == tuple and len(color) == 3 and all(type(num) == int for num in color):
            self.__tuple = color
            self.__name = self.nameOfColor(color)
        else:
            self.__name = "BLACK"
            self.__tuple = (0, 0, 0)     
    
    def __init__(self, color : str | tuple[int, int, int] | None = None):
        self.setColor(color)

    def getName(self) -> str:
        return self.__name
    
    def getTuple(self) -> tuple[int, int, int]:
        return self.__tuple