"""Create a Book class that accepts title and author. Implement:

__str__ to return the string "Book: <title>" when printed.
__repr__ to return the string Book('<title>', '<author>')."""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'Книга: {self.title}'

    def __repr__(self):
        return f'Book(\'{self.title}\', \'{self.author}\')'

