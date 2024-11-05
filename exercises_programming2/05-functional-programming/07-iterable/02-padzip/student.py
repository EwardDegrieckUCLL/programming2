class PadZip:
    def __init__(self, left, right, padding=None):
        self.__left = left
        self.__right = right
        self.__padding = padding
        self.__current_index = 0
        self.__max_len = max(len(left), len(right))
        self.__min_len = min(len(left), len(right))

    def left_bigger(self):
        return len(self.__left) > len(self.__right)

    def __next__(self):
        if self.__current_index >= self.__max_len:
            raise StopIteration
        elif self.__current_index < self.__min_len:
            result = (self.__left[self.__current_index], self.__right[self.__current_index])
        else:
            if self.left_bigger():
                result = (self.__left[self.__current_index], self.__padding)
            else:
                result = (self.__padding, self.__right[self.__current_index])

        self.__current_index += 1
        return result

    def __iter__(self):
        return self
    
    # solution by lector is far more superior, however I'm proud I found a solution!!!
