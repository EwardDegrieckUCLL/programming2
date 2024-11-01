class LengthConverter:
    def __init__(self):
        pass

    @property
    def meter(self):
        return self.__meter
    
    @meter.setter
    def meter(self, value):
        self.__meter = value
        self.__feet = 3.2808 * value
        self.__inch = 39.3701 * value

    @property
    def feet(self):
        return self.__feet
    
    @feet.setter
    def feet(self, value):
        self.__feet = value
        self.__meter = 0.3048 * value
        self.__inch =  12 * value



    @property
    def inch(self):
        return self.__inch
    
    @inch.setter
    def inch(self, value):
        self.__inch = value
        self.__feet = (1/12) * value
        self.__meter = 0.0254 * value