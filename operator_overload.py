class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return (self.name == other.name) and (self.age == other.age)


class Playlist:
    def __init__(self, title, songs):
        self.title = title
        self.songs = songs

    def __len__(self):
        return len(self.songs)


class Grades:
    def __init__(self):
        self._grades = {"math": 5, "history": 4}

    def __getitem__(self, subject):
        return self._grades[subject]


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Item({self.name!r}, {self.price!r})'

    def __lt__(self, other):
        return self.price < other.price