class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for i in range(len(self.books)-1, -1, -1):
            if self.books[i].author == book.author and self.books[i].title == book.title:
                del self.books[i]

    def search_books(self, search_string):
        search_string = search_string.lower()
        result = []
        for book in self.books:
            if (search_string in book.author.lower()) or (search_string in book.title.lower()):
                result.append(book)
        return result
        
