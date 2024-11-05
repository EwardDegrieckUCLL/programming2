class Cycle:
    def __init__(self, list):
        self.__list = list
        self.__current_index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__current_index == len(self.__list):
            self.__current_index = 1
            return self.__list[0]
        else:
            result = self.__list[self.__current_index]
            self.__current_index += 1
            return result
        
    # oplossing van lector is superieur, doch trots op eigen oplossing
    
    # mijn versie van de code cfr. lector (MAAR MSS BEN IK WEL VERKEERD! ook al werkt deze via pytest):
class Cycleeuw:
    def __init__(self, elts):
        self.__elts = list(elts)
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.__elts[(self.__index) % len(self.__elts)]
        self.__index += 1
        return result