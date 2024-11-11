import pytest
from book import *


@pytest.mark.parametrize('name, isbn', [
    ('Alice in wonderland', '978-3-16-148410-0'),
    ('The Bible', "978-1779501127"),
    ('Generic book', '978-92-95055-02-5')
])


def test_valid_creation(name, isbn):
    book = Book(name, isbn)

    assert book.title == name
    assert book.isbn == isbn

@pytest.mark.parametrize('name, isbn', [
    ('', '978-3-16-148410-0'),
    (None, "978-1779501127"),
    ('', '978-92-95055-02-5')
])

def test_creation_with_invalid_title(name, isbn):
    with pytest.raises(RuntimeError):
        Book(name, isbn)


@pytest.mark.parametrize('name, isbn', [
    ('Alice in wonderland', '978-3-6-148410-0'),
    ('The Bible', "978-1789501127"),
    ('Generic book', '978-92-95056-02-5')
])

def test_creation_with_invalid_isbn(name, isbn):
    with pytest.raises(RuntimeError):
        Book(name, isbn)
