def is_digit(n):
    return n in [0,1,2,3,4,5,6,7,8,9]

def is_valid_isbn(isbn):
    ns = [
        int(n) for n in isbn
        if is_digit(int(n))
    ]

    if len(ns) != 13:
        return False

    odd_indexed_ns = (
        n*3 if index % 2 == 1 else n
        for index, n in enumerate(ns)
    )

    total = sum(odd_indexed_ns)

    return total % 10 == 0

class Book:
    def __init__(self, title, isbn):
        try:
            if title:
                self.__title = title
        except:
            raise RuntimeError("Title cannot be empty")

        try:
            if is_valid_isbn(isbn):
                self.__isbn = isbn
        except:
            raise RuntimeError("ISBN is not valid")  

    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn