class AssocList:
    def __init__(self):
        self.__items = []

    def __setitem__(self, key, value):
        for i in range(len(self.__items)):
            if self.__items[i][0] == key:
                # already in list, let's update value
                del self.__items[i]
                self.__items.append([key, value])  
        else:
            self.__items.append([key, value])

    def __getitem__(self, key):
        for i in range(len(self.__items)):
            if self.__items[i][0] == key:
                return self.__items[i][1]
            
    def __contains__(self, key):
        for i in range(len(self.__items)):
            if self.__items[i][0] == key:
                return True