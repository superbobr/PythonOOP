"""Create a class Library that has:

A class attribute location (default value: "No location").
An instance method add_book(self, title) that adds a book to the list self.books (initialize this list in __init__).
A class method set_location(cls, loc) that updates the location attribute for the entire class.
A static method info() that returns the string "Library system v1.0".
 In the main part of the code:

Create a Library object and add several books to it.
Change the location using set_location().
Call info().
Print the contents of self.books and the current location."""


class Library:
    location = 'No location'

    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)

    @classmethod
    def set_location(cls, loc):
        cls.location = loc

    @classmethod
    def get_location(cls):
        return f'Location: {cls.location}'

    @staticmethod
    def info():
        return 'Library system v1.0'


new_library = Library()
new_library.add_book('1984')
new_library.add_book('Pride and Prejudice')
Library.set_location('City Center')

print(new_library.info())
print(Library.get_location())
print(f'Books: {new_library.books}')